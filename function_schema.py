from pydantic import BaseModel

from typing import Union, List, Dict, Any

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

class Item(Property):
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

class ArrayString(Item):
    property_type: str = "string"

class ArrayInteger(Item):
    property_type: str = "integer"

class ArrayProperty(Property):
    property_type: str = "array"
    items: Union["ArrayString", 
                 "ArrayInteger",
                 "ObjectProperty"]

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

    

if __name__=="__main__":
   artist = ArrayString(name="artist",
                           description="The artist of the track") 

   artists = ArrayProperty(name="artists",
                                items=artist,
                                description="A list of artists")

   artistProperty = StringProperty(name="artist",
                           description="The artist of the track") 

   titleProperty = StringProperty(name="title",
                               description="The title of the track")
   pprint(artists.model_dump())
   track = ObjectProperty(name="Track",
                          description="A track with artist and title",
                          properties=[artistProperty,
                                      titleProperty])

   pprint(track.model_dump())

