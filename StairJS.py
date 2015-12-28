import Parser
import Engine

if __name__ == '__main__':
    with open("HelloWorld.js") as file:
        ast = Parser.yacc.parse(file.read())
        Engine.interpret(ast)
