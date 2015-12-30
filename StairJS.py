import Parser
import Engine
import sys

if __name__ == '__main__':
    if len(sys.argv) == 1:
        Parser.build("Statement")
        while True:
            statement = input(">>>")
            if statement.strip() == "exit":
                break
            while True:
                line = input("...")
                if line == "":
                    break
                statement += line
            try:
                ast = Parser.yacc.parse(statement)
                if ast:
                        Engine.engine["Statement"](ast,Engine.glb)
            except Exception as e:
                for i in e.args:
                    print(i, end=" ")
                print()

    else:
        with open(sys.argv[1]) as file:
            Parser.build("Program")
            ast = Parser.yacc.parse(file.read())
            argv = Engine.StObject()
            for i in range(1, len(sys.argv)):
                argv[i-1] = sys.argv[i]
            Engine.glb["argv"] = Engine.StRef(argv)
            Engine.interpret(ast)
