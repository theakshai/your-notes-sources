## "Explains about Contexting,hoisting in javascript"
----

- **How javascript works:**
----

- Everything in Js happens inside *Execution Context.*

	| Memory (Variable environment) | Code (Thread of execution) 			|
	| :---:							|   :---:								|
	| Stored as Key:value pairs     | Execute the code one line at a time	|

	- Javascript is a sync , single threaded language  -> executing code one line at a time after execution the previous line is finished.

- **How javascript code is executed:**
----

Here we will see how the Execution context is works.

**Js Code:**
```js
var n = 2;

function square(num){
	var ans = num*num;
	return ans;
	}

var square2 = square(n);
var square4 = square(4);

	
```

When we run this code, a global execution context is created,

Execution is context is created in two phase:

1.**Memory creation Phase:**  Js allocates memory to all variables and function.

2.**Code execution Phase:**  Executed the code line by line.

Here,


| **Memory** (First Phase)											|		**Code Execution** (Second Phase) 	|
| :---:																|		:---:								|
| ***n***:undefined(spacial value) at first							|	***n***: 2 is allocated	in memory space.
| ***square***:stores a whole code at first							|		Brand new execution context created inside this when a function is executed |
| ***square2***: undefined											|		returns the value of square2 in memory space.		|
| ***square4***: undefined											|		Brand new execution context created inside this when a function is executed|

----

**Execution phase of Function**

| **Memory**	|	**Code execution** 	|
| :----:			|		:----: 		|
| ***num***: undefined		|	2 is passed into the num				|
| ***ans***: undefined		|	Do the calculation and put into the ans memory space|
|							|	**return** keyword tells the return the control of the program back to the execution context where the function was invoked.|
 
**Note:** It will be deleted after the return statement. The Execution environment will form whenver function invocation happens.


**How this manage all the execution context(creation,deletion)?**

It has it's own ***class stack***. Call stack is a general stack. When ever a new Execution stack is need to create a new Execution context will be *pushed* into a stack. After it executed it will be *poped* from the stack the control goes back to the Global execution context. It maintains the order of execution of execution of contexts.

| **Call stack** 									|
|	:---:		 									|
|							-						|
|							-						|
|							-						|
|							-						|
|							-						|
| E2(Execution Context in case of call back funtion)|
| E1(Execution Context) 							|
| Global execution context 							|


- **Hoisting in Javascript:**
----	

In javascript the below code will work just fine:

**Js code:**

```js
hoisting();

function hoisting():
	console.log("Hoisting in fun");
```

**What is hoisting:**

Hoisting is phenomenon is js where accessing function and variable before intialized it without any error.
 It happens due to this the execution context where cause of the memory phase of the execution context

**What happens when we write a call-back function?**
```js
	
	var getName = () => {
		console.log("Namaste Javascript");
	}

	Or

	var getName = function (){
		console.log("hello World");
	}
```
It will allocated same as *'undefined'*

- **Function invocation and variable environment:**
----

**Js code:**

```js

var x = 1;
a();
b(); 
console.log(x);

	function a(){
		var x = 10;
		console.log(x);
	}

	function b(){
		var x = 100;
		console.log(x);
	}

```

The execution context will follow the same method as follows. But here we have *'x = 10'* within a function. Here, it will have it's own value for *'x'*. During the *console.log(x)* in the function js search for the value of x in local memory and logs it to console.

- **What happens when we run a empty js file?**

	It will still create a global execution context. It will also create *window* object and *this* keyword. All these are created by Js Engine.
		
	- ***What is window object?***

	Whenever a Global execution context (Function context also) created it will also create *this* keyword along with it. At global level this points to window. Whatever we create in global space it will attach to the window object.


- **What is the difference between undefined and not defined?**
----

Even before a line executed in code, Js will alocate a memory space for the variable. Undefined is a space holder in the memory space for the variable.
**Note:** undefined != empty. 