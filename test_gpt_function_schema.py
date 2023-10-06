import unittest

from gpt_function_schema import Function, FunctionParameter, FunctionProperties, FunctionProperty, FunctionProperties

class TestFunctionProperty(unittest.TestCase):
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

#
#class TestFunctionParameter(unittest.TestCase):
#    def setUp(self):
#        self.function_with_one_simple_property = {
#            'name': 'extract_student_info',
#            'description': 'Get the student information from the body of the input text',
#            'parameters': {
#                'type': 'object',
#                'properties': {
#                    'name': {
#                        'type': 'string',
#                        'description': 'Name of the person'
#                    },
#                }
#            }
#        }
#
#        self.function_with_many_simple_properties =  {
#            'name': 'extract_student_info',
#            'description': 'Get the student information from the body of the input text',
#            'parameters': {
#                'type': 'object',
#                'properties': {
#                    'name': {
#                        'type': 'string',
#                        'description': 'Name of the person'
#                    },
#                    'major': {
#                        'type': 'string',
#                        'description': 'Major subject.'
#                    },
#                    'school': {
#                        'type': 'string',
#                        'description': 'The university name.'
#                    },
#                    'grades': {
#                        'type': 'integer',
#                        'description': 'GPA of the student.'
#                    },
#                    'club': {
#                        'type': 'string',
#                        'description': 'School club for extracurricular activities. '
#                    }
#                    
#                }
#            }
#        }
#
#    def test_funtion_with_one_simple_property(self):
#        func_property = FunctionProperty(name="name",
#                                         type="string",
#                                         description="Name of the person")
#
#        func_properties = FunctionProperties(properties=[func_property])
#        func_parameter = FunctionParameter(properties=(func_properties)
#
#        function = Function(name="extract_student_info",
#                            description="Get the student information from the body of the input text",
#                            parameters=func_parameter)
#        function_schema= function.model_dump(exclude_none=True, by_alias=True)
#        self.assertEqual(self.function_with_one_simple_property, function_schema)
#
#    def test_funtion_with_many_simple_properties(self):
#        name_property = FunctionProperty(name="name",
#                                         type="string",
#                                         description="Name of the person")
#
#        major_property = FunctionProperty(name="major",
#                                         type="string",
#                                         description="Major subject.")
#
#        func_parameter = FunctionParameter(properties=[name_property, major_property])
#
#        function = Function(name="extract_student_info",
#                            description="Get the student information from the body of the input text",
#                            parameters=func_parameter)
#        function_schema= function.model_dump(exclude_none=True, by_alias=True)
#        print(function_schema)
#        self.assertEqual(self.function_with_one_simple_property, function_schema)

if __name__ == "__main__":
    unittest.main()
