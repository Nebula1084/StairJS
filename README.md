#Stair Engine
First of all, we regard global code as a `function` and treat it accordingly.
##Object Struct
Everything in **Stair JS** is `Object` and would be instantiated by a struct
which is implemented by **C**.
~~~C
struct Object{
	Type type;
	char* name;
	void* fileds;
	char* code;
	struct Object* this;
	struct Object* outFunction;
	char** arguments;
};
~~~
Fields of this structure would be filled according to its type.
##Dictionary
~~~C
struct Dict;
~~~
This data structure would provide a flexiable method to record status of 
every object, whose key is **name of field** and value is **object structure**.
Thus its structure is `{char* : struct Object*}`
##FuncProto
We demonstrate basic plain code as `FuncProto` object which is used in 
instantiation of `Function`. And FuncProto would be instantiated by Interpreter
automatically. 
1. Flied `type` would be filled by `FuncProto`.
2. And interpreter would only fill **code** with `text`.
3. Besides **fileds** is set to be `NULL`.
4. Especially, **outFunction** must be set to the `funtion` where we define this 
`function`.
5. **arguments** must be specified explicitly. We pass a list of name to 
the `FuncProto` whenever instantiation of `FuncProto` happend.


##Function
Whenever a function is invoked. A `Funtion` Object would be instantiated by 
corresponding `FuncProto`.
1. **type** would be set to `Function` 
2. And **fileds** would be allocated new memory space, which 
represented by a `pointer` to `Dict`.
3. Copy `FuncProto`'s **code** to `Function`'s **code** filed.
4. Pass **arguments** to this structure as well as **outFunction**.
5. **This** also need to be specified, but it depends on specfic condition.
###Function Invocation
In `Function` invocations, there are following two situation.
		f();	
**this** we pass is current local `this`.
		a.f();
And in this situation, **this** is `pointer` fo `Object` a.
 
##Object
A `Object` could be instantiated by `Function`. Basic operation is like the 
way we perform in Function instatiation but **this** must be a new `pointer` 
to `struct Object` that we allocate recently.

##Primtive Type
We present `Primtive Type` in format of `Struct Object`. However, `Javascript`
treat her reference mechanism like `Java`. Its **fileds** would be corresponding
type. Primtive Type is passed by value.
Thus, we must create a new object as same as original one. Currently, following
`Primtive Type` is planed to be implemented.
1. int
2. float
3. string
4. bool

##Parameter Pass
Parameters would be passed to the **fields**. And interpretor would scrutinize
the number of parameter is matched or not.
##Return Value
Simply, we just return `struct Object`.
##Function Closure
In order to accomplish `Function Closure`, we introduce **outFunction**.
Interpretor would scan local scope to find current variables. It would find
variables in **outFunction** if not find in local scope yet. Searching priority
is presented below.
1. Local scope
2. This
3. outFunction Recursively.

##Code Slice
We confine syntas of `Stair JS` restrictly. Every operand and operator must
be sperated by `blank`. Similarily `semicolon` would split every statement.

<html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>BNF for StairScript--A Subset of JavaScript</title>
</head>
<body>
<h1 align="CENTER">BNF for StairScript--A Subset of JavaScript</h1>
<h2 align="CENTER">NON-TERMINALS</h2>
<table>
<tbody>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod1">PrimaryExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"this"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod2">ObjectLiteral</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "(" <a href="#prod3">ExpressionNoIn</a> ")" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod5">ArrayLiteral</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod6">Literal</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod6">Literal</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( &lt;DECIMAL_LITERAL&gt; | &lt;HEX_INTEGER_LITERAL&gt; | &lt;STRING_LITERAL&gt; | &lt;BOOLEAN_LITERAL&gt; | &lt;NULL_LITERAL&gt; | &lt;REGULAR_EXPRESSION_LITERAL&gt; )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod4">Identifier</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">&lt;IDENTIFIER_NAME&gt;</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod5">ArrayLiteral</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"[" <a href="#prod8">ElementList</a> "]"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod8">ElementList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( ( <a href="#prod9">AssignmentExpression</a> )? <a href="#prod7">Elision</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod2">ObjectLiteral</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"{" ( <a href="#prod10">PropertyNameAndValueList</a> )? "}"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod10">PropertyNameAndValueList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod11">PropertyNameAndValue</a> ( "," <a href="#prod11">PropertyNameAndValue</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod11">PropertyNameAndValue</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod12">PropertyName</a> ":" <a href="#prod9">AssignmentExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod12">PropertyName</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">&lt;STRING_LITERAL&gt;</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">&lt;DECIMAL_LITERAL&gt;</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod13">MemberExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( ( <a href="#prod14">FunctionExpression</a> | <a href="#prod1">PrimaryExpression</a> ) ( <a href="#prod15">MemberExpressionPart</a> )* )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod16">AllocationExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod16">AllocationExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "new" <a href="#prod13">MemberExpression</a> ( ( <a href="#prod18">Arguments</a> ( <a href="#prod15">MemberExpressionPart</a> )* )* ) )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod15">MemberExpressionPart</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "[" <a href="#prod3">Expression</a> "]" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "." <a href="#prod4">Identifier</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod19">CallExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod13">MemberExpression</a> <a href="#prod18">Arguments</a> ( <a href="#prod20">CallExpressionPart</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod20">CallExpressionPart</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod18">Arguments</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "[" <a href="#prod3">Expression</a> "]" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "." <a href="#prod4">Identifier</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod18">Arguments</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"(" ( <a href="#prod22">ArgumentList</a> )? ")"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod22">ArgumentList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod9">AssignmentExpression</a> ( "," <a href="#prod9">AssignmentExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod23">LeftHandSideExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod19">CallExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod13">MemberExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod25">PostfixExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod23">LeftHandSideExpression</a> ( <a href="#prod26">PostfixOperator</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod26">PostfixOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "++" | "--" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod27">UnaryExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod25">PostfixExpression</a> | ( <a href="#prod28">UnaryOperator</a> <a href="#prod27">UnaryExpression</a> )+ )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod28">UnaryOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "delete" | "void" | "typeof" | "++" | "--" | "+" | "-" | "~" | "!" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod29">MultiplicativeExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod27">UnaryExpression</a> ( <a href="#prod30">MultiplicativeOperator</a> <a href="#prod27">UnaryExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod30">MultiplicativeOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "*" | &lt;SLASH&gt; | "%" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod31">AdditiveExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod29">MultiplicativeExpression</a> ( <a href="#prod32">AdditiveOperator</a> <a href="#prod29">MultiplicativeExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod32">AdditiveOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "+" | "-" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod33">ShiftExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod31">AdditiveExpression</a> ( <a href="#prod34">ShiftOperator</a> <a href="#prod31">AdditiveExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod34">ShiftOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "&lt;&lt;" | "&gt;&gt;" | "&gt;&gt;&gt;" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod37">RelationalExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod33">ShiftExpression</a> ( <a href="#prod38">RelationalNoInOperator</a> <a href="#prod33">ShiftExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod38">RelationalNoInOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "&lt;" | "&gt;" | "&lt;=" | "&gt;=" | "instanceof" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod41">EqualityExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod37">RelationalExpressionNoIn</a> ( <a href="#prod40">EqualityOperator</a> <a href="#prod37">RelationalExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod40">EqualityOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "==" | "!=" | "===" | "!==" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod44">BitwiseANDExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod41">EqualityExpressionNoIn</a> ( <a href="#prod43">BitwiseANDOperator</a> <a href="#prod41">EqualityExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod43">BitwiseANDOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"&amp;"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod47">BitwiseXORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod44">BitwiseANDExpressionNoIn</a> ( <a href="#prod46">BitwiseXOROperator</a> <a href="#prod44">BitwiseANDExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod46">BitwiseXOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"^"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod50">BitwiseORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod47">BitwiseXORExpressionNoIn</a> ( <a href="#prod49">BitwiseOROperator</a> <a href="#prod47">BitwiseXORExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod49">BitwiseOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"|"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod53">LogicalANDExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod50">BitwiseORExpressionNoIn</a> ( <a href="#prod52">LogicalANDOperator</a> <a href="#prod50">BitwiseORExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod52">LogicalANDOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"&amp;&amp;"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod56">LogicalORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod53">LogicalANDExpressionNoIn</a> ( <a href="#prod55">LogicalOROperator</a> <a href="#prod53">LogicalANDExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod55">LogicalOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"||"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod59">AssignmentExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod23">LeftHandSideExpression</a> <a href="#prod60">AssignmentOperator</a> <a href="#prod59">AssignmentExpressionNoIn</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod56">LogicalORExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod60">AssignmentOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "=" | "*=" | &lt;SLASHASSIGN&gt; | "%=" | "+=" | "-=" | "&lt;&lt;=" | "&gt;&gt;=" | "&gt;&gt;&gt;=" | "&amp;=" | "^=" | "|=" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod61">ExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod59">AssignmentExpressionNoIn</a> ( "," <a href="#prod59">AssignmentExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod62">Statement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod63">Block</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod65">VariableStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod66">EmptyStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod68">ExpressionNoInStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod69">IfStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod70">IterationStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod74">ReturnStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod63">Block</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"{" ( <a href="#prod79">StatementList</a> )? "}"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod79">StatementList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod62">Statement</a> )+</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod65">VariableStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"var" <a href="#prod4">Identifier</a> ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod66">EmptyStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">";"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod68">ExpressionNoInStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod61">ExpressionNoIn</a> ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod69">IfStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"if" "(" <a href="#prod3">Expression</a> ")" <a href="#prod62">Statement</a> ( "else" <a href="#prod62">Statement</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod70">IterationStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod102">DoStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod103">WhileStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod104">OriginForStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod102">DoStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"do" <a href="#prod62">Statement</a> "while" "(" <a href="#prod3">Expression</a> ")" ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod103">WhileStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"while" "(" <a href="#prod3">Expression</a> ")" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod104">OriginForStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"for" "(" ( <a href="#prod61">ExpressionNoIn</a> )? ";" ( <a href="#prod3">Expression</a> )? ";" ( <a href="#prod3">Expression</a> )? ")" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod74">ReturnStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"return" ( <a href="#prod3">Expression</a> )? ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod92">FunctionDeclaration</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"function" <a href="#prod4">Identifier</a> ( "(" ( <a href="#prod93">FormalParameterList</a> )? ")" ) <a href="#prod94">FunctionBody</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod14">FunctionExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"function" ( <a href="#prod4">Identifier</a> )? ( "(" ( <a href="#prod93">FormalParameterList</a> )? ")" ) <a href="#prod94">FunctionBody</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod93">FormalParameterList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a> ( "," <a href="#prod4">Identifier</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod94">FunctionBody</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"{" ( <a href="#prod95">SourceElements</a> )? "}"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod96">Program</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod95">SourceElements</a> )? &lt;EOF&gt;</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod95">SourceElements</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod97">SourceElement</a> )+</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod97">SourceElement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod92">FunctionDeclaration</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod98">Name</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">&lt;IDENTIFIER_NAME&gt; ( "." &lt;IDENTIFIER_NAME&gt; )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod101">insertSemiColon</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><i>java code</i></td></tr>
</tbody></table>


</body></html>