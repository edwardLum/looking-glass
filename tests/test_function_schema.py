import pytest

from app.services.function_schema import IntegerProperty, ObjectItem, StringProperty, ArrayProperty, StringItem


@pytest.fixture
def name_property():
    name = {
            'name': {
                'type': 'string',
                'description': 'Name of the person.'
                }
            }
    return name


@pytest.fixture
def grade_property():
    grades = {
            'grades': {
                'type': 'integer',
                'description': 'GPA of the student.'
                }
            }
    return grades

@pytest.fixture
def array():
    return {
            "commands": {
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "A terminal command string"
                },
                "description": "List of terminal command strings to be executed"
            }
        }

def test_dict_equality():
    a = {"a": "b"}
    b = {"a": "b"}

    assert a == b


def test_simple_property():
    grades_dict = {
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                    }
                }

    name_dict = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                    }
                }

    name = StringProperty(name="name",
                         description='Name of the person.')

    grades = IntegerProperty(name="grades",
                             description='GPA of the student.')

    assert name.model_dump() == name_dict

    assert grades.model_dump() == grades_dict



def test_array_property():
    array_property = {
            "commands": {
                "type": "array",
                "items": {
                    "type": "string",
                    "description": "A terminal command string"
                },
                "description": "List of terminal command strings to be executed"
            }
        }
    command = StringItem(description='A terminal command string')

    commands = ArrayProperty(name="commands",
                             description='List of terminal command strings to be executed',
                             items=command)

    assert array_property == commands.model_dump(exclude_none=True)


def test_array_with_object():
    array_of_objects = {
                "tracklist": {
                    "type": "array",
                    "description": "A list of tracks",
                    "items": {
                        "type": "object",
                        "properties": {
                            "artist": {
                                "type": "string",
                                "description": "The artist of the track",
                            },
                            "title": {
                                "type": "string",
                                "description": "The title of the track",
                            },
                        }
                    },
                },
            }

    artist = StringProperty(name="artist",
                             description='The artist of the track')

    title = StringProperty(name="title",
                             description='The title of the track')

    track = ObjectItem(properties=[artist, title],
                        description="Whateer")

    tracklist = ArrayProperty(name="tracklist",
                             items=track,
                             description="A list of tracks")

    print(array_of_objects)
    print(tracklist.model_dump(exclude_none=True))

    assert array_of_objects == tracklist.model_dump(exclude_none=True)
