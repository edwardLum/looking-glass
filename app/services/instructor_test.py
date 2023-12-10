import instructor
from openai import OpenAI
from typing import List

from pydantic import BaseModel

client = instructor.patch((OpenAI()))

class Keyword(BaseModel):
    text: str
    match_type: str

class KeywordList(BaseModel):
    keywords: List[Keyword]

keyword = client.chat.completions.create(
        model="gpt-3.5-turbo",
        response_model=KeywordList,
        messages=[
            {"role": "user", "content": "Provide a list of keywords for a Google Ads ad group themed women's shoes."},
            ]
        )

