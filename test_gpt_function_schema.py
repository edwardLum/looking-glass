import unittest

from gpt_function_schema import Function, FunctionParameter, FunctionProperty

class TestFunctionParameter(unittest.TestCase):
    def setUp(self):
        self.function_with_one_simple_property = {
            'name': 'extract_student_info',
            'description': 'Get the student information from the body of the input text',
            'parameters': {
                'type': 'object',
                'properties': {
                    'name': {
                        'type': 'string',
                        'description': 'Name of the person'
                    },
                }
            }
        }

    def test_funtion_with_one_simple_property(self):
        func_property = FunctionProperty(name="name",
                                         type="string",
                                         description="Name of the person")

        func_parameter = FunctionParameter(properties=func_property)

        function = Function(name="extract_student_info",
                            description="Get the student information from the body of the input text",
                            parameters=func_parameter)
        function_schema= function.model_dump(exclude_none=True, by_alias=True)
        self.assertEqual(self.function_with_one_simple_property, function_schema)


if __name__ == "__main__":
    unittest.main()
