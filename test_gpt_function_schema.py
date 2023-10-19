from os import walk
import unittest

from function_schema import IntegerProperty, StringProperty, ArrayProperty, ArrayString


class TestDictSerialization(unittest.TestCase):
    def setUp(self):
        self.func_property_string = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                    }
                }

        self.func_property_integer = {
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                    }
                }

        self.func_properties = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                }
            }

        self.func_parameter = {
            'type': 'object',
            'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the person.'
                    },
                    'grades': {
                        'type': 'integer',
                        'description': 'GPA of the student.'
                    },
                }
            }

        self.func_property_array = {
                "commands": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "A terminal command string"
                    },
                    "description": "List of terminal command strings to be executed"
                }
            }

        self.func_property_array_of_objects = {
                    "tracklist": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "artist": {
                                    "type": "string",
                                    "description": "The artist of the track.",
                                },
                                "title": {
                                    "type": "string",
                                    "description": "The title of the track.",
                                },
                            }
                        },
                    },
                }

    def test_property_dict_serialization_simple(self):
        name =StringProperty(name="name",
                             description='Name of the person.')
        
        grades = IntegerProperty(name="grades", 
                                 description='GPA of the student.')

        self.assertEqual(self.func_property_string, 
                         name.model_dump(exclude_none=True))

        self.assertEqual(self.func_property_integer, 
                         grades.model_dump(exclude_none=True))



if __name__ == "__main__":
    unittest.main()
