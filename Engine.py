from Ast import StAst


class Engine(object):
    def __init__(self):
        pass

    def interpret(self, ast):
        if ast.name == StAst.FunctionDeclaration:
            pass
        for child in ast.childs:
            self.interpret(child)
