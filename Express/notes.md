##### Routing:

[Documentation Reference]:https://expressjs.com/en/guide/routing.html

Decides how an application should respond when a client request a certain endpoint. In express, it is achieved by app object.

```js
	const app = express();
	app.get()
	app.post()
	app.delete()
	app.patch()
	app.all() => when we have more than one method defined for a certain route.

```

#### Writing Middleware:



[Documentation Reference]:https://expressjs.com/en/guide/writing-middleware.html

Basically a function that have access to the req and res object and the next function. It can execute any code, make changes to req and res object, end the req-res cycle and call the next middleware in the stack.

```js

	const express = require('express');

