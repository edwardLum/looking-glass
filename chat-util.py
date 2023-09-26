from enum import Enum, auto

class PropertyType(Enum):
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    OBJECT = "object"  # Default value

class PropertyCreator:
    def __init__(self, property_name, property_type=PropertyType.OBJECT, property_description=None):
        self.property_name = property_name
        self.property_type = property_type
        self.property_description = property_description

    def create_property(self):
        property_data = {
            "type": self.property_type.value
        }

        if self.property_description:
            property_data["description"] = self.property_description

        return {
            self.property_name: property_data
        }

# Test
property_obj = PropertyCreator("sampleProperty", PropertyType.STRING, "A sample string property")
print(property_obj.create_property())

