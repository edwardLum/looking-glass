import os

import openai 

from fastapi import FastAPI


openai.api_key = os.getenv("OPENAI_API_KEY")

# chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "List 3 related keywords for a Google Ads ad group themed with the 'sustainable fashion theme'"}])

example_user_input = "Provide three keywords to be used in a Google Ads ad group with the theme 'Boxing gloves'"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": example_user_input}],
        functions=[
        {
            "name": "get_keywords",
            "description": "Get a list of Google Ads keywords",
            "parameters": {
                "type": "object",
                "properties": {
                    "keywords": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "description": "A list of keywords"
                        },
                        "description": "List of Google Ads keywords to be added to an ad group"
                    }
                },
                "required": ["keywords"]
            }
        }
        ],
        function_call="auto",
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
