INT = "int"
FLOAT = "float"
STRING = "string"
BOOL = "bool"
FUNCPROTO = "funcproto"
OBJECT = "object"
FUNCTION = "function"
NULL = {"type": OBJECT, "value": "null"}
UNDEFINED = {"type": "undefined"}


class StObject(dict):
    def __init__(self):
        super(StObject, self).__init__()


class StFunction(StObject):
    def __init__(self):
        super(StFunction, self).__init__()
        self.ast = None  # function expression


class StActiveRecord(dict):
    def __init__(self):
        super(StActiveRecord, self).__init__()
        self.return_value = None
        self.this = None
        self.outFunction = None
        pass
