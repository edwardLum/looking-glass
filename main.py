import os

import openai 

from fastapi import FastAPI


openai.api_key = os.getenv("OPENAI_API_KEY")

# chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the 'sustainable fashion theme'"}])

theme="Sustainable Fashion Theme"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the following theme: Sustainable Fashion."}],
    functions=[
    {
        "name": "get_three_keywords",
        "description": "Get 3 keywords related to the theme provided",
        "parameters": {
            "type": "object",
            "properties": {
                "keyword_theme": {
                    "type": "string",
                    "description": "The theme of the keywords to be provided",
                },
            },
            "required": ["keyword_theme"],
        },
    }
],
    function_call={'name': "get_three_keywords"},
)

reply_content = completion.choices[0].message
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


def generate_prompt(animal):
    return """List 3 keywords for 'sustainable fashion'""".format(
        animal.capitalize()
    )
