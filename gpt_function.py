import json
import os

import openai

class Function():
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters.to_dict()
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)  # Added indent for better formatting

class FunctionParameter():
    def __init__(self, required, param_type="object", properties=None):
        self.param_type = param_type
        self.properties = properties if properties is not None else []
        self.required = required  

    def to_dict(self):
        properties_dict = {prop.name: prop.to_dict() for prop in self.properties}

        return {
            "type": self.param_type,
            "properties": properties_dict,
            "required": self.required
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)  # Added indent for better formatting

class FunctionProperty():
    _property_types = {"string", "integer", "float", "boolean", "object", "array"}
    
    def __init__(self, name, property_type, description=None, items=None, properties=None):
        self.name = name
        self._property_type = None
        self.property_type = property_type
        self.description = description
        self.items = items  # Used for arrays
        self.properties = properties  # Used for nested objects

    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        if value not in self._property_types:
            raise ValueError(f"Invalid type. Permitted types are: {', '.join(self._property_types)}")
        self._property_type = value

    def to_dict(self):
        prop_dict = {
            "type": self.property_type,
            "description": self.description
        }
        if self.property_type == "array" and self.items:
            prop_dict["items"] = self.items.to_dict()
        if self.property_type == "object" and self.properties:
            prop_dict["properties"] = {prop.name: prop.to_dict() for prop in self.properties}
        return prop_dict

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)  # Added indent for better formatting

if __name__=="__main__":
        # Usage:

# Define a simple property
    keyword_property = FunctionProperty("keyword", "string", "A keyword.")

# Define a property that is an array of the above simple property
    keywords_array_property = FunctionProperty("keywords", "array", "The list of keywords.", items=keyword_property)

# Define a property that is an object containing the above array property
    ad_group_property = FunctionProperty("ad_group", "object", properties=[keywords_array_property])

# Define a property that is an array of the above object property
    ad_groups_array_property = FunctionProperty("ad_groups", "array", "The list of ad groups.", items=ad_group_property)

# Define the function parameter using the above array property
    function_param = FunctionParameter(["ad_groups"], properties=[ad_groups_array_property])

# Define the function using the above function parameter
    get_ad_groups_function = Function(name="get_ad_groups", description="Gets a list of ad groups and associated keywords", parameters=function_param)
    
    func_json = get_ad_groups_function.to_json()
    print(func_json)

   # openai.api_key = os.getenv("OPENAI_API_KEY")

   # example_input = "Recommend 5 ad groups with 10 keywords each, for a Google Ads campaign. The campaign theme is {}.".format("computer games")

#    completion = openai.ChatCompletion.create(
#        model="gpt-3.5-turbo-0613",
#        messages=[
#            {
#                "role": "user",
#                "content": example_input,
#            }
#        ],
#        functions=[func_json],

#        function_call={"name": "get_ad_groups"}
#    )
#
    #reply_content = completion.choices[0].message
    #ad_groups = reply_content.to_dict()['function_call']['arguments']
    #print(json.loads(ad_groups))
        
