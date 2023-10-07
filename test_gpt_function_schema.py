from os import walk
import unittest

from gpt_function_schema import Function, FunctionParameter, FunctionProperties, FunctionProperty, FunctionProperties

class TestDictSerialization(unittest.TestCase):
    def setUp(self):
        self.func_property_string = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                    }
                }

        self.func_property_integer = {
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                    }
                }

        self.func_properties = {
                'name': {
                    'type': 'string',
                    'description': 'Name of the person.'
                },
                'grades': {
                    'type': 'integer',
                    'description': 'GPA of the student.'
                }
            }

        self.func_parameter = {
            'type': 'object',
            'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the person.'
                    },
                    'grades': {
                        'type': 'integer',
                        'description': 'GPA of the student.'
                    },
                }
            }

    def test_property_dict_serialization_string(self):
        name_property_string = FunctionProperty(name="name", 
                                         type="string",
                                         description='Name of the person.')
        
        grades_property_string = FunctionProperty(name="grades", 
                                         type="integer",
                                         description='GPA of the student.')

        self.assertEqual(self.func_property_string, 
                         name_property_string.model_dump(exclude_none=True))

        self.assertEqual(self.func_property_integer, 
                         grades_property_string.model_dump(exclude_none=True))
    
    def test_properties_dict_serialization(self):
        name_property_string = FunctionProperty(name="name", 
                                         type="string",
                                         description='Name of the person.')
        
        grades_property_string = FunctionProperty(name="grades", 
                                         type="integer",
                                         description='GPA of the student.')

        properties = FunctionProperties(properties=[name_property_string, 
                                        grades_property_string])

        self.assertEqual(self.func_properties, 
                         properties.model_dump(exclude_none=True))

    def test_parameter_dict_serialization(self):
        name_property_string = FunctionProperty(name="name", 
                                         type="string",
                                         description='Name of the person.')
        
        grades_property_string = FunctionProperty(name="grades", 
                                         type="integer",
                                         description='GPA of the student.')

        properties = FunctionProperties(properties=[name_property_string, 
                                        grades_property_string])

        parameter = FunctionParameter(properties=properties)
        
        self.assertEqual(self.func_parameter, 
                         parameter.model_dump(exclude_none=True))



if __name__ == "__main__":
    unittest.main()
