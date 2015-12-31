INT = "int"
FLOAT = "float"
STRING = "string"
BOOL = "bool"
FUNCPROTO = "funcproto"
OBJECT = "object"
FUNCTION = "function"


class StObject(dict):
    def __init__(self):
        super(StObject, self).__init__()

    def __str__(self):
        ret = "{"
        for k, v in self.items():
            ret = ret + k.__str__() + ":" + v.__str__() + ","
        return ret[:-1] + "}"


class StRef(object):
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return self.obj.__str__()


class Undefined(object):
    def __init__(self):
        pass

    def __str__(self):
        return "undefined"


class StNull:
    def __init__(self):
        pass

    def __str__(self):
        return "null"

UNDEFINED = Undefined()
NULL = StNull()


class StFunction(StObject):
    def __init__(self):
        super(StFunction, self).__init__()
        self.ast = None  # function expression
        self.argument_list = []

    def __str__(self):
        return StFunction.code(self.ast)

    @staticmethod
    def code(code):
        if not isinstance(code, list):
            return code.__str__()
        ret = str()
        for i in range(1, len(code)):
            ret += StFunction.code(code[i])
        return ret


class StActiveRecord(dict):
    def __init__(self):
        super(StActiveRecord, self).__init__()
        self.return_value = None
        self.this = None
        self.outFunction = None
        pass

    def __str__(self):
        ret = "{"
        for k, v in self.items():
            ret = ret + k.__str__() + ":" + v.__str__() + ","
        return ret[:-1] + "}"
