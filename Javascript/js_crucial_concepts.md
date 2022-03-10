### The Scope Chain , scope & lexical environment:
----

```js

	function a(){
		console.log(b);
	}

	var b = 10;
	a();
``` 

- **What is scope?**
	 
	 Where you access a specific variable and function.


- **What is a lexical environment?**

Program:

```js

	function a(){
		var b = 10;
		c();
		function c(){

		}
	}

	a();
	console.log(b);

```

*When we try to run this program*,


| **Call stack** 												|	
| :----:														|
|																|
|																|
|																|
|																|
|																|
|																|
|	EC for c()													|
|	EC for a()[created memory for b and c]						|
|	Global Ec is created[created memory for a()]				|

- **What is a Lexical environment?**

	Whenever a execution context is created lexical environment is also created which is basically a local memory along with the lexical memory of the parent. *Lexical means Hirerachy*. Here, c is lexical to a. Whenever a ec created a reference to the lexical environment for the parent is also created in a memory space.

	For global the reference points to null it has no parent code.

- **What is scope chain?**

	This basically the chain formed by the lexical environment for with their parent lexical environment.
	

### Difference between let, var and const:
----

let and const declaration are always hoisted. But they are in a *temporal dead zone*.

- **Let**:

Example:

```js
	console.log(b);
	console.log(a); //throws error
	let a = 10;
	console.log(a); //No error
	var b = 100;

```

- In the above program we can access the variable b Which is undefined due to hoisting. But if we try to console a we have *Reference Error: Cannot access a*.

- In general ***let and const*** are allocated memory in a separate space (script scope). We can't access to let and const before the initialization.

- **What is a temporal dead zone?**

	Time between the *let* variable is hoisted and it got initalized.

- **What is an Reference Error?**

	When we try to access variable which is in a temporal dead zone. And also if we try to access and not defined variable or function.

- **What is an Syntax Error?**

	In general there is an error in syntax. But, here for let it has been throw when we try to redeclare same variables. Due to this error not even a single code will be executed.

	Example:

	```js

		let a = 10;
		let a = 10;

	// Syntax error:Identifier 'a' has already been declared.

	```

- **Const**:

	Here, late initialization is not possible as in *let*. Here, it throws a *Syntax error:Missing initializer in const declaration*. So, it must need to be intialized at the same line of declaration.

- **What is a Type Error?:**




### Block , Scope and shadowing in Js
----

- **What is a block?**

	Block is a combination of statement(or Compound statement ) is the place of Js excepts single statement. Generally, defined with a couple of curly braces.

- **What is a block scope?**

	Variables and functions that we can acess inside the block.

	Example:

	```js

		{
			//Compound statements

			var a = 10;
			let u = 20;
			const s = 30;
		}
	
	```
In the above program, while hoisting u and s are allocated in a *block scope*(a separate space for block) where a is allocated in global scope. We can't access u and s outside the *blockscope*.

- **What is shadowing?**

	If we have two variable of same name outside and inside the block. *The variable inside the block shadows the outside variable and also modifies the value in case of var*.

- **What is illegal shadowing?**

	```js


		//Illegal Shadowing is block: Shadowing let using var

		let a = 20;

		{
			var a = 20;
		}
	
		//Correct Shadowing: Shadowing var using let

		var u = 20;

		{
			let u = 20; 
		}

	```
In the first example the var is crossing the boundary due to global ec. Lexical scoping is followed in block scope also. Scope rules are followed same for the arrow function as for function scope.

### Closures

Program:

```js

	function x(){
		var a = 7;
		function y(){
			console.log(a);
		}

		y();
	}

	x();

```
Lexical scope = closure...???

- **What is Closure??**

	It is means a functions bundles together with the reference to    it's lexical scope.

```js

	function x(){
		var a = 7;
		function y(){
			console.log(a);
		} 

		return y;
	}

	var z = x();
	console.log(z); 
```

Here, the output will be the whole y().

### Important Questions on interview about closures and setTimeOut():
----

```js

	function x(){

		var i = 1;
		setTimeout(function(){
			console.log(i);
		},1000);
		console.log("Namaste Javascript");
	}

	x();
```
 Here, setTimeout function takes the callback function and sets a time to it. When the time got overs it will put the function to the call stack and runs it.

### First Call Funtions
----

- **What is a function statement?**

```js

	function a(){
		console.log("a called");
	}

```

- **What is function expression?**
```js
	
	var b = function(){
		console.log('b called');	
	}
	
``` 

- **What is the difference between function statement and function expression?**

	The main difference between hoisting.

- **What is a anonymous function?**

```js

	//A function statement without a function name. These are used in a space where functions are used as a value.

```

- **What is a first class functions?**

 The ability to use function to use as a value, return a function itself, passing function as a arguments is called first class functions in javascript.


### What is a callback function
----

Passing a function into other function is called *Callback Function*

```js

	setTimeout(()=>{
		console.log("Timer");
	},1000)

	function x(y) {
		console.log("x");
		y();
	}

	x(function y(){
		console.log("y");
	})

```


### Asynchronous and event loop in javascript
----

In generall, Whatever comes in call stack it executes line by line (Synchronous) without any delay. But what if we want to execute something after certain time? Call stack can't do it. It has no *timer* feature. 

In genrall, 

Browser[ Js Engine [ Callstack(code execution inside it) ] ]


- **Web Api's**

 To access all those super powers of the browser.

 Example:

 	1. setTimeout()
 	2. DOM API's
 	3. fetch()
 	4. localstroage
 	5. console.log
 	6. location

These are the things gives access to the powers from the browser, by to the global object(window). Browser give access to the super powers to the Js engine using the *window* keyworkd.

```js

	window.setTimeout(()=>{

	},1000);

```
Since, it(GEC and the web api's) is a global scope we can access it without *window.* keyword.

Example:

```js

	console.log("start");

	setTimeout(function cb(){
		console.log("callback");
	}, 5000);

	console.log("end");
```

1. GEC is created

2. **console.log("start")** = Use the *console* web api(plugged through window object) which makes a call internally to log something in the console.

3. **setTimeout()** = Call the web api and give the timer feature of the web. It registers a callback and starts the timer of 5000ms. It moves to the next line.

4. Again using console web api.

5. Now the timer which is running still runs. But all the code is finished executed, so the GEC will pop up off the call stack. As soon as the timer function is finished.cb need to be executed. But how? as the GEC is popped out. Then it somehow need to come inside the stack. **Now the event loop and callback queue** come to the picture.

	- The cb go to the call stack through the callback queue. The job of the event loop is to check the callstack is empty or not as well as if anything is inside the callback queue. If yes, it then pushes the cb from callback queue to the callstack queue.

- **How event listener works?**

```js

	console.log("start");

	document.getElementById("btn").addEventListener("click", function cb(){
		console.log("callback");
	});

	console.log("end");

```

After GEC created .,

1. Using console web api it prints start.

2. *What is addEventListener?* This is also web api called dom api. This one register a call back and event(which is click) is attached to it. Then it moves on and execute next line.

3. console api to print. No more lines to execute, so GEC is popped.

4. On click, the cb is pushed to callback queue. event loops main job is to see the call stack and callback queue. Here now, cb is pushed to call stack and it inturn exectues it and log it in console.

5. **What is the need of call back queue as a intermediator?**

	Suppose the user clickes it several time the cb will be queued in the callback queue. If the call stack is empty the event loop executes one by one. 


- **How the fetch works?**

```js

	console.log("start");

	setTimeout(function cbT() {
		console.log("CB SetTimeout");
	},5000);

	fetch("https://api.netflix.com").then(function cbF() {
		console.log("CB Netflix");
	});

	console.log("End");

```
After GEC created.,

1. Using console api it log the "start" in console.

2. Using setTimeout api it registers the cbT function in the web api environment and the timer starts from 5000ms. It moves to the next line.

3. fetch = use to make a networks calls. It also registers cbF function to the webapi environment. Once the data getback from the fetch, the cbF will be executed.

- **Microtask queue**
	
	Similar to the callback queue but has higher priority. Whatever comes here executed first.Now what comes inside it? Incase for networks calls and promises cbF goes here, if the callstack is empty eventloop push it to the call back queus.


- **What are microtasks?**

	All the cb functions which comes from promises comes here. Mutation observer goes inside here. Only these two. Other goes to the call back queue(also called Task queue).

- Suppose there are 3 task in microtaks and 1 in callback. If suppose microtask creates sub microtask the callback queue will never get a chance to executed for a long time. this is called as starvation of the task inside callback queue.


#### Js Engine
----

Js can run anywhere because of the JRE(Every Browser has).Which has, node.js has JRE.

1. Js engine(Heart of Js engine)
2. Set of api's
3. callback queue
4. event loop
5. microtask queue

- **Deepdive into JsEngine(Google's V8)**

1. Js engine takes code input,

	1. Parsing:
		1. Code is broken down into tokens.
		2. (ASTEXPLORE.NET)Syntax Parser: take the code -> AST(Abstract Syntax Tree)
	
	2. Compilation:
		Javascript has JIT or(AOT) compilation(compiler + interpretter). 
			- What is the differrence between interpretter?
				Takes the code and starts executing line by line
			- What is compiler?
				take code -> form optimized code -> output	
		1. AST is goes to the interpretter. Compiler also tries to optimize code on the run time.
	3. Execution
		1. Line comes from the interpretter executed hand in hand.
		2. It is not possible without memroy heap and call stack. In memory heap all memory is stored.
		3. Garbage collector(mark and sweep algorithm): used to free the memory.
		4. Inline caching
		5.  copy elision
		6. inlining

### setTimeout - trust issues
----
It may not take exact 5ms time to execute. Concurrency model?
How to block the main thread? to execute it directly for the setted time?

```js

	console.log("Start");

	setTimeout(function cb() {
		console.log("Call back");
	},5000);

	console.log("End");

//million
	
	let startDate = new Date().getTime();
	let endDate = startDate;
	while(endDate<=(startDate+500000)){
		endDate = new Date().getTime();
	}

	console.log("While expires");


	//Output:
		// start
		// end
		// while expires
		// call back



```















