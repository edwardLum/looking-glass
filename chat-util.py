
class FunctionArgument():
    _argument_types= {"string", "integer", "float", "boolean"}
    
    def __init__(self, argument_name, argument_type, argument_description=None):
        self.argument_name = argument_name
        self._argument_type = None
        self.argument_type = argument_type
        self.argument_description = argument_description
    
    @property
    def argument_type(self):
        return self._argument_type

    @argument_type.setter
    def argument_type(self, value):
        if value not in self._argument_types:
            raise ValueError(f"Invalid color. Permitted colors are: {', '.join(self._argument_types)}")
        self._argument_type = value

    def create_property(self):
        pass
