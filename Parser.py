from __future__ import print_function
import ply.lex as lex

# import pdb
unsupported = (
    'abstract',
    'arguments',
    'boolean',
    'byte',
    'case',
    'catch',
    'char',
    'class',
    'const',
    'debugger',
    'default',
    'delete',
    'double',
    'enum',
    'eval',
    'export',
    'extends',
    'false',
    'final',
    'finally',
    'float',
    'goto',
    'implements',
    'import',
    'instanceof',
    'int',
    'interface',
    'let',
    'long',
    'native',
    'package',
    'private',
    'protected',
    'public',
    'short',
    'static',
    'super',
    'switch',
    'synchronized',
    'throw',
    'throws',
    'transient',
    'true',
    'try',
    'typeof',
    'void',
    'volatile',
    'with',
    'yield'
)
reserved = {
#     'abstract':'ABSTRACT',
#     'arguments':'ARGUMENTS',
#     'boolean':'BOOLEAN',
#     'break':'BREAK',
#     'byte':'BYTE',
#     'case':'CASE',
#     'catch':'CATCH',
#     'char':'CHAR',
#     'class':'CLASS',
#     'const':'CONST',
#     'continue':'CONTINUE',
#     'debugger':'DEBUGGER',
#     'default':'DEFAULT',
    'delete':'DELETE',
    'do':'DO',
    # 'double':'DOUBLE',
    'else':'ELSE',
    # 'enum':'ENUM',
    # 'eval':'EVAL',
    # 'export':'EXPORT',
    # 'extends':'EXTENDS',
    # 'false':'FALSE',
    # 'final':'FINAL',
    # 'finally':'FINALLY',
    # 'float':'FLOAT',
    'for':'FOR',
    'function':'FUNCTION',
    # 'goto':'GOTO',
    'if':'IF',
    # 'implements':'IMPLEMENTS',
    # 'import':'IMPORT',
    'in':'IN',
    'instanceof':'INSTANCEOF',
    # 'int':'INT',
    # 'interface':'INTERFACE',
    # 'let':'LET',
    # 'long':'LONG',
    # 'native':'NATIVE',
    'new':'NEW',
    'null':'NULL',
    # 'package':'PACKAGE',
    'print':'PRINT',
    # 'private':'PRIVATE',
    # 'protected':'PROTECTED',
    # 'public':'PUBLIC',
    'return':'RETURN',
    # 'short':'SHORT',
    # 'static':'STATIC',
    # 'super':'SUPER',
    # 'switch':'SWITCH',
    # 'synchronized':'SYNCHRONIZED',
    'this':'THIS',
    # 'throw':'THROW',
    # 'throws':'THROWS',
    # 'transient':'TRANSIENT',
    # 'true':'TRUE',
    # 'try':'TRY',
    'typeof':'TYPEOF',
    'var':'VAR',
    'void':'VOID',
    # 'volatile':'VOLATILE',
    'while':'WHILE',
    # 'with':'WITH',
    # 'yield':'YIELD'
}

operator = [
    "PLUS_PLUS",
    "MINUS_MINUS",
    "PLUS",
    "MINUS",
    "BIT_WISE_NOT",
    "NOT",
    "EQUAL_EQUAL",
    "NOT_EQUAL",
    "EQUAL_EQUAL_EQUAL",
    "NOT_EQUAL_EQUAL",
    "EQUAL",
    "MUL_EQUAL",
    "DIV_EQUAL",
    "MOD_EQUAL",
    "PLUS_EQUAL",
    "MINUS_EQUAL",
    "SHIFT_LEFT_EQUAL",
    "SHIFT_RIGHT_ARITHMATIC_EQUAL",
    "SHIFT_RIGHT_LOGIC_EQUAL",
    "AND_EQUAL",
    "XOR_EUQAL",
    "OR_EUQAL",
    "SHIFT_LEFT",
    "SHIFT_RIGHT_ARITHMATIC",
    "SHIFT_RIGHT_LOGIC",
    "AND_AND",
    "OR_OR",
    "LESS_THAN",
    "GREAT_THAN",
    "LESS_EQUAL_THAN",
    "GREAT_EQUAL_THAN",
    "MUL",
    "DIV",
    "MOD",
    "OR",
    "XOR",
    "AND"
]

tokens = [
    'IDENTIFIER_NAME',
    'FLOAT_LITERAL',
    'DECIMAL_INTEGER_LITERAL',
    'HEX_INTEGER_LITERAL',
    'BOOLEAN_LITERAL',
    'STRING_LITERAL'
    ] + list(reserved.values()) + operator

def t_BOOLEAN_LITERAL(t):
    r'false|true'
    t.value = bool(t.value)
    return t

def t_IDENTIFIER_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in unsupported:
        raise Exception('"' + t.value + '" is Forbidden used as Identifier.')
    t.type = reserved.get(t.value,'IDENTIFIER_NAME')    # Check for reserved words
    return t

t_PLUS_PLUS = r"\+\+"
t_MINUS_MINUS = r"--"
t_PLUS = r"\+"
t_MINUS = r"-"
t_BIT_WISE_NOT = r"~"
t_NOT = r"!" 
t_EQUAL_EQUAL = r"=="
t_NOT_EQUAL = r"!="
t_EQUAL_EQUAL_EQUAL = r"==="
t_NOT_EQUAL_EQUAL = r"!=="
t_EQUAL = r"="
t_MUL_EQUAL = r"\*="
t_DIV_EQUAL = r"/="
t_MOD_EQUAL = r"%="
t_PLUS_EQUAL = r"\+="
t_MINUS_EQUAL = r"-="
t_SHIFT_LEFT_EQUAL = r"<<="
t_SHIFT_RIGHT_ARITHMATIC_EQUAL = r">>="
t_SHIFT_RIGHT_LOGIC_EQUAL = r">>>="
t_AND_EQUAL = r"&="
t_XOR_EUQAL = r"^="
t_OR_EUQAL = r"\|="
t_SHIFT_LEFT = r"<<"
t_SHIFT_RIGHT_ARITHMATIC = r">>"
t_SHIFT_RIGHT_LOGIC = r">>>"
t_AND_AND = r"&&"
t_OR_OR = r"\|\|"
t_LESS_THAN = r"<"
t_GREAT_THAN = r">"
t_LESS_EQUAL_THAN = r"<="
t_GREAT_EQUAL_THAN = r">="
t_MUL = r"\*"
t_DIV = r"/"
t_MOD = r"%"
t_OR = r"\|"
t_XOR = r"\^"
t_AND = r"&"


# pdb.set_trace()

def t_STRING_LITERAL(t):
    r'("([^\\"]|\\"|\\\\|\\n|\\t|\\r|\\v|\\b|\\f)*")|(\'([^\\\']|\\\'|\\\\|\\n|\\t|\\r|\\v|\\b|\\f)*\')'
    t.value = eval(t.value)
    return t

def t_COMMENT(t):
    r'(//.*)|(/\*(.|\n)*\*/)'
    t.lexer.lineno += t.value.count("\n")
    pass
    # No return value. Token discarded

def t_FLOAT_LITERAL(t):
    r'(\d+\.\d+)|(\d+e-?\d+)'
    t.value = float(t.value)
    return t


def t_DECIMAL_INTEGER_LITERAL(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_HEX_INTEGER_LITERAL(t):
    r'0x\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    raise Exception("Illegal character '%s' at line %d" % (t.value[0],lexer.lineno))

# # EOF handling rule
# def t_eof(t):
#     # Get more input (Example)
#     more = input('... ')
#     if more:
#         self.lexer.input(more)
#         return self.lexer.token()
#     return None

t_ignore = ' \t\f\v'
literals = "(){}[];.,?:"

# if __name__ == '__main__':
#     lex.runmain()

# lexer = lex.lex()#optimize=1)
# with open("HelloWorld.js") as file:
#     lexer.input(file.read())
#     for tok in lexer:
#         print(tok)
start = "Program"

# def p_empty(p):
#     """ empty : """

def p_error(t):
    pass

def p_Block(p):
    """Block : '{' StatementList '}'
    | '{'  '}'"""
    p[0] = "Block"
    p[0] = list(p)
    # print("Block")


def p_PrimaryExpression(p):
    """PrimaryExpression : THIS
    |   ObjectLiteral
    |   '(' ExpressionNoIn ')' 
    |   Identifier
    |   ArrayLiteral
    |   Literal
    |   FunctionExpression"""
    p[0] = "PrimaryExpression"
    p[0] = list(p)

def p_Literal(p):
    """Literal : DECIMAL_INTEGER_LITERAL 
    | HEX_INTEGER_LITERAL 
    | STRING_LITERAL 
    | BOOLEAN_LITERAL 
    | FLOAT_LITERAL
    | NULL """
    p[0] = "Literal"
    p[0] = list(p)


def p_Identifier(p):
    """Identifier : IDENTIFIER_NAME"""
    p[0] = "Identifier"
    p[0] = list(p)


def p_ArrayLiteral(p):
    """ArrayLiteral : '[' ElementList ']'"""
    p[0] = "ArrayLiteral"
    p[0] = list(p)

def p_ElementList(p):
    """ElementList : ElementList_END_WITH_EX
    | ElementList_END_WITH_EX AssignmentExpressionNoIn """
    if len(p) == 3:
        p[1].append(p[2])
    p[0] = p[1]

def p_ElementList_END_WITH_EX(p):
    """ElementList_END_WITH_EX : AssignmentExpressionNoIn 
    |   ',' 
    |   ElementList_END_WITH_EX AssignmentExpressionNoIn ','
    |   ElementList_END_WITH_EX ','"""
    if len(p) == 2:
        p[0] = ["ElementList", p[1]]
    elif len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    elif len(p) == 4:
        p[1].append(p[2])
        p[1].append(p[3])
        p[0] = p[1]


def p_ObjectLiteral(p):
    """ObjectLiteral : '{' PropertyNameAndValueList '}'
    | '{'  '}'"""
    p[0] = "ObjectLiteral"
    p[0] = list(p)


def p_PropertyNameAndValueList(p):
    """PropertyNameAndValueList : PropertyNameAndValue 
    |  PropertyNameAndValueList ',' PropertyNameAndValue """
    if len(p) == 4:
        p[1].append(p[2])
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = ["PropertyNameAndValueList",p[1]]


def p_PropertyNameAndValue(p):
    """PropertyNameAndValue : PropertyName ':' AssignmentExpressionNoIn"""
    p[0] = "PropertyNameAndValue"
    p[0] = list(p)


def p_PropertyName(p):
    """PropertyName : Identifier
    |   STRING_LITERAL
    |   DECIMAL_INTEGER_LITERAL
    |   HEX_INTEGER_LITERAL
    |   FLOAT_LITERAL"""
    p[0] = "PropertyName"
    p[0] = list(p)


def p_MemberExpression(p):
    """MemberExpression : PrimaryExpression 
    |   AllocationExpression
    |   MemberExpression MemberExpressionPart """
    p[0] = "MemberExpression"
    p[0] = list(p)


def p_AllocationExpression(p):
    """AllocationExpression : NEW MemberExpression Arguments"""
    p[0] = "AllocationExpression"
    p[0] = list(p)


def p_MemberExpressionPart(p):
    """MemberExpressionPart : '[' ExpressionNoIn ']' 
    | '.' Identifier """
    p[0] = "MemberExpressionPart"
    p[0] = list(p)


def p_CallExpression(p):
    """CallExpression : MemberExpression Arguments
    | CallExpression CallExpressionPart """
    p[0] = "CallExpression"
    p[0] = list(p)


def p_CallExpressionPart(p):
    """CallExpressionPart : Arguments
    |   '[' ExpressionNoIn ']'
    |   '.' Identifier """
    p[0] = "CallExpressionPart"
    p[0] = list(p)


def p_Arguments(p):
    """Arguments : '(' ArgumentList ')'
    | '('  ')'"""
    p[0] = "Arguments"
    p[0] = list(p)


def p_ArgumentList(p):
    """ArgumentList : AssignmentExpressionNoIn 
    | ArgumentList ',' AssignmentExpressionNoIn """
    if len(p) == 4:
        p[1].append(p[2])
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = ["ArgumentList",p[1]]


def p_RightHandSideExpression(p):
    """RightHandSideExpression : CallExpression
    |   MemberExpression"""
    p[0] = "RightHandSideExpression"
    p[0] = list(p)

def p_LeftHandSideExpression(p):
    """LeftHandSideExpression  ::= Identifier
    |   CallExpression MemberExpressionPart 
    |   MemberExpression MemberExpressionPart """
    p[0] = "LeftHandSideExpression"
    p[0] = list(p)

def p_PostfixExpression(p):
    """PostfixExpression : RightHandSideExpression 
    | PostfixExpression PostfixOperator """
    p[0] = "PostfixExpression"
    p[0] = list(p)


def p_PostfixOperator(p):
    """PostfixOperator : PLUS_PLUS 
    | MINUS_MINUS"""
    p[0] = "PostfixOperator"
    p[0] = list(p)


def p_UnaryExpression(p):
    """UnaryExpression : PostfixExpression 
    | UnaryOperator UnaryExpression """
    p[0] = "UnaryExpression"
    p[0] = list(p)


def p_UnaryOperator(p):
    """UnaryOperator : DELETE 
    | VOID 
    | TYPEOF 
    | PLUS_PLUS 
    | MINUS_MINUS
    | PLUS 
    | MINUS 
    | BIT_WISE_NOT 
    | NOT """
    p[0] = "UnaryOperator"
    p[0] = list(p)


def p_MultiplicativeExpression(p):
    """MultiplicativeExpression : UnaryExpression 
    | MultiplicativeExpression MultiplicativeOperator UnaryExpression """
    p[0] = "MultiplicativeExpression"
    p[0] = list(p)


def p_MultiplicativeOperator(p):
    """MultiplicativeOperator : MUL 
    | DIV 
    | MOD """
    p[0] = "MultiplicativeOperator"
    p[0] = list(p)


def p_AdditiveExpression(p):
    """AdditiveExpression : MultiplicativeExpression 
    | AdditiveExpression AdditiveOperator MultiplicativeExpression """
    p[0] = "AdditiveExpression"
    p[0] = list(p)


def p_AdditiveOperator(p):
    """AdditiveOperator : PLUS 
    | MINUS """
    p[0] = "AdditiveOperator"
    p[0] = list(p)


def p_ShiftExpression(p):
    """ShiftExpression : AdditiveExpression 
    | ShiftExpression ShiftOperator AdditiveExpression """
    p[0] = "ShiftExpression"
    p[0] = list(p)


def p_ShiftOperator(p):
    """ShiftOperator : SHIFT_LEFT 
    | SHIFT_RIGHT_ARITHMATIC 
    | SHIFT_RIGHT_LOGIC """
    p[0] = "ShiftOperator"
    p[0] = list(p)


def p_RelationalExpressionNoIn(p):
    """RelationalExpressionNoIn : ShiftExpression 
    | RelationalExpressionNoIn RelationalNoInOperator ShiftExpression """
    p[0] = "RelationalExpressionNoIn"
    p[0] = list(p)


def p_RelationalNoInOperator(p):
    """RelationalNoInOperator : LESS_THAN 
    | GREAT_THAN 
    | LESS_EQUAL_THAN 
    | GREAT_EQUAL_THAN 
    | INSTANCEOF """
    p[0] = "RelationalNoInOperator"
    p[0] = list(p)


def p_EqualityExpressionNoIn(p):
    """EqualityExpressionNoIn : RelationalExpressionNoIn 
    | EqualityExpressionNoIn EqualityOperator RelationalExpressionNoIn """
    p[0] = "EqualityExpressionNoIn"
    p[0] = list(p)


def p_EqualityOperator(p):
    """EqualityOperator : EQUAL_EQUAL 
    | NOT_EQUAL 
    | EQUAL_EQUAL_EQUAL 
    | NOT_EQUAL_EQUAL """
    p[0] = "EqualityOperator"
    p[0] = list(p)


def p_BitwiseANDExpressionNoIn(p):
    """BitwiseANDExpressionNoIn : EqualityExpressionNoIn
    | BitwiseANDExpressionNoIn BitwiseANDOperator EqualityExpressionNoIn """
    p[0] = "BitwiseANDExpressionNoIn"
    p[0] = list(p)


def p_BitwiseANDOperator(p):
    """BitwiseANDOperator : AND"""
    p[0] = "BitwiseANDOperator"
    p[0] = list(p)


def p_BitwiseXORExpressionNoIn(p):
    """BitwiseXORExpressionNoIn : BitwiseANDExpressionNoIn 
    | BitwiseXORExpressionNoIn BitwiseXOROperator BitwiseANDExpressionNoIn """
    p[0] = "BitwiseXORExpressionNoIn"
    p[0] = list(p)


def p_BitwiseXOROperator(p):
    """BitwiseXOROperator : XOR"""
    p[0] = "BitwiseXOROperator"
    p[0] = list(p)


def p_BitwiseORExpressionNoIn(p):
    """BitwiseORExpressionNoIn : BitwiseXORExpressionNoIn 
    | BitwiseORExpressionNoIn BitwiseOROperator BitwiseXORExpressionNoIn """
    p[0] = "BitwiseORExpressionNoIn"
    p[0] = list(p)


def p_BitwiseOROperator(p):
    """BitwiseOROperator : OR"""
    p[0] = "BitwiseOROperator"
    p[0] = list(p)


def p_LogicalANDExpressionNoIn(p):
    """LogicalANDExpressionNoIn : BitwiseORExpressionNoIn 
    | LogicalANDExpressionNoIn LogicalANDOperator BitwiseORExpressionNoIn """
    p[0] = "LogicalANDExpressionNoIn"
    p[0] = list(p)


def p_LogicalANDOperator(p):
    """LogicalANDOperator : AND_AND"""
    p[0] = "LogicalANDOperator"
    p[0] = list(p)


def p_LogicalORExpressionNoIn(p):
    """LogicalORExpressionNoIn : LogicalANDExpressionNoIn 
    | LogicalORExpressionNoIn LogicalOROperator LogicalANDExpressionNoIn """
    p[0] = "LogicalORExpressionNoIn"
    p[0] = list(p)


def p_LogicalOROperator(p):
    """LogicalOROperator : OR_OR"""
    p[0] = "LogicalOROperator"
    p[0] = list(p)


def p_AssignmentExpressionNoIn(p):
    """AssignmentExpressionNoIn : LeftHandSideExpression AssignmentOperator AssignmentExpressionNoIn
    |   LogicalORExpressionNoIn"""
    p[0] = "AssignmentExpressionNoIn"
    p[0] = list(p)



def p_AssignmentOperator(p):
    """AssignmentOperator : EQUAL
    | MUL_EQUAL
    | DIV_EQUAL
    | MOD_EQUAL
    | PLUS_EQUAL 
    | MINUS_EQUAL 
    | SHIFT_LEFT_EQUAL
    | SHIFT_RIGHT_ARITHMATIC_EQUAL 
    | SHIFT_RIGHT_LOGIC_EQUAL 
    | AND_EQUAL 
    | XOR_EUQAL 
    | OR_EUQAL"""
    p[0] = "AssignmentOperator"
    p[0] = list(p)


def p_ExpressionNoIn(p):
    """ExpressionNoIn : AssignmentExpressionNoIn 
    | ExpressionNoIn ',' AssignmentExpressionNoIn"""
    p[0] = "ExpressionNoIn"
    p[0] = list(p)

def p_Statement(p):
    """Statement : Block
    |   VariableStatement
    |   EmptyStatement
    |   ExpressionNoInStatement
    |   IfStatement
    |   IterationStatement
    |   ReturnStatement
    |   PrintStatement"""
    p[0] = "Statement"
    p[0] = list(p)
    # print("Statement")


def p_StatementList(p):
    """StatementList : Statement
    | StatementList Statement"""
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else:
        p[0] = "StatementList"
        p[0] = list(p)
    # print("StatementList")


def p_VariableStatement(p):
    """VariableStatement : VAR Identifier ';' 
    | VAR Identifier 
    | VAR Identifier EQUAL AssignmentExpressionNoIn
    | VAR Identifier EQUAL AssignmentExpressionNoIn ';'"""
    p[0] = "VariableStatement"
    p[0] = list(p)
    # print("VariableStatement")


def p_EmptyStatement(p):
    """EmptyStatement : ';'"""
    p[0] = "EmptyStatement"
    p[0] = list(p)
    # print("EmptyStatement")


def p_ExpressionNoInStatement(p):
    """ExpressionNoInStatement : ExpressionNoIn ';'
    |  ExpressionNoIn """
    p[0] = "ExpressionNoInStatement"
    p[0] = list(p)
    # print("ExpressionNoInStatement")

def p_IfStatement(p):
    """IfStatement : IF '(' ExpressionNoIn ')' Statement ELSE Statement 
    | IF '(' ExpressionNoIn ')' Statement """
    p[0] = "IfStatement"
    p[0] = list(p)
    # print("IfStatement")


def p_IterationStatement(p):
    """IterationStatement : DoStatement
    |   WhileStatement
    |   OriginForStatement
    |   ForEachStatement"""
    p[0] = "IterationStatement"
    p[0] = list(p)
    # print("IterationStatement")


def p_DoStatement(p):
    """DoStatement : DO Statement WHILE '(' ExpressionNoIn ')' ';' 
    | DO Statement WHILE '(' ExpressionNoIn ')' """
    p[0] = "DoStatement"
    p[0] = list(p)
    # print("DoStatement")


def p_WhileStatement(p):
    """WhileStatement : WHILE '(' ExpressionNoIn ')' Statement"""
    p[0] = "WhileStatement"
    p[0] = list(p)
    # print("WhileStatement")


def p_OriginForStatement(p):
    """OriginForStatement : FOR '(' ExpressionNoIn  ';' ExpressionNoIn ';' ExpressionNoIn  ')' Statement"""
    p[0] = "OriginForStatement"
    p[0] = list(p)
    # print("OriginForStatement")

def p_ForEachStatement(p):
    """ForEachStatement : FOR '(' VAR Identifier IN ExpressionNoIn ')' Statement"""
    p[0] = 'ForEachStatement'
    p[0] = list(p)

def p_ReturnStatement(p):
    """ReturnStatement : RETURN ExpressionNoIn ';' 
    | RETURN ExpressionNoIn 
    | RETURN ';' 
    | RETURN"""
    p[0] = "ReturnStatement"
    p[0] = list(p)
    # print("ReturnStatement")

def p_PrintStatement(p):
    """PrintStatement : PRINT ExpressionNoIn ';'
    | PRINT ExpressionNoIn """
    p[0] = "PrintStatement"
    p[0] = list(p)

# def p_FunctionDeclaration(p):
#     """FunctionDeclaration : FUNCTION Identifier '(' FormalParameterList ')' FunctionBody
#                     | FUNCTION Identifier '(' ')' FunctionBody"""
#     p[0] = 'FunctionDeclaration'
#     p[0] = list(p)
#     # print("FunctionDeclaration")

def p_FunctionExpression(p):
    """FunctionExpression : FUNCTION Identifier '(' FormalParameterList ')' FunctionBody
                    | FUNCTION Identifier '(' ')' FunctionBody
                    | FUNCTION '(' FormalParameterList ')' FunctionBody
                    | FUNCTION '(' ')' FunctionBody"""
    p[0] = 'FunctionExpression'
    p[0] = list(p)
    # print("FunctionExpression")

def p_FormalParameterList(p):
    """FormalParameterList : Identifier 
                    | FormalParameterList ',' Identifier"""
    if len(p) == 4:
        p[1].append(p[2])
        p[1].append(p[3])
        p[0] = p[1]
    else:
        p[0] = ['FormalParameterList',p[1]]
    # print("FormalParameterList")

# def p_MoreFormalParameter(p):
#     """MoreFormalParameter : ',' Identifier"""
#     p[0] = [p[1],p[2]]
#     # print("MoreFormalParameter")

def p_FunctionBody(p):
    """FunctionBody : '{'  '}'
                    | '{' SourceElements '}'"""
    p[0] = 'FunctionBody'
    p[0] = list(p)
    # print("FunctionBody")


def p_Program(p):
    """Program : SourceElements"""
    p[0] = ["Program",p[1]]


def p_SourceElements(p):
    """SourceElements : SourceElement
                    | SourceElements SourceElement"""
    if len(p) == 3:
        p[1].append(p[2])
        p[0] = p[1]
    else :
        p[0] = ['SourceElements',p[1]]


def p_SourceElement(p):
    """SourceElement : Statement"""
            # |   FunctionDeclaration
    p[0] = 'SourceElement'
    p[0] = list(p)

# def p_error(t):
#     raise t

def printAST(p,n):
    if p != None:
        print('  '*n,end = '')
        if type(p) is list:
            print(p[0])
            for node in p[1:]:
                printAST(node,n+1)
        else:
            print(p)

lex.lex()

import ply.yacc as yacc
yacc.yacc(debug=0)
# yacc.yacc()
if __name__ == '__main__':
    with open("HelloWorld.js") as file:
        ast = yacc.parse(file.read())
        printAST(list(ast),0)