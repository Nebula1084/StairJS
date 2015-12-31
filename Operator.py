import Engine
from Object import *

def literal(ast, context):
    return ast[1]


def postfix_expression(ast, context):
    if len(ast) > 2:
        x = Engine.engine[ast[1][0]](ast[1], context)
        ret = x
        if ast[2][1] == "++":
            ret = x[1]
            x[1] += 1
        elif ast[2][1] == "--":
            ret = x[1]
            x[1] -= 1
        return ret
    else:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret


def postfix_operator(ast, context):
    for x, y in Engine.iterate(ast, context):
        return x


def unary_expression(ast, context):
    if len(ast) > 2:
        x = Engine.engine[ast[2][0]](ast[2], context)
        ret = x
        if ast[1][1] == "++":
            x[1] += 1
            ret = x[1]
        elif ast[1][1] == "--":
            x[1] -= 1
            ret = x[1]
        elif ast[1][1] == "+":
            ret = x[1]
        elif ast[1][1] == "-":
            ret = -x[1]
        return ret
    else:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret


def unary_operator(ast, context):
    Engine.traverse(ast, context)


def multiplicative_expression(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        if isinstance(ret, StRef):
            ret = ret.obj
        return ret
    else:
        m1 = Engine.engine[ast[1][0]](ast[1], context)
        if isinstance(m1, StRef):
            m1 = m1.obj
        m2 = Engine.engine[ast[3][0]](ast[3], context)
        if isinstance(m2, StRef):
            m2 = m2.obj
        if ast[2][1] == "*":
            return m1 * m2
        if ast[2][1] == "/":
            return m1 / m2


def multiplicative_operator(ast, context):
    Engine.traverse(ast, context)


def additive_expression(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        a1 = Engine.engine[ast[1][0]](ast[1], context)
        a2 = Engine.engine[ast[3][0]](ast[3], context)
        if ast[2][1] == "+":
            return a1 + a2
        elif ast[2][1] == "-":
            return a1 - a2


def additive_operator(ast, context):
    Engine.traverse(ast, context)


def shift_expression(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print (Engine.engine[ast[1][0]](ast[1], context))
        print (Engine.engine[ast[3][0]](ast[3], context))


def shift_operator(ast, context):
    Engine.traverse(ast, context)


def relational_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(Engine.engine[ast[1][0]](ast[1], context))
        print(Engine.engine[ast[3][0]](ast[3], context))
        # if(ast[2][1] == "==="):
        #     return relational_expression_no_in(ast[1]) == shift_expression(ast[3])


def relational_no_in_operator(ast, context):
    Engine.traverse(ast, context)


def equality_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def equality_operator(ast, context):
    Engine.traverse(ast, context)


def bitwise_and_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def bitwise_and_operator(ast, context):
    Engine.traverse(ast, context)


def bitwise_xor_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def bitwise_xor_operator(ast, context):
    Engine.traverse(ast, context)


def bitwise_or_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def bitwise_or_operator(ast, context):
    Engine.traverse(ast, context)


def logical_and_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def logical_and_operator(ast, context):
    Engine.traverse(ast, context)


def logical_or_expression_no_in(ast, context):
    if len(ast) != 4:
        ret = Engine.engine[ast[1][0]](ast[1], context)
        return ret
    else:
        print(ngine.engine[ast[1][0]](ast[1], context))
        print(ngine.engine[ast[3][0]](ast[3], context))


def logical_or_operator(ast, context):
    Engine.traverse(ast, context)
