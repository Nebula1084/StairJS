class Object(object):
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOL = "bool"
    FUNCPROTO = "funcproto"
    OBJECT = "object"
    FUNCTION = "function"

    def __init__(self):
        self.fields = {}


class StPrimitive(Object):
    def __init__(self, _type_, _value_):
        super(StPrimitive, self).__init__()
        self.fields["_type_"] = _type_
        self.fields["_value_"] = _value_


class StInt(StPrimitive):
    def __init__(self, _value_):
        super(StInt, self).__init__(Object.INT, _value_)


class StFloat(StPrimitive):
    def __init__(self, _value_):
        super(StFloat, self).__init__(Object.FLOAT, _value_)


class StString(StPrimitive):
    def __init__(self, _value_):
        super(StString, self).__init__(Object.STRING, _value_)


class StBool(StPrimitive):
    def __init__(self, _value_):
        super(StBool, self).__init__(Object.BOOL, _value_)


class StFuncProto(Object):
    def __init__(self):
        super(StFuncProto, self).__init__()
        self.fields["_type_"] = Object.FUNCPROTO


class StFunction(Object):
    def __init__(self):
        super(StFunction, self).__init__()
        self.fields["_type_"] = Object.FUNCTION


class StObject(Object):
    def __init__(self):
        super(StObject, self).__init__()
        self.fields["_type_"] = Object.OBJECT
