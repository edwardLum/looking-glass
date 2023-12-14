from enum import Enum

import instructor
from openai import OpenAI
from typing import List

from pydantic import BaseModel

from app.services.openai_api_caller import Caller 

client = instructor.patch((OpenAI()))


class MatchType(str, Enum):
    exact = "Exact"
    phrase = "Phrase"
    broad = "Broad"


class Keyword(BaseModel):
    text: str
    match_type: MatchType


class KeywordList(BaseModel):
    keywords: List[Keyword]


class KeywordSuggestion():
    def __init__(self, ad_group_theme, min_number_of_keywords=2, max_number_of_keywords=30):
        self.basic_prompt = "Recommend a list of Google Ads keywords, that will be used in the context of an Ad Group within a Google Ads campaign. Use the information below:"
        self.min_number_of_keywords = min_number_of_keywords
        self.max_number_of_keywords = max_number_of_keywords
        self.ad_group_theme = ad_group_theme
        self.prompt_customizer = f'Minimum number of keywords: {self.min_number_of_keywords} - Maximum number of keywords: {self.max_number_of_keywords} - Ad Group Theme: {self.ad_group_theme}'
        self.prompt = self.basic_prompt + "\n" + self.prompt_customizer

    def get_keywords(self):
        caller = Caller(self.prompt, KeywordList)
        caller.make_request()
        return caller.json_model()


     
