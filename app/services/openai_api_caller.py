import os
import json

import openai

class Caller():
    """
    A class to manage calls and completions with OpenAI's API.

    Attributes:
    - prompt (str): The user's input or prompt for which a completion is desired.
    - function (dict): The function configuration for OpenAI's API call.
    - messages (list[dict]): A list of message objects, initially containing the user's prompt.
    - function_call (dict): The function call configuration for OpenAI's API.

    Methods:
    - create_completion_call(): Make a chat completion call to OpenAI's API.
    - get_structured_completion(): Retrieve and structure the completion response from OpenAI's API.
    """

    def __init__(self, prompt, function):
        """
        Initializes the Caller class.

        Args:
        - prompt (str): The user's input or prompt.
        - function (dict): The function configuration for the API call.
        """
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
        """
        Make a chat completion call to OpenAI's API based on the provided prompt and function configuration.

        Returns:
        openai.ChatCompletion: The response from OpenAI's API.
        """
        return openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=self.messages,
            functions=[self.function],
            function_call=self.function_call
        )


    def get_structured_completion(self):
        """
        Retrieve the structured completion response from OpenAI's API, focusing on the function call's arguments.

        Returns:
        dict: The structured arguments from the completion response.
        """
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
