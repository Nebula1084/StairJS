import Engine
from Object import *
from Control import *
from NonTerminal import *


def primary_expression(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def identifier(ast, context):
    return context[ast[1]]


def array_literal(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def element_list(ast, context):
    ret = {}
    i = 0
    for x in Engine.iterate(ast, context):
        ret[i] = x
        i += 1
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
    func_proto = Engine.engine[ast[1][0]](ast[1], context)
    arguments_list = Engine.engine[ast[2][0]](ast[2], context)
    new_ar = StActiveRecord()
    new_ar.this = context
    new_ar["arugments"] = arguments_list

    code = func_proto[1]["code"]
    formal_list = formal_parameter_list(code[3], context)
    for i in range(0, len(formal_list)):
        if i in arguments_list:
            new_ar[formal_list[i]] = arguments_list[i]
        else:
            new_ar[formal_list[i]] = UNDEFINED
    print new_ar
    print code


def call_expression_part(ast, context):
    Engine.traverse(ast, context)


def arguments(ast, context):
    if len(ast) == 3:
        return {}
    else:
        return argument_list(ast[2], context)


def argument_list(ast, context):
    ret = {}
    i = 0
    for x, y in Engine.iterate(ast, context):
        ret[i] = x
        i += 1
    return ret


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
    ret = []
    for x in ast:
        if isinstance(x, list):
            ret.append(x[1])
    return ret


def more_formal_parameter(ast, context):
    Engine.traverse(ast, context)


def function_body(ast, context):
    return statement_list(ast, context)


def variable_statement(ast, context):
    var = ast[2][1]
    if len(ast) <= 4:
        context[var] = ["left", UNDEFINED]
    else:
        context[var] = ["left", assignment_expression_no_in(ast[4], context)]
