from NonTerminal import *
from Object import *
import Engine
from Control import statement_list


def primary_expression(ast, active_record):
    if len(ast) == 2:
        if ast[1] == "this":
            return None, active_record.this
        else:
            return Engine.engine[ast[1][0]](ast[1], active_record)
    else:
        return None, expression_no_in(ast[2], active_record)
        # pe = ast[1]
        # if isinstance(pe, list):
        #     return Engine.engine[pe[0]](pe, active_record)
        # else:
        #     return active_record.this


def identifier(ast, active_record):
    def find_identifier(identifier, active_record):
        if active_record is None:
            return Engine.glb, identifier
        if identifier in active_record:
            return active_record, identifier
        else:
            return find_identifier(identifier, active_record.outFunction)
    return find_identifier(ast[1], active_record)


def array_literal(ast, active_record):
    obj = StObject()
    element_list(ast[2], active_record, obj)
    return None, obj


def element_list(ast, active_record, obj):
    i = 0
    for child in ast:
        if isinstance(child, list) and child[0] == AssignmentExpressionNoIn:
            obj[i] = assignment_expression_no_in(child, active_record)
        elif child == ',':
            i += 1


def object_literal(ast, active_record):
    obj = StObject()
    if len(ast) == 4:
        property_name_and_value_list(ast[2], active_record, obj)
    return None, obj


def property_name_and_value_list(ast, active_record, obj):
    for child in ast:
        if isinstance(child, list) and child[0] == PropertyNameAndValue:
            property_name_and_value(child, active_record, obj)


def property_name_and_value(ast, active_record, obj):
    obj[property_name(ast[1], active_record)] = assignment_expression_no_in(ast[3], active_record)


def property_name(ast, active_record):
    if isinstance(ast[1], list):
        return ast[1][1]
    else:
        return ast[1]


def member_expression(ast, active_record):
    if len(ast) == 3:
        owner_of_owner, key = member_expression(ast[1], active_record)
        if isinstance(owner_of_owner, dict):
            owner = owner_of_owner[key]
        else:
            owner = key
        return member_expression_part(ast[2], active_record, owner)
    else:
        return Engine.engine[ast[1][0]](ast[1], active_record)


def allocation_expression(ast, active_record):
    obj = StObject()
    owner, key = member_expression(ast[2], active_record)
    if owner is None:
        constructor = key
    else:
        constructor = owner[key]
    if not isinstance(constructor, StFunction):
        raise Exception(constructor + " is not callable.")
    new_ar = StActiveRecord()
    new_ar.this = obj
    new_ar.outFunction = constructor.outFunction
    arguments(ast[2], active_record, new_ar, constructor.argument_list)
    return None, function_body(constructor.ast, new_ar)


def member_expression_part(ast, active_record, owner):
    if isinstance(owner, dict):
        if ast[1] == ".":
            key = ast[2][1]
        else:
            key = expression_no_in(ast[2], active_record)
            if not (isinstance(key, str) or isinstance(key, int) or isinstance(key, float)):
                raise Exception("Only number or string can be a key")
        return owner, key
    else:
        raise Exception(str(owner) + " has no member.")


def call_expression(ast, active_record):
    if ast[2][0] == Arguments:
        owner, key = Engine.engine[ast[1][0]](ast[1], active_record)
        if owner is None:
            function = key
        elif key in owner:
            function = owner[key]
        else:
            raise Exception("'" + key + "' is not defined.")
        if not isinstance(function, StFunction):
            raise Exception(str(function) + " is not callable.")
        new_ar = StActiveRecord()
        new_ar.this = active_record.this
        new_ar.outFunction = function.outFunction
        arguments(ast[2], active_record, new_ar, function.argument_list)
        return None, function_body(function.ast, new_ar)
    else:
        owner, ret = call_expression(ast[1], active_record)
        return member_expression_part(ast[2], active_record, ret)

#
# def call_expression_part(ast, active_record):
#     Engine.traverse(ast, active_record)


def arguments(ast, active_record, new_ar, argument_names):
    if len(ast) == 3:
        new_ar["arguments"] = StObject()
    else:
        argument_list(ast[2], active_record, new_ar, argument_names)


def argument_list(ast, active_record, new_ar, argument_names):
    arguments_value = StObject()
    i = 0
    for child in ast:
        if isinstance(child, list) and child[0] == AssignmentExpressionNoIn:
            arg = assignment_expression_no_in(child, active_record)
            arguments_value[i] = arg
            if i < len(argument_names):
                new_ar[argument_names[i]] = arg
    new_ar["arguments"] = arguments_value


def right_hand_side_expression(ast, active_record):
    owner, key = Engine.engine[ast[1][0]](ast[1], active_record)
    if isinstance(owner, dict):
        if key in owner:
            return owner[key]
        else:
            raise Exception("'" + key + "' is not defined")
    else:
        return key


def left_hand_side_expression(ast, active_record):
    owner, key = Engine.engine[ast[1][0]](ast[1], active_record)
    if len(ast) == 3:
        if isinstance(owner, dict):
            owner = owner[key]
        else:
            owner = key
        owner, key = member_expression_part(ast[2], active_record, owner)
    if isinstance(owner, dict):
        return owner, key
    else:
        raise Exception(key + " can't be assignment")


def assignment_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return Engine.engine[ast[1][0]](ast[1], active_record)
    else:
        owner, key = left_hand_side_expression(ast[1], active_record)
        operator = assignment_operator(ast[2], active_record)
        right_value = assignment_expression_no_in(ast[3], active_record)
        if operator == "=":
            owner[key] = right_value
        elif operator == "+=":
            owner[key] += right_value
        elif operator == "-=":
            owner[key] -= right_value
        else:
            raise Exception("Unsupport operator " + operator)
        return right_value

        # if len(ast) > 2:
        #     left = Engine.engine[ast[1][0]](ast[1], active_record)
        #     right = Engine.engine[ast[3][0]](ast[3], active_record)
        #     if isinstance(right, StRef):
        #         left.obj = right.obj
        #     else:
        #         left.obj = right
        #     return left.obj
        # else:
        #     return Engine.engine[ast[1][0]](ast[1], active_record)


def assignment_operator(ast, active_record):
    return ast[1]


def expression_no_in(ast, active_record):
    return assignment_expression_no_in(ast[1], active_record)


#
# def function_declaration(ast, active_record):
#     Engine.traverse(ast, active_record)


def function_expression(ast, active_record):
    func_proto = StFunction()
    func_proto.outFunction = active_record
    for child in ast:
        if isinstance(child, list) and child[0] == Identifier:
            func_proto.name = child[1]
            active_record[child[1]] = func_proto
        if isinstance(child, list) and child[0] == FormalParameterList:
            func_proto.argument_list = formal_parameter_list(child, active_record)
        if isinstance(child, list) and child[0] == FunctionBody:
            func_proto.ast = child
    return None, func_proto


def formal_parameter_list(ast, active_record):
    ret = []
    for x in ast:
        if isinstance(x, list):
            ret.append(x[1])
    return ret


def function_body(ast, active_record):
    if len(ast) == 3:
        return UNDEFINED
    else:
        ret = statement_list(ast[2], active_record)
        if ret is None:
            ret = UNDEFINED
    return ret


def variable_statement(ast, active_record):
    var = ast[2][1]
    if len(ast) <= 4:
        active_record[var] = UNDEFINED
    else:
        active_record[var] = assignment_expression_no_in(ast[4], active_record)
