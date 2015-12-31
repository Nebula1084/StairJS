from Control import *
from Object import *
from Operator import *
from Expression import *
from NonTerminal import *

glb = StActiveRecord()
glb["this"] = glb


def interpret(ast):
    program(ast, glb)


engine = {
    Block: block,
    PrimaryExpression: primary_expression,
    Literal: literal,
    Identifier: identifier,
    ArrayLiteral: array_literal,
    ElementList: element_list,
    ElementList_END_WITH_EX: element_list_end_with_ex,
    ObjectLiteral: object_literal,
    PropertyNameAndValueList: property_name_and_value_list,
    PropertyNameAndValue: property_name_and_value,
    PropertyName: property_name,
    MemberExpression: member_expression,
    AllocationExpression: allocation_expression,
    MemberExpressionPart: member_expression_part,
    CallExpression: call_expression,
    CallExpressionPart: call_expression_part,
    Arguments: arguments,
    ArgumentList: argument_list,
    RightHandSideExpression: right_hand_side_expression,
    LeftHandSideExpression: left_hand_side_expression,
    PostfixExpression: postfix_expression,
    PostfixOperator: postfix_operator,
    UnaryExpression: unary_expression,
    UnaryOperator: unary_operator,
    MultiplicativeExpression: multiplicative_expression,
    MultiplicativeOperator: multiplicative_operator,
    AdditiveExpression: additive_expression,
    AdditiveOperator: additive_operator,
    ShiftExpression: shift_expression,
    ShiftOperator: shift_operator,
    RelationalExpressionNoIn: relational_expression_no_in,
    RelationalNoInOperator: relational_no_in_operator,
    EqualityExpressionNoIn: equality_expression_no_in,
    EqualityOperator: equality_operator,
    BitwiseANDExpressionNoIn: bitwise_and_expression_no_in,
    BitwiseANDOperator: bitwise_and_operator,
    BitwiseXORExpressionNoIn: bitwise_xor_expression_no_in,
    BitwiseXOROperator: bitwise_xor_operator,
    BitwiseORExpressionNoIn: bitwise_or_expression_no_in,
    BitwiseOROperator: bitwise_or_operator,
    LogicalANDExpressionNoIn: logical_and_expression_no_in,
    LogicalANDOperator: logical_and_operator,
    LogicalORExpressionNoIn: logical_or_expression_no_in,
    LogicalOROperator: logical_or_operator,
    AssignmentExpressionNoIn: assignment_expression_no_in,
    AssignmentOperator: assignment_operator,
    ExpressionNoIn: expression_no_in,
    Statement: statement,
    StatementList: statement_list,
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
    FunctionDeclaration: function_declaration,
    FunctionExpression: function_expression,
    FormalParameterList: formal_parameter_list,
    MoreFormalParameter: more_formal_parameter,
    FunctionBody: function_body,
    Program: program,
    SourceElements: source_elements,
    SourceElement: source_element,
}


def traverse(ast, this, debug=False):
    if debug:
        print(ast[0])
    length = len(ast)
    for i in range(1, length):
        if isinstance(ast[i], list) and ast[i][0] in engine:
            engine[ast[i][0]](ast[i], this)
        else:
            if debug:
                print ast[i]


def iterate(ast, this, debug=False):
    if debug:
        print(ast[0])
    length = len(ast)
    for i in range(1, length):
        if isinstance(ast[i], list) and ast[i][0] in engine:
            yield engine[ast[i][0]](ast[i], this), ast[i][0]
        else:
            if debug:
                print ast[i]
