import os
import json

import openai

from app.services.function_schema import Function, ArrayProperty, StringItem, StringProperty, ObjectItem

def campaign_structure_suggestion(business_category):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    prompt_input =  f"""Hello! Please recommend a campaign structure for a Google Search Ads account.
                       Provide a tree structure of campaigns and ad groups. Campaigns should be thematically separated and group relevant ad groups together.
                       Name campaigns and ad groups according to their theme. Do not limit yourself on the number of campaigns and ad groups you are going to recommend.
                       I would like to have a minimum of 5 campaigns with 10 a groups each. Campaign and ad groups names should only inlcude the actual campaign name,
                       without any additions like "Cammpaign #1", "Campaign -" etc.
                       Please include a separate note with the rational behind your choices.
                       The business category of the account is {business_category}. """

    # Hardcoding function creation temporarily

    rational = StringProperty(name="rational",
                              description="The rational behind the campaign structure recommendation")
    campaign_name = StringProperty(name="campaing_name",
                                   description="The name of the campaign")

    ad_group_name = StringProperty(name="ad_group_name",
                                   description="The name of the ad group")

    ad_group = ObjectItem(name="ad_group",
                          description="A Google Ads ad group",
                          properties=[ad_group_name])

    ad_groups = ArrayProperty(name="ad_groups",
                              description="A list of Google Ads ad groups",
                              items=ad_group
    )

    campaign = ObjectItem(name="campaign",
                          description="A Google Ads campaign",
                          properties=[campaign_name,ad_groups])

    campaigns = ArrayProperty(name="campaigns",
                                 description='A list of Google Ads campaigns',
                                 items=campaign)

    function = Function(name="get_campaign_structure",
                        description="Get a list of Google Ads campaigns with associated ad groups and a rational expaining the choices.",
                        properties = [campaigns, rational]).model_dump()


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {
                "role": "user",
                "content": prompt_input,
            }
        ],
        functions=[function],
        function_call={"name": "get_campaign_structure"})

    reply_content = completion.choices[0].message
    keywords = reply_content.to_dict()['function_call']['arguments']
    return json.loads(keywords)
