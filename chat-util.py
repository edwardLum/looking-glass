class JSONCreator:

    def create_property(self,
                                 property_name,
                                 property_type,
                                 item_type=None,
                                 item_description=None,
                                 property_description=None):
        property_data = {
            "type": property_type
        }

        if item_type and item_description:
            property_data["items"] = {
                "type": item_type,
                "description": item_description
            }

        if property_description:
            property_data["description"] = property_description

        return {
            property_name: property_data
        }

    def create_json_object(self,
                           name,
                           description,
                           parameter_type,
                           property_name,
                           property_type,
                           item_type,
                           item_description,
                           property_description,
                           required_list):
        
        properties = self.create_properties_object(
            property_name,
            property_type,
            item_type,
            item_description,
            property_description
        )

        return {
            "name": name,
            "description": description,
            "parameters": {
                "type": parameter_type,
                "properties": properties,
                "required": required_list
            }
        }

# Test
json_creator = JSONCreator()
print(
    json_creator.create_json_object(
        name="get_keywords",
        description="Get a list of Google Ads keywords",
        parameter_type="object",
        property_name="some_property",
        property_type="array",
        item_type="string",
        item_description="Some description",
        property_description="Another description",
        required_list=["some_property"]
    )
)

