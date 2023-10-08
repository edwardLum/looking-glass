import os
import json

from pprint import pprint
from openai.api_resources import completion

from pydantic import BaseModel, Field, field_validator, ValidationError, model_serializer, model_validator, ConfigDict
from typing import List, Union, Optional, Dict, Any

import openai


class ArrayItem (BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    item_type: str = Field(alias="type") 
    description: str
    

    @field_validator('item_type')
    @classmethod
    def validate_item_type(cls, value: str):
        allowed_types = {"string", "integer", "float", "boolean", "object", "array"}
        if value not in allowed_types:
            raise ValueError(f"Invalid type. Permitted types are: {', '.join(allowed_types)}")
        return value

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        return {
                "type": self.item_type,
                "description": self.description,
                }


class FunctionProperty(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    name: str
    property_type: str = Field(alias="type")
    description: Optional[str]
    items: Optional[ArrayItem] = None
    properties: Optional[List['FunctionProperty']] = None

    @field_validator('property_type')
    @classmethod
    def validate_property_type(cls, value: str):
        allowed_types = {"string", "integer", "float", "boolean", "object", "array"}
        if value not in allowed_types:
            raise ValueError(f"Invalid type. Permitted types are: {', '.join(allowed_types)}")
        return value

    @model_validator(mode='before')
    @classmethod
    def check_items_and_properties(cls, values: Any) -> Any:
        property_type = values.get('property_type')
        items = values.get('items')
        properties = values.get('properties')
        if property_type == 'array' and items is None:
            raise ValueError(f"items field is required for type array")
        elif property_type != 'array' and items is not None:
            raise ValueError(f"items field should be empty for type {property_type}")
        if property_type == 'object' and properties is None:
            raise ValueError(f"properties field is required for type object")
        elif property_type != 'object' and properties is not None:
            raise ValueError(f"properties field should be empty for type {property_type}")
        return values

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        if self.items:
            return {self.name: {
                        "type": self.property_type,
                        "description": self.description,
                        "items": self.items.model_dump(exclude_none=True)
                        }
                }
        return {self.name: {
                    "type": self.property_type,
                    "description": self.description,
                    }
            }

FunctionProperty.model_rebuild()


class FunctionProperties(BaseModel):
    properties: List[FunctionProperty]

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        property_dict = {}
        for func_property in self.properties:
            property_dict.update(func_property.model_dump(exclude_none=True))

        return property_dict

class FunctionParameter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    property_type: str = Field(default="object", alias="type")
    properties: FunctionProperties 
    required: Optional[List[str]] = None

    @model_serializer
    def serialize_model(self) -> Dict[str, Any]:
        return {'type': self.property_type,
                'properties': self.properties}
    

class Function(BaseModel):
    name: str
    description: str
    parameters: FunctionParameter

class FunctionCalling(BaseModel):
    model: str
    messages: List[dict]
    functions: List[Function]
    function_call: str


def query_simple():
    openai.api_key = os.getenv("OPENAI_API_KEY")
    example_input = "Generate a google ads keyword with the keyword theme of boxing gloves"

    completion = openai.ChatCompletion.create(
            model = 'gpt-3.5-turbo-0613',
            messages = [{'role': 'user', 'content': example_input}],
            functions = [create_function_calling_json(example_input)],
            function_call = 'auto',
            )

    reply_content = completion.choices[0].message
    ad_groups = reply_content.to_dict()['function_call']['arguments']
    return json.loads(ad_groups)
     
