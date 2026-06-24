# Understanding AWS (Amazon Web Services)

## What is AWS?

Amazon Web Services (AWS) is a comprehensive cloud computing platform offered by Amazon. It provides on-demand access to computing resources — servers, storage, databases, networking, analytics, AI/ML, and more — over the internet, with pay-as-you-go pricing.

---

## Core Concepts

### Cloud Computing Models

| Model | Description | Example |
|-------|-------------|---------|
| **IaaS** | Infrastructure as a Service — raw compute, storage, networking | EC2, S3, VPC |
| **PaaS** | Platform as a Service — managed runtime/environment | Elastic Beanstalk, RDS |
| **SaaS** | Software as a Service — fully managed applications | WorkMail, Chime |

### Deployment Models

- **Public Cloud** — Resources hosted on AWS infrastructure, shared across customers
- **Private Cloud** — Dedicated environment for a single organization
- **Hybrid Cloud** — Mix of on-premises and AWS cloud resources

---

## AWS Global Infrastructure

### Regions
- Geographic locations around the world (e.g., `us-east-1`, `ap-south-1`)
- Each region is isolated and contains multiple Availability Zones
- Choose a region based on latency, compliance, and service availability

### Availability Zones (AZs)
- Physically separate data centers within a region
- Connected via low-latency, high-bandwidth links
- Deploying across AZs ensures high availability and fault tolerance

### Edge Locations
- Used by CloudFront (CDN) to cache content closer to users
- Reduces latency for global users

---

## Key AWS Services

### Compute

| Service | Description |
|---------|-------------|
| **EC2** (Elastic Compute Cloud) | Virtual machines (instances) in the cloud |
| **Lambda** | Serverless functions — run code without managing servers |
| **ECS / EKS** | Container orchestration (Docker / Kubernetes) |
| **Elastic Beanstalk** | PaaS — deploy web apps without managing infrastructure |
| **Lightsail** | Simple VPS for small workloads |

### Storage

| Service | Description |
|---------|-------------|
| **S3** (Simple Storage Service) | Object storage — scalable, durable, web-accessible |
| **EBS** (Elastic Block Store) | Persistent block storage attached to EC2 |
| **EFS** (Elastic File System) | Managed NFS file system shared across instances |
| **Glacier / S3 Glacier** | Low-cost archival storage |
| **Storage Gateway** | Hybrid storage between on-premises and AWS |

### Databases

| Service | Description |
|---------|-------------|
| **RDS** | Managed relational DB (MySQL, PostgreSQL, Oracle, SQL Server) |
| **Aurora** | AWS-optimized relational DB (MySQL/PostgreSQL compatible) |
| **DynamoDB** | Fully managed NoSQL key-value and document database |
| **ElastiCache** | In-memory caching (Redis / Memcached) |
| **Redshift** | Data warehousing and analytics |
| **DocumentDB** | MongoDB-compatible document database |

### Networking

| Service | Description |
|---------|-------------|
| **VPC** (Virtual Private Cloud) | Isolated virtual network within AWS |
| **Route 53** | Scalable DNS and domain registration |
| **CloudFront** | Content Delivery Network (CDN) |
| **ELB** (Elastic Load Balancing) | Distribute traffic across instances |
| **API Gateway** | Create, publish, and manage REST/WebSocket APIs |
| **Direct Connect** | Dedicated private connection from on-premises to AWS |

### Security & Identity

| Service | Description |
|---------|-------------|
| **IAM** (Identity and Access Management) | Users, roles, policies, and permissions |
| **KMS** (Key Management Service) | Create and manage encryption keys |
| **Secrets Manager** | Store and rotate secrets securely |
| **WAF** | Web Application Firewall |
| **Shield** | DDoS protection |
| **GuardDuty** | Threat detection and monitoring |
| **Inspector** | Automated security assessments |

### Monitoring & Management

| Service | Description |
|---------|-------------|
| **CloudWatch** | Metrics, logs, alarms, and dashboards |
| **CloudTrail** | Audit log of all API calls |
| **Config** | Track configuration changes over time |
| **Systems Manager** | Operational management of AWS resources |
| **Trusted Advisor** | Best practices recommendations |
| **Cost Explorer** | Visualize and analyze AWS costs |

### Developer Tools

| Service | Description |
|---------|-------------|
| **CodeCommit** | Git-based source control |
| **CodeBuild** | CI build service |
| **CodeDeploy** | Automated deployment |
| **CodePipeline** | End-to-end CI/CD pipeline |
| **CloudFormation** | Infrastructure as Code (IaC) using templates |
| **CDK** (Cloud Development Kit) | Define infrastructure using code (Python, TypeScript, etc.) |

### AI / ML

| Service | Description |
|---------|-------------|
| **SageMaker** | Build, train, and deploy ML models |
| **Rekognition** | Image and video analysis |
| **Comprehend** | Natural language processing (NLP) |
| **Polly** | Text-to-speech |
| **Transcribe** | Speech-to-text |
| **Bedrock** | Access foundation models (FMs) via API |

---

## IAM — Identity and Access Management

IAM controls who can do what in your AWS account.

### Key Components

- **Users** — Individual identities (people or services)
- **Groups** — Collection of users with shared permissions
- **Roles** — Temporary permissions assumed by services or users
- **Policies** — JSON documents defining allowed/denied actions

### Example IAM Policy

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject"],
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

### Best Practices

- Follow the **Principle of Least Privilege** — grant only what's needed
- Enable **MFA** for all users, especially root
- Never use root account for day-to-day operations
- Use **IAM Roles** for EC2, Lambda, and other services instead of embedding credentials
- Rotate access keys regularly

---

## VPC — Virtual Private Cloud

A VPC is your own isolated network within AWS.

```
VPC (10.0.0.0/16)
├── Public Subnet (10.0.1.0/24)   → Internet Gateway → Internet
│     └── EC2 (Web Server)
└── Private Subnet (10.0.2.0/24)  → NAT Gateway → Internet (outbound only)
      └── RDS (Database)
```

### Key Components

- **Subnets** — Divide VPC into public/private segments
- **Internet Gateway** — Allows public subnet traffic to reach the internet
- **NAT Gateway** — Allows private subnet outbound internet access
- **Route Tables** — Control traffic routing within VPC
- **Security Groups** — Stateful firewall at the instance level
- **NACLs** — Stateless firewall at the subnet level

---

## EC2 — Elastic Compute Cloud

EC2 provides resizable virtual machines (instances).

### Instance Types

| Family | Use Case |
|--------|----------|
| `t3`, `t4g` | General purpose, burstable (web servers, dev) |
| `m5`, `m6i` | General purpose, balanced (app servers) |
| `c5`, `c6i` | Compute optimized (batch processing, gaming) |
| `r5`, `r6i` | Memory optimized (databases, caches) |
| `p3`, `p4` | GPU instances (ML training) |
| `i3`, `i4i` | Storage optimized (NoSQL, data warehousing) |

### Pricing Models

| Model | Best For |
|-------|----------|
| **On-Demand** | Unpredictable workloads, short-term |
| **Reserved** (1 or 3 yr) | Steady-state workloads — up to 72% savings |
| **Spot** | Fault-tolerant, flexible workloads — up to 90% savings |
| **Savings Plans** | Flexible commitment-based discount |
| **Dedicated Host** | Compliance or licensing requirements |

---

## S3 — Simple Storage Service

S3 is object storage designed for durability (99.999999999% — "11 nines").

### Storage Classes

| Class | Use Case |
|-------|----------|
| **S3 Standard** | Frequently accessed data |
| **S3 Intelligent-Tiering** | Unknown or changing access patterns |
| **S3 Standard-IA** | Infrequently accessed, rapid retrieval |
| **S3 One Zone-IA** | Non-critical, infrequently accessed |
| **S3 Glacier Instant** | Archive with millisecond retrieval |
| **S3 Glacier Flexible** | Archive, retrieval in minutes to hours |
| **S3 Glacier Deep Archive** | Lowest cost, retrieval in hours |

### Key Features

- **Versioning** — Keep multiple versions of objects
- **Lifecycle Policies** — Automatically transition or expire objects
- **Replication** — Cross-region or same-region replication
- **Bucket Policies** — Resource-based access control
- **Encryption** — SSE-S3, SSE-KMS, or SSE-C

---

## Serverless with Lambda

AWS Lambda runs code in response to events without provisioning servers.

```python
import json

def lambda_handler(event, context):
    name = event.get("name", "World")
    return {
        "statusCode": 200,
        "body": json.dumps(f"Hello, {name}!")
    }
```

### Key Concepts

- **Trigger** — What invokes the function (API Gateway, S3, DynamoDB, etc.)
- **Runtime** — Python, Node.js, Java, Go, .NET, Ruby, custom
- **Execution Role** — IAM role granting permissions to the function
- **Timeout** — Max 15 minutes per invocation
- **Memory** — 128 MB to 10,240 MB

---

## AWS Well-Architected Framework

AWS defines 6 pillars for building reliable, secure, and efficient systems:

| Pillar | Focus |
|--------|-------|
| **Operational Excellence** | Automate, iterate, learn from failures |
| **Security** | Protect data, systems, and assets |
| **Reliability** | Recover from failures, meet demand |
| **Performance Efficiency** | Use resources efficiently |
| **Cost Optimization** | Avoid unnecessary spend |
| **Sustainability** | Minimize environmental impact |

---

## Shared Responsibility Model

AWS and the customer share security responsibilities:

```
┌─────────────────────────────────────────────────┐
│              CUSTOMER RESPONSIBILITY             │
│  - Data encryption & integrity                  │
│  - Application security                         │
│  - Identity & access management (IAM)           │
│  - OS patching (for EC2)                        │
│  - Network & firewall configuration             │
└─────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────┐
│                AWS RESPONSIBILITY                │
│  - Physical hardware & data centers             │
│  - Hypervisor & virtualization layer            │
│  - Managed service infrastructure               │
│  - Global network infrastructure                │
└─────────────────────────────────────────────────┘
```

---

## Common Architecture Patterns

### Three-Tier Web Application

```
Internet
   │
   ▼
CloudFront (CDN)
   │
   ▼
Application Load Balancer
   │
   ▼
EC2 / ECS (App Layer) — Auto Scaling Group
   │
   ▼
RDS (Database Layer) — Multi-AZ
```

### Serverless API

```
Client → API Gateway → Lambda → DynamoDB
                            └──→ S3
```

### Event-Driven Architecture

```
S3 Upload → S3 Event → Lambda → SQS → Lambda → DynamoDB
                             └──→ SNS → Email/SMS
```

---

## Useful AWS CLI Commands

```bash
# Configure AWS CLI
aws configure

# List S3 buckets
aws s3 ls

# Copy file to S3
aws s3 cp file.txt s3://my-bucket/

# List EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,State.Name]' --output table

# Invoke Lambda function
aws lambda invoke --function-name my-function --payload '{"key":"value"}' output.json

# Get CloudWatch logs
aws logs get-log-events --log-group-name /aws/lambda/my-function --log-stream-name latest
```

---

## Cost Management Tips

1. **Right-size instances** — Use CloudWatch metrics to identify over-provisioned resources
2. **Use Reserved Instances or Savings Plans** for predictable workloads
3. **Enable S3 Intelligent-Tiering** for unknown access patterns
4. **Delete unused resources** — Unattached EBS volumes, idle load balancers, old snapshots
5. **Use Spot Instances** for batch and fault-tolerant workloads
6. **Set billing alerts** via CloudWatch + Budget alarms
7. **Use AWS Cost Explorer** to analyze spend trends

---

## Getting Started Checklist

- [ ] Create an AWS account
- [ ] Enable MFA on the root account
- [ ] Create an IAM admin user — avoid using root daily
- [ ] Set up billing alerts
- [ ] Explore the AWS Free Tier (12-month free resources)
- [ ] Launch your first EC2 instance
- [ ] Create an S3 bucket and upload a file
- [ ] Write and deploy a Lambda function
- [ ] Explore the AWS Console and familiarize yourself with key services

---

## Resources

- [AWS Documentation](https://docs.aws.amazon.com)
- [AWS Free Tier](https://aws.amazon.com/free)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected)
- [AWS Skill Builder (Training)](https://skillbuilder.aws)
- [AWS Certified Cloud Practitioner](https://aws.amazon.com/certification/certified-cloud-practitioner/) — Recommended starting certification
