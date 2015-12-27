import Parser

if __name__ == '__main__':
    with open("HelloWorld.js") as file:
        ast = Parser.yacc.parse(file.read())
        Parser.printAST(list(ast), 0)
