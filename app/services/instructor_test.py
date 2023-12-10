import instructor
from openai import OpenAI
from pydantic import BaseModel

client = instructor.patch((OpenAI()))

class Keyword(BaseModel):
    text: str
    match_type: str



keyword = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=Keyword,
        messages=[
            {"role": "user", "content": "Provide a keyword for a Google Ads ad group themed women's shoes."},
            ]
        )

