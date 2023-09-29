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

@app.get("/keywords/")
async def read_keywords(theme: str = "None", no_of_keywords: int = 3):
    pass
    
def keyword_function():
    no_of_keywords = FunctionProperty("number_of_keywords", "integer", description="The number of keywords to be returned by the function")
    keyword_theme = FunctionProperty("keyword_theme", "string", description="The theme of the keywords to be returned")
    keyword_func_param = FunctionParameter(required="[number_of_keywords, keyword_theme]", properties=[no_of_keywords, keyword_theme])
    keyword_func = Function("get_google_ads_keywords", "A function to generate given number of keywords based on given theme, to be used by a Google Ads campaign", keyword_func_param)

    return keyword_func.to_json()

def manual_function(theme, no_of_keywords):
    example_user_input = "Generate {} keywords to be used in a Google Ads campaign. Keyword theme is {}".format(no_of_keywords, theme)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": example_user_input}],
            functions=[
            {"name": "get_google_ads_keywords", 
             "description": "A function to generate given number of keywords based on given theme, to be used by a Google Ads campaign", 
             "parameters": {"type": "object", 
                            "properties": {
                                "keywords": {
                                    "type": "array", 
                                    "items": {
                                        "type": "string",
                                        "description": "A keyword to be used in a Google Ads."
                                        }
                                    }, 
                                "required": ["keywords"]
                                }
                            }
             }
            ],
            function_call="auto",
    )
    reply_content = completion.choices[0].message
    print(example_user_input)
    return reply_content

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
