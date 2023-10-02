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
async def get_structure(campaign_theme: str = "None"):
    return campaign_suggestion((campaign_theme)) 
    
@app.get("/keywords/")
async def get_keywords(keyword_theme: str = "None"):
    return keywords_suggestion(keyword_theme)

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
                                "ad_group_name": {
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

def keywords_suggestion(keyword_theme):

    openai.api_key = os.getenv("OPENAI_API_KEY")

    example_input = "Recommend 10 keywords that will be used in a Google Ads campaign. The keyword theme is {}.".format(keyword_theme)

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
                "name": "get_keywords",
                "description": "Gets a list of keywords from a query",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keywords": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "keyword": {
                                        "type": "string",
                                        "description": "A keyword."
                                    }
                                }
                            },
                            "description": "The list of keywords."
                        }
                    },
                    "required": ["keywords"]
                }
            }
            ])

    reply_content = completion.choices[0].message
    ad_groups = reply_content.to_dict()['function_call']['arguments']
    return json.loads(ad_groups)
