#### Target Group Attributes
1. deregistration_delay.timeout_seconds
2. slow_start.duration_seconds
	- It gives targets time to warm-up before the load balancer sends them a full share of requests.
	- exists when duration periods elapses
3. load_balancing.algoirthm.type
	- Least Outstanding Request = Less busy instance get the next request [ ALB, CLB ]
	- Round Robin = Equally choose the targets [ ALP , CLB ]
	- Flow Hash = Target based on the hash of protocol, Ip etc, and the target will last for the life of the connection [ NLB ]
1. stickiness.enabled
2. stickiness.app_cookie.cookie_name
3. stickiness.app_cookie.duration_seconds

#### ALB Rules
1. Process in order
2. Support action = forward, redirect, fixed-response
3. Rule Conditions:
	- host-header
	- http-request-method
	- path-pattern
	- source-ip
	- http-header
	- query-string
4. Target Group Weighting = give weights for the target group for the single rule, this allows you to control the distribution of the traffic to your applications [ blue/green deployment ]
#### Auto Scaling Groups
1. The goal is to scale out and scale in to match the loads. Have min , desired and max ec2 running
2. Free of cost only pay for ec2
##### ASG Attributes
1. Need to create Launch Template
2. Cloud Watch Alarms and Scaling = used to scale asg based on this
#### Dynamic Scaling Policies
##### Target Tracking Scaling
1. Want to maintain in a target state
##### Simple/Step Scaling
1. Trigger a action if the target state changes
##### Scheduled Actions
1. Schedule the scaling on the particular day 
#### Predictive Scaling
1. Forecast load and schedule scaling ahead
2. Good metrics to scale on = CPU Utilisation, RequestCountPerTarget, Average Network In/Out, Any custom metric using cloud watch agent
3. Scaling Cooldowns = cooldown period for launch/terminate instance, default ( 300 seconds ) during this asg won't launch or terminate instances. Always use ready to use AMI
#### Life Cycle Hooks [ SysOps ]
1. Hook a life cycle to a ASG
2. By default it it goes from pending to InService. You can also add some steps in between these states. Also actions before termination of the instance.
3. UseCase: cleanup, log extraction, special health Checks
4. Launch Configuration VS Launch Template = You can't edit once created so u can use the versioning systems
5. SQS with Auto Scaling = CloudWatch Metric ( Queue Length) -> SQS queue msg large -> trigger alarm -> auto scale 
6. Health checks = 2 instance across 2 AZ for high availability
	1. Ec2 status Checks
	2. Ec2 Health Checks
	3. Custom Health Checks = using CLI or SDK
	4. ASG won't reboot unhealthy hosts
#### Troubleshooting ASG issues
1. can't launch instance in asg = max capacity for asg or az in reached
2. asg suspends if the instances can't launch in 24 hrs
3. key/sg not exist if the instance is not launching
4. Metrics collected every 1 min ( asg should be opt in) / for ec2 it is default for 5 min and granularity 1 min
#### Overview  
1. Auto scaling group
2. Spot fleet request
3. ECS
4. DynamoDB
5. Aurora



