import os
import json

import openai

from app.services.function_schema import Function, ArrayProperty, StringItem

def keyword_suggestion(ad_group_theme, number_of_keywords):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    example_input = "Provide a recommendation of {} Google Ads keywords, that will be used in the context of an Ad Group within a Google Ads campaign. The Ad Group theme is {}.".format(number_of_keywords, ad_group_theme)

    # Hardcoding function creation temporarily

    keyword = StringItem(description="A Google Ads keyword")
    keywords = ArrayProperty(name="keywords",
                                 description='A list of Google Ads keywords',
                                 items=keyword)

    function = Function(name="get_keywords",
                        description="Get Google Ads keywords to be used in Google Ads campaigns",
                        properties = [keywords]).model_dump()


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user",
                "content": example_input,
            }
        ],
        functions=[function],
        function_call={"name": "get_keywords"})

    reply_content = completion.choices[0].message
    keywords = reply_content.to_dict()['function_call']['arguments']
    return json.loads(keywords)
