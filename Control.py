import Engine


def block(ast, context):
    Engine.traverse(ast, context)


def statement(ast, context):
    Engine.traverse(ast, context)


def statement_list(ast, context):
    Engine.traverse(ast, context)


def empty_statement(ast, context):
    Engine.traverse(ast, context)


def expression_no_in_statement(ast, context):
    Engine.traverse(ast, context)


def if_statement(ast, context):
    Engine.traverse(ast, context)


def iteration_statement(ast, context):
    Engine.traverse(ast, context)


def do_statement(ast, context):
    Engine.traverse(ast, context)


def while_statement(ast, context):
    Engine.traverse(ast, context)


def origin_for_statement(ast, context):
    Engine.traverse(ast, context)


def for_each_statement(ast, context):
    Engine.traverse(ast, context)


def return_statement(ast, context):
    Engine.traverse(ast, context)


def program(ast, context):
    Engine.traverse(ast, context)


def source_elements(ast, context):
    Engine.traverse(ast, context)


def source_element(ast, context):
    Engine.traverse(ast, context)
