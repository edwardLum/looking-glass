
class FunctionParameter():
    _parameter_types= {"string", "integer", "float", "boolean"}
    
    def __init__(self, parameter_name, parameter_type, parameter_description=None):
        self.parameter_name = parameter_name
        self._parameter_type = None
        self.parameter_type = parameter_type
        self.parameter_description = parameter_description
    
    @property
    def parameter_type(self):
        return self._parameter_type

    @parameter_type.setter
    def parameter_type(self, value):
        if value not in self._parameter_types:
            raise ValueError(f"Invalid color. Permitted colors are: {', '.join(self._parameter_types)}")
        self._parameter_type = value

    def create_property(self):
        pass
