
- Bucket = top level directories
- files = objects in bucket\
- Must have a unique name across globe
- buckets are regioned service
- 3-63 chars, no_uppercase, no_underscore, not_an_ip, not start with xn-- and end with -s3alias
- 403 error bucket policy not allows public reads
##### Objects
- files have key
- key is a full path [ prefix + object_name ]
- values are the content of the body
- Max is 5TB
- To upload a big file u should upload as a multi-part upload
- Metadata- kv pairs
- Tags
- Version_Id
##### Bucket Policy
- User-Based = IAM Policies
- Resource-Based = Bucket Policies, Object / Bucket Access Control List
- Encrypting objects in S3
- Force objects to upload encrypted ( s3: x-amz-server-side-encryption)
- aws:PrincipalOrgId
- NotIpAddress
##### JSON
- Effect, Actions, Principal, Resources
##### S3 versioning
- bucket level
- Protect against unintended  deletes ( how it is doing it )
- null version
- once deleted ( delete marker type )
##### S3 Replication
- CRR = Cross region replication
- SRR = Same region replication
- Must enable versioning
- Buckets can be in different AWS
- Copying is async
- Use case = CRR [ compliance, lower latency]
- Only new objects will be replicated
- To replicate the old use s3 batch replication
- No chaining of replication
##### S3 Storage Class [ Refer Docs ]

