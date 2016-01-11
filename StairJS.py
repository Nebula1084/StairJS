import Parser
import Engine
import sys

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    Parser.build("Program")
    if len(sys.argv) != 1:
        if sys.argv[1] == "-i":
            n = 2
        else:
            n = 1
        with open(sys.argv[n]) as file:
            ast = Parser.yacc.parse(file.read())
            if ast is not None:
                args = Engine.StObject()
                for i in range(n, len(sys.argv)):
                    args[i - n] = sys.argv[i]
                Engine.glb["args"] = args
                try:
                    Engine.interpret(ast)
                except Exception as e:
                    print("error: ", end="")
                    print(e)
                    sys.exit(1)

    if len(sys.argv) == 1 or sys.argv[1] == "-i":
        if len(sys.argv) == 1:
            print("""Stair JavaScript Interpreter V1.0 \n"""
                  """Powered by Li Qimai, Hai Jiewen, Chen Guangxiang, Cai Wuwei""")
        while True:
            statement = input(">>>")
            if statement.strip() == "exit":
                print("Bye!")
                break
            if statement.strip() == "":
                continue
            while True:
                line = input("...")
                if line == "":
                    break
                statement += line
            try:
                if statement != "":
                    ast = Parser.yacc.parse(statement)
                    if ast:
                        ret = Engine.interpret(ast, print_result=True)
                        if ret is not None:
                            print(ret)
            except Exception as e:
                print("error: ", end="")
                print(e)
                # for i in e.args:
                #     print(i, end=" ")
                # print()
