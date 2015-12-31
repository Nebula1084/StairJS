from NonTerminal import *
from Object import *


def statement_list(ast, context):
    for i in range(1, len(ast)):
        ret = statement(ast[i], context)
        if context.return_value is not None:
            break
    return ret


from Expression import expression_no_in, variable_statement

controlEngine = None


def statement(ast, context):
    return controlEngine[ast[1][0]](ast[1], context)


def block(ast, context):
    if len(ast) == 4:
        statement_list(ast[2], context)


def empty_statement(ast, context):
    pass


def expression_no_in_statement(ast, context):
    return expression_no_in(ast[1], context)


def if_statement(ast, context):
    if expression_no_in(ast[2], context):
        statement(ast[5], context)
    else:
        if len(ast) == 8:
            statement(ast[7], context)


def iteration_statement(ast, context):
    controlEngine[ast[1][0]](ast[1], context)


def do_statement(ast, context):
    while True:
        statement(ast[2], context)
        if context.return_value is not None:
            break
        if not expression_no_in(ast[4], context):
            break;


def while_statement(ast, context):
    while expression_no_in(ast[3], context):
        statement(ast[5], context)
        if context.return_value is not None:
            break


def origin_for_statement(ast, context):
    expression_no_in(ast[3], context)
    while expression_no_in(ast[5], context):
        statement(ast[9], context)
        if context.return_value is not None:
            break
        expression_no_in(ast[7], context)


def for_each_statement(ast, context):
    for context[ast[4][1]] in expression_no_in(ast[6], context):
        statement(ast[8], context)
        if context.return_value is not None:
            break


def return_statement(ast, context):
    if ast[len(ast) - 1] == ";":
        ast.pop()
    if len(ast) == 2:
        context.return_value = UNDEFINED
    elif len(ast) == 3:
        context.return_value = expression_no_in(ast[2], context)


def print_statement(ast, context):
    print(expression_no_in(ast[2], context))


def program(ast, context):
    return statement_list(ast[1], context)


# def source_elements(ast, context):
#     for i in range(1, len(ast)):
#         source_element(ast[i], context)


# def source_element(ast, context):
#     statement(ast[1], context)


controlEngine = {
    Block: block,
    VariableStatement: variable_statement,
    EmptyStatement: empty_statement,
    ExpressionNoInStatement: expression_no_in_statement,
    IfStatement: if_statement,
    IterationStatement: iteration_statement,
    DoStatement: do_statement,
    WhileStatement: while_statement,
    OriginForStatement: origin_for_statement,
    ForEachStatement: for_each_statement,
    ReturnStatement: return_statement,
    PrintStatement: print_statement
}


def main():
    pass


if __name__ == '__main__':
    main()
