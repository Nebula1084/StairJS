import Engine
from Object import *
from NonTerminal import *


def primary_expression(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def identifier(ast, context):
    return context[ast[1]]


def array_literal(ast, context):
    for x in Engine.iterate(ast, context):
        return x


def element_list(ast, context):
    ret = []
    for x in Engine.iterate(ast, context):
        ret.append(x)
    return ret


def element_list_end_with_ex(ast, context):
    Engine.traverse(ast, context)


def object_literal(ast, context):
    Engine.traverse(ast, context)


def property_name_and_value_list(ast, context):
    Engine.traverse(ast, context)


def property_name_and_value(ast, context):
    Engine.traverse(ast, context)


def property_name(ast, context):
    Engine.traverse(ast, context)


def member_expression(ast, context):
    mem = Engine.engine[ast[1][0]](ast[1], context)
    return mem


def allocation_expression(ast, context):
    Engine.traverse(ast, context)


def member_expression_part(ast, context):
    Engine.traverse(ast, context)


def call_expression(ast, context):
    func_proto = Engine.engine[ast[1][0]](ast, context)
    new_context = {"this": context}
    print ast
    print func_proto[1]["code"]


def call_expression_part(ast, context):
    Engine.traverse(ast, context)


def arguments(ast, context):
    Engine.traverse(ast, context)


def argument_list(ast, context):
    Engine.traverse(ast, context)


def right_hand_side_expression(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def left_hand_side_expression(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def assignment_expression_no_in(ast, context):
    if len(ast) > 2:
        left = Engine.engine[ast[1][0]](ast[1], context)
        right = Engine.engine[ast[3][0]](ast[3], context)
        if isinstance(right, list):
            left[1] = right[1]
        else:
            left[1] = right
        return left[1]
    else:
        return Engine.engine[ast[1][0]](ast[1], context)


def assignment_operator(ast, context):
    Engine.traverse(ast, context)


def expression_no_in(ast, context):
    Engine.traverse(ast, context)


def function_declaration(ast, context):
    Engine.traverse(ast, context)


def function_expression(ast, context):
    return {"type": FUNCPROTO, "code": ast}


def formal_parameter_list(ast, context):
    Engine.traverse(ast, context)


def more_formal_parameter(ast, context):
    Engine.traverse(ast, context)


def function_body(ast, context):
    Engine.traverse(ast, context)


def variable_statement(ast, context):
    var = ast[2][1]
    if len(ast) <= 4:
        context[var] = ["left", UNDEFINED]
    else:
        context[var] = ["left", assignment_expression_no_in(ast[4], context)]
