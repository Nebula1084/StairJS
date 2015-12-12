#Stair JS
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