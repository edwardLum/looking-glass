from pydantic import BaseModel, Field, field_validator, ValidationError, model_validator
from typing import List, Union, Optional, Dict, Any

class FunctionProperty(BaseModel):
    name: str
    property_type: str
    description: Optional[str]
    items: Optional['FunctionProperty'] = None
    properties: Optional[List['FunctionProperty']] = None

    @field_validator('property_type')
    def validate_property_type(cls, value):
        allowed_types = {"string", "integer", "float", "boolean", "object", "array"}
        if value not in allowed_types:
            raise ValueError(f"Invalid type. Permitted types are: {', '.join(allowed_types)}")
        return value

    @model_validator(mode='before')
    def check_items_and_properties(cls, values):
        property_type = values.get('property_type')
        items = values.get('items')
        properties = values.get('properties')
        if property_type == 'array' and items is None:
            raise ValidationError(f"items field is required for type array")
        elif property_type != 'array' and items is not None:
            raise ValidationError(f"items field should be empty for type {property_type}")
        if property_type == 'object' and properties is None:
            raise ValidationError(f"properties field is required for type object")
        elif property_type != 'object' and properties is not None:
            raise ValidationError(f"properties field should be empty for type {property_type}")
        return values

FunctionProperty.model_rebuild()

class FunctionParameter(BaseModel):
    param_type: str = Field(default="object", alias="type")
    properties: List[FunctionProperty]
    required: List[str]


class Function(BaseModel):
    name: str
    description: str
    parameters: FunctionParameter




