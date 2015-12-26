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
<td align="LEFT" valign="BASELINE">( "(" <a href="#prod61">ExpressionNoIn</a> ")" )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "(" <a href="#prod3">ExpressionNoIn</a> ")" )</td>
</tr> -->
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
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod14">FunctionExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod6">Literal</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">&lt;DECIMAL_INTEGER_LITERAL&gt; 
    | &lt;HEX_INTEGER_LITERAL&gt; 
    | &lt;FLOAT_LITERAL&gt; 
    | &lt;STRING_LITERAL&gt; 
    | &lt;BOOLEAN_LITERAL&gt; 
    | NULL </td>
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
<td align="LEFT" valign="BASELINE">( <a href="#prod59">AssignmentExpressionNoIn</a> )? ( "," ( <a href="#prod59">AssignmentExpressionNoIn</a> )?  )*</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod5">ArrayLiteral</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"[" ( ( <a href="#prod7">Elision</a> )? "]" | <a href="#prod8">ElementList</a> <a href="#prod7">Elision</a> "]" | ( <a href="#prod8">ElementList</a> )? "]" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod8">ElementList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod7">Elision</a> )? <a href="#prod9">AssignmentExpression</a> ( <a href="#prod7">Elision</a> <a href="#prod9">AssignmentExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod7">Elision</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "," )+</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod2">ObjectLiteral</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"{" ( <a href="#prod10">PropertyNameAndValueList</a> )? "}"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod10">PropertyNameAndValueList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod11">PropertyNameAndValue</a> ( "," <a href="#prod11">PropertyNameAndValue</a> )*</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod10">PropertyNameAndValueList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod11">PropertyNameAndValue</a> ( "," <a href="#prod11">PropertyNameAndValue</a> | "," )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod11">PropertyNameAndValue</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod12">PropertyName</a> ":" <a href="#prod59">AssignmentExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod12">PropertyName</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">&lt;DECIMAL_INTEGER_LITERAL&gt; </td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">&lt;HEX_INTEGER_LITERAL&gt; </td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">&lt;FLOAT_LITERAL&gt; </td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod13">MemberExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod1">PrimaryExpression</a><td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod16">AllocationExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod13">MemberExpression</a> <a href="#prod15">MemberExpressionPart</a> )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod17">MemberExpressionForIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( ( <a href="#prod14">FunctionExpression</a> | <a href="#prod1">PrimaryExpression</a> ) ( <a href="#prod15">MemberExpressionPart</a> )* )</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod16">AllocationExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"new" <a href="#prod13">MemberExpression</a> <a href="#prod18">Arguments</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod15">MemberExpressionPart</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "[" <a href="#prod61">ExpressionNoIn</a> "]" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "." <a href="#prod4">Identifier</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod19">CallExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod13">MemberExpression</a> <a href="#prod18">Arguments</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod19">CallExpression</a> <a href="#prod20">CallExpressionPart</a> )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod21">CallExpressionForIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod17">MemberExpressionForIn</a> <a href="#prod18">Arguments</a> ( <a href="#prod20">CallExpressionPart</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod20">CallExpressionPart</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod18">Arguments</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "[" <a href="#prod61">ExpressionNoIn</a> "]" )</td>
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
<td align="LEFT" valign="BASELINE"><a href="#prod59">AssignmentExpressionNoIn</a> ( "," <a href="#prod59">AssignmentExpressionNoIn</a> )*</td>
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
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod24">LeftHandSideExpressionForIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod21">CallExpressionForIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod17">MemberExpressionForIn</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod25">PostfixExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod23">LeftHandSideExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod25">PostfixExpression</a> <a href="#prod26">PostfixOperator</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod26">PostfixOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "++" | "--" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod27">UnaryExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod25">PostfixExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod28">UnaryOperator</a> <a href="#prod27">UnaryExpression</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod28">UnaryOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "delete" | "void" | "typeof" | "++" | "--" | "+" | "-" | "~" | "!" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod29">MultiplicativeExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod27">UnaryExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod29">MultiplicativeExpression</a> <a href="#prod30">MultiplicativeOperator</a> <a href="#prod27">UnaryExpression</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod30">MultiplicativeOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "*" | "/" | "%" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod31">AdditiveExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod29">MultiplicativeExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod31">AdditiveExpression</a> <a href="#prod32">AdditiveOperator</a> <a href="#prod29">MultiplicativeExpression</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod32">AdditiveOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "+" | "-" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod33">ShiftExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod31">AdditiveExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod33">ShiftExpression</a> <a href="#prod34">ShiftOperator</a> <a href="#prod31">AdditiveExpression</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod34">ShiftOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "&lt;&lt;" | "&gt;&gt;" | "&gt;&gt;&gt;" )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod35">RelationalExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod33">ShiftExpression</a> ( <a href="#prod36">RelationalOperator</a> <a href="#prod33">ShiftExpression</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod36">RelationalOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "&lt;" | "&gt;" | "&lt;=" | "&gt;=" | "instanceof" | "in" )</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod37">RelationalExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod33">ShiftExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod37">RelationalExpressionNoIn</a> <a href="#prod38">RelationalNoInOperator</a> <a href="#prod33">ShiftExpression</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod38">RelationalNoInOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "&lt;" | "&gt;" | "&lt;=" | "&gt;=" | "instanceof" )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod39">EqualityExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod35">RelationalExpression</a> ( <a href="#prod40">EqualityOperator</a> <a href="#prod35">RelationalExpression</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod41">EqualityExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod37">RelationalExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod41">EqualityExpressionNoIn</a> <a href="#prod40">EqualityOperator</a> <a href="#prod37">RelationalExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod40">EqualityOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "==" | "!=" | "===" | "!==" )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod42">BitwiseANDExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod39">EqualityExpression</a> ( <a href="#prod43">BitwiseANDOperator</a> <a href="#prod39">EqualityExpression</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod44">BitwiseANDExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod41">EqualityExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod44">BitwiseANDExpressionNoIn</a> <a href="#prod43">BitwiseANDOperator</a> <a href="#prod41">EqualityExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod43">BitwiseANDOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"&amp;"</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod45">BitwiseXORExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod42">BitwiseANDExpression</a> ( <a href="#prod46">BitwiseXOROperator</a> <a href="#prod42">BitwiseANDExpression</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod47">BitwiseXORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod44">BitwiseANDExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod47">BitwiseXORExpressionNoIn</a> <a href="#prod46">BitwiseXOROperator</a> <a href="#prod44">BitwiseANDExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod46">BitwiseXOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"^"</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod48">BitwiseORExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod45">BitwiseXORExpression</a> ( <a href="#prod49">BitwiseOROperator</a> <a href="#prod45">BitwiseXORExpression</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod50">BitwiseORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod47">BitwiseXORExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod50">BitwiseORExpressionNoIn</a> <a href="#prod49">BitwiseOROperator</a> <a href="#prod47">BitwiseXORExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod49">BitwiseOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"|"</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod51">LogicalANDExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod48">BitwiseORExpression</a> ( <a href="#prod52">LogicalANDOperator</a> <a href="#prod48">BitwiseORExpression</a> )*</td>
</tr> -->

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod53">LogicalANDExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod50">BitwiseORExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod53">LogicalANDExpressionNoIn</a> <a href="#prod52">LogicalANDOperator</a> <a href="#prod50">BitwiseORExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod52">LogicalANDOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"&amp;&amp;"</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod54">LogicalORExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod51">LogicalANDExpression</a> ( <a href="#prod55">LogicalOROperator</a> <a href="#prod51">LogicalANDExpression</a> )*</td>
</tr> -->
<tr>

<td align="RIGHT" valign="BASELINE"><a name="prod56">LogicalORExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod53">LogicalANDExpressionNoIn</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod56">LogicalORExpressionNoIn</a> <a href="#prod55">LogicalOROperator</a> <a href="#prod53">LogicalANDExpressionNoIn</a></td>
</tr>

<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod55">LogicalOROperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"||"</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod57">ConditionalExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod54">LogicalORExpression</a> ( "?" <a href="#prod9">AssignmentExpression</a> ":" <a href="#prod9">AssignmentExpression</a> )?</td>
</tr> -->
<!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod58">ConditionalExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod56">LogicalORExpressionNoIn</a> ( "?" <a href="#prod9">AssignmentExpression</a> ":" <a href="#prod59">AssignmentExpressionNoIn</a> )?</td>
</tr> -->
<!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod9">AssignmentExpression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod23">LeftHandSideExpression</a> <a href="#prod60">AssignmentOperator</a> <a href="#prod9">AssignmentExpression</a> | <a href="#prod57">ConditionalExpression</a> )</td>
</tr> -->
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
<!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod59">AssignmentExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod23">LeftHandSideExpression</a> <a href="#prod60">AssignmentOperator</a> <a href="#prod59">AssignmentExpressionNoIn</a> | <a href="#prod58">ConditionalExpressionNoIn</a> )</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod60">AssignmentOperator</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "=" | "*=" | "/=" | "%=" | "+=" | "-=" | "&lt;&lt;=" | "&gt;&gt;=" | "&gt;&gt;&gt;=" | "&amp;=" | "^=" | "|=" )</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod3">Expression</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod9">AssignmentExpression</a> ( "," <a href="#prod9">AssignmentExpression</a> )*</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod61">ExpressionNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod59">AssignmentExpressionNoIn</a> ( "," <a href="#prod59">AssignmentExpressionNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod62">Statement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod63">Block</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod64">JScriptVarStatement</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod65">VariableStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod66">EmptyStatement</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod67">LabelledStatement</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod68">ExpressionNoInStatement</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod68">ExpressionStatement</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod69">IfStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod70">IterationStatement</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod71">ContinueStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod72">BreakStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod73">ImportStatement</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod74">ReturnStatement</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod75">WithStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod76">SwitchStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod77">ThrowStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod78">TryStatement</a></td>
</tr> -->
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
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod65">VariableStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"var" <a href="#prod80">VariableDeclarationList</a> ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod80">VariableDeclarationList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod81">VariableDeclaration</a> ( "," <a href="#prod81">VariableDeclaration</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod82">VariableDeclarationListNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod83">VariableDeclarationNoIn</a> ( "," <a href="#prod83">VariableDeclarationNoIn</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod81">VariableDeclaration</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a> ( <a href="#prod84">Initialiser</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod83">VariableDeclarationNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a> ( <a href="#prod85">InitialiserNoIn</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod84">Initialiser</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"=" <a href="#prod9">AssignmentExpression</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod85">InitialiserNoIn</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"=" <a href="#prod59">AssignmentExpressionNoIn</a></td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod66">EmptyStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">";"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod68">ExpressionNoInStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod61">ExpressionNoIn</a> ( ";" )?</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod68">ExpressionStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod61">ExpressionNoIn</a> ( ";" )?</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod69">IfStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"if" "(" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a> ( "else" <a href="#prod62">Statement</a> )?</td>
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
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod105">ForEachStatement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod102">DoStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"do" <a href="#prod62">Statement</a> "while" "(" <a href="#prod61">ExpressionNoIn</a> ")" ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod103">WhileStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"while" "(" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod104">OriginForStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"for" "(" <a href="#prod61">ExpressionNoIn</a>  ";" <a href="#prod61">ExpressionNoIn</a> ";" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod105">ForEachStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"for" "(" "var" <a href="#prod4">Identifier</a> "in" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a></td>
</tr>
<!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod70">IterationStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( "do" <a href="#prod62">Statement</a> "while" "(" <a href="#prod61">ExpressionNoIn</a> ")" ( ";" )? )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "while" "(" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "for" "(" ( <a href="#prod61">ExpressionNoIn</a> )? ";" ( <a href="#prod61">ExpressionNoIn</a> )? ";" ( <a href="#prod61">ExpressionNoIn</a> )? ")" <a href="#prod62">Statement</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "for" "(" "var" <a href="#prod80">VariableDeclarationList</a> ";" ( <a href="#prod61">ExpressionNoIn</a> )? ";" ( <a href="#prod61">ExpressionNoIn</a> )? ")" <a href="#prod62">Statement</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "for" "(" "var" <a href="#prod83">VariableDeclarationNoIn</a> "in" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a> )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE">( "for" "(" <a href="#prod24">LeftHandSideExpressionForIn</a> "in" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a> )</td>
</tr> -->
<!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod71">ContinueStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"continue" ( <a href="#prod4">Identifier</a> )? ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod72">BreakStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"break" ( <a href="#prod4">Identifier</a> )? ( ";" )?</td>
</tr> -->
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod74">ReturnStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"return" ( <a href="#prod61">ExpressionNoIn</a> )? ( ";" )?</td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod75">WithStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"with" "(" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod76">SwitchStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"switch" "(" <a href="#prod61">ExpressionNoIn</a> ")" <a href="#prod86">CaseBlock</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod86">CaseBlock</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"{" ( <a href="#prod87">CaseClauses</a> )? ( "}" | <a href="#prod88">DefaultClause</a> ( <a href="#prod87">CaseClauses</a> )? "}" )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod87">CaseClauses</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( <a href="#prod89">CaseClause</a> )+</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod89">CaseClause</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( ( "case" <a href="#prod61">ExpressionNoIn</a> ":" ) ) ( <a href="#prod79">StatementList</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod88">DefaultClause</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">( ( "default" ":" ) ) ( <a href="#prod79">StatementList</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod67">LabelledStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a> ":" <a href="#prod62">Statement</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod77">ThrowStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"throw" <a href="#prod61">ExpressionNoIn</a> ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod78">TryStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"try" <a href="#prod63">Block</a> ( ( <a href="#prod90">Finally</a> | <a href="#prod91">Catch</a> ( <a href="#prod90">Finally</a> )? ) )</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod91">Catch</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"catch" "(" <a href="#prod4">Identifier</a> ")" <a href="#prod63">Block</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod90">Finally</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"finally" <a href="#prod63">Block</a></td>
</tr> -->
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
<td align="LEFT" valign="BASELINE"><a href="#prod62">Statement</a></td>
</tr><!-- 
<tr>
<td align="RIGHT" valign="BASELINE"></td>
<td align="CENTER" valign="BASELINE">|</td>
<td align="LEFT" valign="BASELINE"><a href="#prod92">FunctionDeclaration</a></td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod73">ImportStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"import" <a href="#prod98">Name</a> ( "." "*" )? ";"</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod98">Name</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">&lt;IDENTIFIER_NAME&gt; ( "." &lt;IDENTIFIER_NAME&gt; )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod64">JScriptVarStatement</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE">"var" <a href="#prod99">JScriptVarDeclarationList</a> ( ";" )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod99">JScriptVarDeclarationList</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod100">JScriptVarDeclaration</a> ( "," <a href="#prod100">JScriptVarDeclaration</a> )*</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod100">JScriptVarDeclaration</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><a href="#prod4">Identifier</a> ":" &lt;IDENTIFIER_NAME&gt; ( <a href="#prod84">Initialiser</a> )?</td>
</tr>
<tr>
<td align="RIGHT" valign="BASELINE"><a name="prod101">insertSemiColon</a></td>
<td align="CENTER" valign="BASELINE">::=</td>
<td align="LEFT" valign="BASELINE"><i>java code</i></td>
</tr> -->
</tbody>
</table>


</body></html>