import pytest

from app.services.function_schema import IntegerProperty, ObjectItem, StringProperty, ArrayProperty, StringItem


@pytest.fixture
def simple_properties():
    name = {
            'name': {
                'type': 'string',
                'description': 'Name of the person.'
                }
            }

    grades = {
            'grades': {
                'type': 'integer',
                'description': 'GPA of the student.'
                }
            }
    return {"name": name,
            "grades": grades}

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


@pytest.fixture
def array_of_objects():
    return {
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

def test_simple_property():
    name =StringProperty(name="name",
                         description='Name of the person.')

    grades = IntegerProperty(name="grades",
                             description='GPA of the student.')

    assert name == simple_properties["name"].model_dump()

    assert grades == simple_properties["grades"].model_dump()



def test_array_property():
    command =StringItem(description='A terminal command string')

    commands = ArrayProperty(name="commands",
                             description='List of terminal command strings to be executed',
                             items=command)

    assert array == commands.model_dump(exclude_none=True)


def test_array_with_object():
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

if __name__ == "__main__":
    unittest.main()
