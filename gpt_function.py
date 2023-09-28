


class FunctionParameter():
    def __init__(self, param_type, properties, required):
        self.param_type = param_type
        self.properties = properties
        self.required = required 
        self.json = self.create_json()
    
    def create_json(self):
        pass

class FunctionProperty():
    __property_types= {"string", "integer", "float", "boolean"}
    
    def __init__(self, _property_name, _property_type, _property_description=None):
        self._property_name = _property_name
        self.__property_type = None
        self._property_type = _property_type
        self._property_description = _property_description
        self.json = self.create_json()
    
    @property
    def _property_type(self):
        return self.__property_type

    @_property_type.setter
    def _property_type(self, value):
        if value not in self.__property_types:
            raise ValueError(f"Invalid color. Permitted colors are: {', '.join(self.__property_types)}")
        self.__property_type = value

    def create_json(self):
        pass
        
