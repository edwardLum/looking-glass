from pydantic import BaseModel

from typing import Union, List, Dict, Any, Optional

from pydantic.functional_serializers import model_serializer

from pprint import pprint

class Property(BaseModel):
    name: str
    description: str
    property_type: str

    @model_serializer
    def serialize_model(self):
        return {self.name: {
            "type": self.property_type,
            "description": self.description,
            }}

class Item(BaseModel):
    description: str
    property_type: str

    @model_serializer
    def serialize_model(self):
        return {
                "type": self.property_type,
                "description": self.description
                }

class StringProperty(Property):
    property_type: str = "string"

class IntegerProperty(Property):
    property_type: str = "integer"

class BooleanProperty(Property):
    property_type: str = "boolean"


class FloatProperty(Property):
    property_type: str = "float"

class StringItem(Item):
    property_type: str = "string"

class IntegerItem(Item):
    property_type: str = "integer"

class ArrayProperty(Property):
    property_type: str = "array"
    items: Union["StringItem",
                 "IntegerItem",
                 "ObjectItem"]

    @model_serializer
    def serialize_model(self):
        return {self.name: {
            "type": self.property_type,
            "items": self.items.model_dump(),
            "description": self.description,
            }}

class ObjectProperty(Property):
    property_type: str = "object"
    properties: List[Union[StringProperty,
                                IntegerProperty,
                                ArrayProperty,
                                BooleanProperty,
                                FloatProperty]]

    @model_serializer
    def serialize_model(self):
        properties_dict = {}
        for prop in self.properties:
            properties_dict.update(prop.model_dump())

        return {self.name: {
            "type": self.property_type,
            "properties": properties_dict,
            "description": self.description,
            }

    }

class ObjectItem(Item):
    description: Optional[str]
    property_type: str = "object"
    properties: List[Union[StringProperty,
                                IntegerProperty,
                                ArrayProperty,
                                BooleanProperty,
                                FloatProperty]]

    @model_serializer
    def serialize_model(self):
        properties_dict = {}
        for prop in self.properties:
            properties_dict.update(prop.model_dump())

        return {
            "type": self.property_type,
            "properties": properties_dict,
            }

class Function(BaseModel):
    description: str
    name: str
    properties: List[Union[StringProperty,
                            IntegerProperty,
                            ArrayProperty,
                            BooleanProperty,
                            FloatProperty]]

    @model_serializer
    def serialize_model(self):
        properties_dict = {}
        for prop in self.properties:
            properties_dict.update(prop.model_dump())

        return {
        "name": self.name,
        "description": self.description,
        "parameters": {
            "type": "object",
            "properties": properties_dict
        }
        }
