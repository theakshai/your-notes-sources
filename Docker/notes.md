*What is problem does docker is trying to solve?*
 	
	Previously it was like one app for one server. VM's solves this problem, but this needs a separate os and resources.
	Running your applications in same operating systems => containers

*What is the container vs vm?*

	vm runs on top of hypervisor and container runs on top of container engine.

**What is docker runtime**?

	orchestation
	    |
	Engine
	    |
	    Runtime

Runtime:
	Allow us to start and stop the container.
	Two types:
		1. run c
		2. conatiner d

Engine:
	Docker CLI -> Rest API -> Server, daemon ( Which communicates with run time )

Orchestration:

	It is used in the production and rool out and managing containers

Container Image: Image of the application ( Instruction to make the application ).

	Dockerfile (Used to create a Image )  -> Image -> Conatiner ( Running image )

What is Devops:

	Application -> Creating a container. 


Docker run Hello World:
	
	run => running an image to create a container.

Docker run Image-name

What is inside the image?
	The container also contains the os.( Smaller version )
