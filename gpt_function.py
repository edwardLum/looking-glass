import json

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
        return json.dumps(self.to_dict())


class FunctionParameter():
    def __init__(self, param_type, properties, required):
        self.param_type = param_type
        self.properties = properties
        self.required = required 
    

class FunctionProperty():
    _property_types= {"string", "integer", "float", "boolean"}
    
    def __init__(self, name, property_type, description=None):
        self.name = name
        self._property_type = None
        self.property_type = property_type
        self.description = description 
    
    @property
    def property_type(self):
        return self._property_type

    @property_type.setter
    def property_type(self, value):
        if value not in self._property_types:
            raise ValueError(f"Invalid color. Permitted colors are: {', '.join(self._property_types)}")
        self._property_type = value

    def to_dict(self):
        return {
                self.name: {
                    "type": self.property_type,
                    "description": self.description
                    }
        }

        
