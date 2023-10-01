import json

import os

import openai 

from fastapi import FastAPI

from gpt_function import FunctionParameter, FunctionProperty, Function

openai.api_key = os.getenv("OPENAI_API_KEY")

# chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the 'sustainable fashion theme'"}])


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/campaign_structure/")
async def read_keywords(campaign_theme: str = "None"):
    return campaign_suggestion((campaign_theme)) 
    
def campaign_suggestion(campaign_theme):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    example_input = "Recommend 5 ad groups with 10 keywords each, for a Google Ads campaign. The campaign theme is {}.".format(campaign_theme)

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

def keyword_function():
    no_of_keywords = FunctionProperty("number_of_keywords", "integer", description="The number of keywords to be returned by the function")
    keyword_theme = FunctionProperty("keyword_theme", "string", description="The theme of the keywords to be returned")
    keyword_func_param = FunctionParameter(required="[number_of_keywords, keyword_theme]", properties=[no_of_keywords, keyword_theme])
    keyword_func = Function("get_google_ads_keywords", "A function to generate given number of keywords based on given theme, to be used by a Google Ads campaign", keyword_func_param)

    return keyword_func.to_json()

def simplified():
# Define the function schema
    functions = {
        "generate_keywords": {
            "type": "function",
            "args": {"theme": "string"},
            "output": {"keywords": "array"}
        }
    }

# Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        prompt="Generate keywords for the theme: travel",
        functions=functions,
        function_call={"name": "generate_keywords", "args": {"theme": "travel"}}
    )

# Extract the keywords from the response
    keywords = response['choices'][0]['function_call']['output']['keywords']
    print(keywords)


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

def manual_function_two(theme, no_of_keywords):
    # example_user_input = "How do I install Tensorflow for my GPU?"
    example_user_input = "Generate {} keywords to be used in a Google Ads campaign. Keyword theme is {}".format(no_of_keywords, theme)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": example_user_input}],
            functions=[
            {
                "name": "get_keywords",
                "description": "Get a list of 5 keywords to be used on a Google Ads campaign",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {
                                "type": "string",
                                "description": "A Google Ads keyword"
                            },
                            "description": " A list of 5 Google Ads keywords"
                        }
                    },
                    "required": ["keywords"]
                }
            }
            ],
            function_call={"name": "get_keywords"},
    )
    reply_content = completion.choices[0].message
    print(example_user_input)
    return reply_content

# keywords = reply_content.to_dict()['function_call']['arguments']
#  keywords = json.loads(keywords)#   print(keywords['keywords'])
