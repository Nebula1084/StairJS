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
        if len(self) > 0:
            ret += "\n"
        for k, v in self.items():
            ret += "    " + k.__repr__() + ":" + v.__repr__() + ",\n"
        return ret + "}"


# class StRef(object):
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __str__(self):
#         return self.obj.__str__()


class Undefined(object):
    def __init__(self):
        pass

    def __str__(self):
        return "undefined"

    def __repr__(self):
        return self.__str__()


class StNull:
    def __init__(self):
        pass

    def __str__(self):
        return "null"

    def __repr__(self):
        return self.__str__()


UNDEFINED = Undefined()
NULL = StNull()


class StFunction(StObject):
    def __init__(self):
        super(StFunction, self).__init__()
        self.name = ""
        self.ast = None  # function expression
        self.argument_list = []
        self.outFunction = None

    def __str__(self):
        ret = "function " + self.name
        ret += "("
        if len(self.argument_list) > 0:
            ret += self.argument_list[0]
            for i in range(1, len(self.argument_list)):
                ret += ", " + self.argument_list[i]
        ret += ")"
        ret += StFunction.code(self.ast)
        return ret

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def code(code):
        if not isinstance(code, list):
            return code.__str__()
        ret = ""
        if len(code) == 2:
            return StFunction.code(code[1])
        else:
            for i in range(1, len(code)):
                child = StFunction.code(code[i])
                ret += child
                if i != len(code) - 1:
                    ret += " "
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
