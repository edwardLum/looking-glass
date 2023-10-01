import openai
import os
import json


def tracklist():
    openai.api_key = os.getenv("OPENAI_API_KEY")

    example_input = "Recommend 5 ad groups with 10 keywords each, for a Google Ads campaign. The campaign theme is Sports Betting."

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user",
                "content": example_input,
            }
        ],
        functions=[
        {
            "name": "get_ad_groups",
            "description": "Gets a list of ad groups from a query",
            "parameters": {
                "type": "object",
                "properties": {
                    "ad_groups": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "group_name": {
                                    "type": "string",
                                    "description": "The name of the ad group."
                                },
                                "keywords": {
                                    "type": "array",
                                    "items": {
                                        "type": "object",
                                        "properties": {
                                            "keyword": {
                                                "type": "string",
                                                "description": "A keyword associated with the ad group."
                                            }
                                        }
                                    },
                                    "description": "The list of keywords associated with the ad group."
                                }
                            }
                        },
                        "description": "The list of ad groups."
                    }
                },
                "required": ["ad_groups"]
            }
        }

        ],
        function_call={"name": "get_ad_groups"}
    )
    reply_content = completion.choices[0].message
    ad_groups = reply_content.to_dict()['function_call']['arguments']
    return json.loads(ad_groups)




def manual_function():
    example_user_input = "Recommend me a tracklist of 20 tracks and remixes from 2019."

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user",
             "content": example_user_input
             }
        ],
        functions=[
            {
                "name": "get_tracklist", 
                "description": "Gets a list of tracks from a query",
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
                                        "description": "The artist of the track."
                                    },
                                    "title": {
                                        "type": "string",
                                        "description": "The title of the track."
                                    },
                                }
                            },
                        },
                    },
                    "required": ["tracklist"]
                }
            }

        ],
        function_call= {"name": "get_tracklist"},
    )
    print(completion)

