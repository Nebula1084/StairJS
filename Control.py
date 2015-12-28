import Engine


def block(ast, this):
    Engine.traverse(ast, this)


def statement(ast, this):
    Engine.traverse(ast, this)


def statement_list(ast, this):
    Engine.traverse(ast, this)


def empty_statement(ast, this):
    Engine.traverse(ast, this)


def expression_no_in_statement(ast, this):
    Engine.traverse(ast, this)


def if_statement(ast, this):
    Engine.traverse(ast, this)


def iteration_statement(ast, this):
    Engine.traverse(ast, this)


def do_statement(ast, this):
    Engine.traverse(ast, this)


def while_statement(ast, this):
    Engine.traverse(ast, this)


def origin_for_statement(ast, this):
    Engine.traverse(ast, this)


def for_each_statement(ast, this):
    Engine.traverse(ast, this)


def return_statement(ast, this):
    Engine.traverse(ast, this)


def program(ast, this):
    Engine.traverse(ast, this)


def source_elements(ast, this):
    Engine.traverse(ast, this)


def source_element(ast, this):
    Engine.traverse(ast, this)
