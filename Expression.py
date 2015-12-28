import Engine
from Object import *


def primary_expression(ast, this):
    print ast
    for x in Engine.iterate(ast, this):
        print "primary_expression:", x
        return x


def identifier(ast, this):
    return ast[1]


def array_literal(ast, this):
    for x in Engine.iterate(ast, this):
        print x
        return x


def element_list(ast, this):
    ret = []
    for x in Engine.iterate(ast, this):
        ret.append(x)
    return ret


def element_list_end_with_ex(ast, this):
    Engine.traverse(ast, this)


def object_literal(ast, this):
    Engine.traverse(ast, this)


def property_name_and_value_list(ast, this):
    Engine.traverse(ast, this)


def property_name_and_value(ast, this):
    Engine.traverse(ast, this)


def property_name(ast, this):
    Engine.traverse(ast, this)


def member_expression(ast, this):
    Engine.traverse(ast, this)


def allocation_expression(ast, this):
    Engine.traverse(ast, this)


def member_expression_part(ast, this):
    Engine.traverse(ast, this)


def call_expression(ast, this):
    Engine.traverse(ast, this)


def call_expression_part(ast, this):
    Engine.traverse(ast, this)


def arguments(ast, this):
    Engine.traverse(ast, this)


def argument_list(ast, this):
    Engine.traverse(ast, this)


def left_hand_side_expression(ast, this):
    Engine.traverse(ast, this)


def postfix_expression(ast, this):
    Engine.traverse(ast, this)


def postfix_operator(ast, this):
    Engine.traverse(ast, this)


def assignment_expression_no_in(ast, this):
    Engine.traverse(ast, this)
    return 1


def assignment_operator(ast, this):
    Engine.traverse(ast, this)


def expression_no_in(ast, this):
    Engine.traverse(ast, this)


def function_declaration(ast, this):
    Engine.traverse(ast, this)


def function_expression(ast, this):
    Engine.traverse(ast, this)


def formal_parameter_list(ast, this):
    Engine.traverse(ast, this)


def more_formal_parameter(ast, this):
    Engine.traverse(ast, this)


def function_body(ast, this):
    Engine.traverse(ast, this)


def variable_statement(ast, this):
    this[identifier(ast[2], this)] = UNDEFINED
