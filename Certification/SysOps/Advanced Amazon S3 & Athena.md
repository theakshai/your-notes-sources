##### Lifecycle Rules
- Transition Actions
- Expiration Actions
- S3 analytics/storage class analysis [ only for standard and standard - IA ]
##### S3 Event Notification
1. All the events for s3 you can image for 
2. Advanced Filtering options, multiple destinations and eventbridge capabilities
##### Baseline Performance
- auto scale to high request rate 100-200ms
- at least 3500 or 5500 (get/head) / request/s/per prefix
- Multi part upload = user files > 100 mb, must for > 5gb, can parallelise uploads
- S3 Transfer Acceleration = increase transfer speed to an AWS edge location
- S3 Byte-Range Fetches = Parallelise get's, better resilience in case of failures, can used to retrieve only partial data
##### S3 select and glacier select
- Retrieve less data using sql using server-side filtering
- less network transfer, less cpu cost client-side
##### S3 Batch Operation
- Perform bulk operations in existing s3 objects with a single request
##### S3 Inventory
- list objects and their corresponding metadata
- can used to = audit and report, get no of objects and total storage
- outputs = csv, orc or apache parquet