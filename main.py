import os

import openai 

from fastapi import FastAPI


openai.api_key = os.getenv("OPENAI_API_KEY")

chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the 'sustainable fashion theme'"}])

theme="Sustainable Fashion Theme"

completion = openai.ChatCompletion.create(
    model="gpt-4-0613",
    messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the theme: {}".format(theme)}],
    functions=[
    {
        "name": "get_three_keywords",
        "description": "Get 3 keywords related to the theme provided",
        "parameters": {
            "type": "string",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
    }
],
function_call="auto",
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def generate_prompt(animal):
    return """List 3 keywords for 'sustainable fashion'""".format(
        animal.capitalize()
    )
