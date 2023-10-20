from os import walk
import unittest

from function_schema import IntegerProperty, StringProperty, ArrayProperty, StringItem


class TestPropertySerialization(unittest.TestCase):
    def setUp(self):
        self.name = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                    }
                }

        self.grades = {
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                    }
                }

        self.properties = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                }
            }

        self.parameter = {
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

        self.commands = {
                "commands": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "description": "A terminal command string"
                    },
                    "description": "List of terminal command strings to be executed"
                }
            }

        self.array_of_objects = {
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

    def test_simple_property_serialization(self):
        name =StringProperty(name="name",
                             description='Name of the person.')

        grades = IntegerProperty(name="grades",
                                 description='GPA of the student.')

        self.assertEqual(self.name,
                         name.model_dump())

        self.assertEqual(self.grades,
                         grades.model_dump())



    def test_array_property_serialization(self):
        command =StringItem(description='A terminal command string')

        commands = ArrayProperty(name="commands",
                                 description='List of terminal command strings to be executed',
                                 items=command)

        self.assertEqual(self.commands,
                         commands.model_dump(exclude_none=True))


if __name__ == "__main__":
    unittest.main()
