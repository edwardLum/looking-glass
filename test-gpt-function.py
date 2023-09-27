import unittest

from gpt_function import FunctionParameter


class TestFunctionParameter(unittest.TestCase):

    def test_successful_instantiation(self):
        arg = FunctionParameter("arg1", "string", "A string parameter")
        self.assertEqual(arg.parameter_name, "arg1")
        self.assertEqual(arg.parameter_type, "string")
        self.assertEqual(arg.parameter_description, "A string parameter")

    def test_invalid_parameter_type(self):
        with self.assertRaises(ValueError):
            FunctionParameter("arg1", "invalid_type")

    def test_parameter_type_property(self):
        arg = FunctionParameter("arg1", "integer")
        self.assertEqual(arg.parameter_type, "integer")

        # Now, try to set to an invalid type and check for exception
        with self.assertRaises(ValueError):
            arg.parameter_type = "invalid_type"

        # Ensure the original value hasn't changed after attempting to set an invalid value
        self.assertEqual(arg.parameter_type, "integer")

if __name__ == "__main__":
    unittest.main()
