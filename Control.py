from Engine import *


def block(ast, context):
    if len(ast) == 3:
        statement_list(ast[2],context)


def statement(ast, context):
    Engine.eigen[ast[1][0]](ast[1],context)


def statement_list(ast, context):
    for i in range(1:len(ast)):
        if return_value != None:
            break
        statement(ast[i],context)
    


def empty_statement(ast, context):
    pass


def expression_no_in_statement(ast, context):
    expression_no_in(ast[1],context)


def if_statement(ast, context):
    if expression_no_in(ast[2],context):
        statement(ast[5],context)
    else:
        if len(ast) == 8:
            statement(ast[7],context)


def iteration_statement(ast, context):
    Engine.eigen[ast[1][0]](ast[1],context)


def do_statement(ast, context):
    while True:
        statement(ast[2],context)
        if context.return_value != None:
            break
        if not expression_no_in(ast[4],context):
            break;


def while_statement(ast, context):
    while expression_no_in(ast[3],context):
        statement(ast[5],context)
        if context.return_value != None:
            break


def origin_for_statement(ast, context):
    expression_no_in(ast[3],context)
    while expression_no_in(ast[5],context):
        statement(ast[9],context)
        if context.return_value != None:
            break
        expression_no_in(ast[7],context)


def for_each_statement(ast, context):
    for context[ast[4][1]] in expression_no_in(ast[6],context):
        statement(ast[8],context)
        if context.return_value != None:
            break
    


def return_statement(ast, context):
    if ast[len(ast)-1] == ";":
        ast.pop()
    if len(ast) == 2:
        context.return_value = UNDEFINED
    elif len(ast) == 3:
        context.return_value = expression_no_in(ast[2],context)

def print_statement():
    print(expression_no_in(ast[2]))

def program(ast, context):
    source_elements(ast[1],context)


def source_elements(ast, context):
    for i in range(1:len(ast)):
        source_element(ast[i],context)

def source_element(ast, context):
    statement(ast[1],context)

def main():
    pass

if __name__ == '__main__':
    main()