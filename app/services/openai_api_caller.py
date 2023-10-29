import os
import json

import openai

class Caller():

    def __init__(self, prompt, function):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.prompt = prompt
        self.function = function
        self.messages = [
        {
            "role": "user",
            "content": self.prompt
        }
        ]
        self.function_call = {"name": self.function["name"]}

    def create_completion_call(self):
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=self.messages,
            functions=[self.function],
            function_call=self.function_call
        )


    def get_structured_completion(self):
        completion = self.create_completion_call()
        content = completion.choices[0].message
        structured_completion = content.to_dict()['function_call']['arguments']

        return json.loads(structured_completion)

test_f = {
            "name": "get_tracklist",
            "description": "Gets a list of tracks from a query.",
            "parameters": {
                "type": "object",
                "properties": {
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
                },
                "required": ["tracklist"],
            }
        }
