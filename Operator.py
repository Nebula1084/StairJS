import Engine
from Object import *
from Expression import left_hand_side_expression, right_hand_side_expression


def literal(ast, active_record):
    if ast[1] != "null":
        return None, ast[1]
    else:
        return None, NULL


def postfix_expression(ast, active_record):
    if len(ast) > 2:
        owner, key = Engine.engine[ast[1][0]](ast[1], active_record)
        ret = owner[key]
        if ast[2][1] == "++":
            owner[key] += 1
        elif ast[2][1] == "--":
            owner[key] -= 1
        return None, ret
    else:
        return left_hand_side_expression(ast[1], active_record)


# def postfix_operator(ast, active_record):
#     for x, y in Engine.iterate(ast, active_record):
#         return x


def unary_expression(ast, active_record):
    if len(ast) > 2:
        operand = Engine.engine[ast[2][0]](ast[2], active_record)
        operator = ast[1][1]
        if operator == "+":
            ret = + operand
        elif operator == "-":
            ret = - operand
        elif operator == "void":
            ret = UNDEFINED
        elif operator == "typeof":
            if type(operand) == int:
                ret = "number"
            elif type(operand) == float:
                ret = "number"
            elif type(operand) == str:
                ret = "string"
            elif type(operand) == bool:
                ret = "boolean"
            elif type(operand) == StFunction:
                ret = "function"
            elif type(operand) == StObject:
                ret = "object"
            elif type(operand) == StNull:
                ret = "null"
            elif type(operand) == Undefined:
                ret = "undefined"
        elif operator == "~":
            ret = ~operand
        elif operator == "!":
            ret = not operand
    else:
        ret = Engine.engine[ast[1][0]](ast[1], active_record)
    return ret


#
# def unary_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def multiplicative_expression(ast, active_record):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], active_record)
        return ret
    else:
        a1 = Engine.engine[ast[1][0]](ast[1], active_record)
        a2 = Engine.engine[ast[3][0]](ast[3], active_record)
        if ast[2][1] == "*":
            return a1 * a2
        elif ast[2][1] == "/":
            return a1 // a2
        elif ast[2][1] == "%":
            return a1 % a2


#
# def multiplicative_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def additive_expression(ast, active_record):
    if len(ast) == 2:
        return multiplicative_expression(ast[1], active_record)
    else:
        a1 = additive_expression(ast[1], active_record)
        a2 = multiplicative_expression(ast[3], active_record)
        if ast[2][1] == "+":
            return a1 + a2
        elif ast[2][1] == "-":
            return a1 - a2


#
# def additive_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def shift_expression(ast, active_record):
    if len(ast) == 2:
        return additive_expression(ast[1], active_record)
    else:
        a1 = shift_expression(ast[1], active_record)
        a2 = additive_expression(ast[3], active_record)
        if ast[2][1] == "<<":
            return a1 << a2
        elif ast[2][1] == ">>":
            return a1 >> a2
        elif ast[2][1] == ">>>":
            ret = a1 >> a2
            if a2 > 0:
                k = int("01111111111111111111111111111111", 2) >> (a2 - 1)
                ret &= k
            return ret


#
# def shift_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def relational_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return shift_expression(ast[1], active_record)
    else:
        a1 = relational_expression_no_in(ast[1], active_record)
        a2 = shift_expression(ast[3], active_record)
        if ast[2][1] == "<":
            ret = a1 < a2
        elif ast[2][1] == ">":
            ret = a1 > a2
        elif ast[2][1] == "<=":
            ret = a1 <= a2
        elif ast[2][1] == ">=":
            ret = a1 >= a2
        # elif ast[2][1] == "instanceof":
        #     ret = isinstance(a1, a2)
        return ret


# def relational_no_in_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def equality_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return relational_expression_no_in(ast[1], active_record)
    else:
        a1 = equality_expression_no_in(ast[1], active_record);
        a2 = relational_expression_no_in(ast[3], active_record)
        if ast[2][1] == "==":
            return a1 == a2
        elif ast[2][1] == "!=":
            return a1 != a2
        elif ast[2][1] == "===":
            return a1 == a2
        elif ast[2][1] == "!==":
            return a1 != a2


# def equality_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def bitwise_and_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return equality_expression_no_in(ast[1], active_record)
    else:
        a1 = bitwise_and_expression_no_in(ast[1], active_record)
        a2 = equality_expression_no_in(ast[3], active_record)
        return a1 & a2


# def bitwise_and_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def bitwise_xor_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return bitwise_and_expression_no_in(ast[1], active_record)
    else:
        a1 = bitwise_xor_expression_no_in(ast[1], active_record)
        a2 = bitwise_and_expression_no_in(ast[3], active_record)
        return a1 ^ a2


# def bitwise_xor_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def bitwise_or_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return bitwise_xor_expression_no_in(ast[1], active_record)
    else:
        a1 = bitwise_or_expression_no_in(ast[1], active_record)
        a2 = bitwise_xor_expression_no_in(ast[3], active_record)
        return a1 | a2


# def bitwise_or_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def logical_and_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return bitwise_or_expression_no_in(ast[1], active_record)
    else:
        a1 = logical_and_expression_no_in(ast[1], active_record)
        a2 = bitwise_or_expression_no_in(ast[3], active_record)
        return a1 and a2


# def logical_and_operator(ast, active_record):
#     Engine.traverse(ast, active_record)


def logical_or_expression_no_in(ast, active_record):
    if len(ast) == 2:
        return logical_and_expression_no_in(ast[1], active_record)
    else:
        a1 = logical_or_expression_no_in(ast[1], active_record)
        a2 = logical_and_expression_no_in(ast[3], active_record)
        return a1 or a2


# def logical_or_operator(ast, active_record):
#     Engine.traverse(ast, active_record)
