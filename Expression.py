from NonTerminal import *
from Object import *
import Engine


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
    arguments_list = arguments(ast[2], context)
    new_ar = StActiveRecord()
    new_ar.this = context
    new_ar["arugments"] = arguments_list

    code = func_proto[0].ast
    formal_list = func_proto[0].argument_list
    for i in range(0, len(formal_list)):
        if i in arguments_list:
            new_ar[formal_list[i]] = arguments_list[i]
        else:
            new_ar[formal_list[i]] = Undefined()
    func_body = None
    for x in code:
        if isinstance(x, list) and x[0] == FunctionBody:
            func_body = x
            break
    function_body(func_body, new_ar)


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
            left[0] = right[0]
        else:
            left[0] = right
        return left[0]
    else:
        return Engine.engine[ast[1][0]](ast[1], context)


def assignment_operator(ast, context):
    Engine.traverse(ast, context)


def expression_no_in(ast, context):
    return assignment_expression_no_in(ast[1], context)


def function_declaration(ast, context):
    Engine.traverse(ast, context)


def function_expression(ast, context):
    func_proto = StFunction()
    func_proto.ast = ast
    for fpl in ast:
        if isinstance(fpl, list) and fpl[0] == Identifier:
            context[fpl[1]] = func_proto
        if isinstance(fpl, list) and fpl[0] == FormalParameterList:
            func_proto.argument_list = formal_parameter_list(fpl, context)
    return func_proto


def formal_parameter_list(ast, context):
    ret = []
    for x in ast:
        if isinstance(x, list):
            ret.append(x[1])
    return ret


def more_formal_parameter(ast, context):
    Engine.traverse(ast, context)


from Control import statement_list


def function_body(ast, context):
    ret = statement_list(ast[2], context)
    return context.return_value


def variable_statement(ast, context):
    var = ast[2][1]
    if len(ast) <= 4:
        context[var] = [UNDEFINED]
    else:
        context[var] = [assignment_expression_no_in(ast[4], context)]
