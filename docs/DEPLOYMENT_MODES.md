# Database Operations Knowledge Assistant

## Overview

Database Operations Knowledge Assistant is a lightweight semantic search platform that enables Database Administrators (DBAs), Support Engineers, DevOps Teams, SRE Teams, and Cloud Operations Teams to search operational documentation using natural language.

The solution allows users to upload database runbooks, SOPs, troubleshooting guides, operational procedures, recovery documentation, and technical manuals, then perform semantic search using vector embeddings powered by Valkey-compatible vector databases.

The platform supports:

* Open Source Valkey
* Percona Valkey
* AWS MemoryDB Vector Search

This enables organizations to start with a low-cost deployment and seamlessly migrate to enterprise-grade managed infrastructure without application changes.

---

# Benefits

* Faster knowledge discovery
* Reduced troubleshooting time
* Centralized operational documentation
* Vendor-neutral architecture
* Open-source and managed deployment options
* Easy deployment using Docker
* GitHub Actions CI/CD ready
* Supports on-premises and cloud environments
* Easily extendable to full RAG architectures

---

# Key Features

### Document Management

* PDF Upload
* Automatic Text Extraction
* Duplicate Document Detection
* Batch Document Processing

### Semantic Search

* Intelligent Text Chunking
* Embedding Generation
* Vector Similarity Search
* Natural Language Queries

### Platform Support

* Open Source Valkey
* Percona Valkey
* AWS MemoryDB Vector Search

### Deployment

* Streamlit Web Interface
* Docker Deployment
* GitHub Actions CI/CD
* EC2 Deployment
* Kubernetes Ready

---

# Architecture

```text
PDF Documents
      │
      ▼
Text Extraction
      │
      ▼
Chunking
      │
      ▼
Embedding Generation
      │
      ▼
Vector Database
(Valkey / Percona Valkey / AWS MemoryDB)
      │
      ▼
Semantic Search
      │
      ▼
Streamlit User Interface
```

---

# Technology Stack

| Component                  | Technology                |
| -------------------------- | ------------------------- |
| Frontend                   | Streamlit                 |
| Language                   | Python                    |
| Embedding Model            | Sentence Transformers     |
| Vector Database            | Valkey                    |
| Enterprise Vector Database | Percona Valkey            |
| Managed Vector Database    | AWS MemoryDB              |
| Containerization           | Docker                    |
| CI/CD                      | GitHub Actions            |
| Deployment                 | EC2 / Docker / Kubernetes |

---

# Supported Use Cases

### Database Platforms

* PostgreSQL
* MySQL
* SQL Server
* Oracle
* MongoDB
* Amazon RDS
* Aurora PostgreSQL
* Aurora MySQL

### Documentation Types

* Administration Guides
* Backup and Recovery Procedures
* Disaster Recovery Runbooks
* Replication Guides
* Operational SOPs
* Troubleshooting Documentation
* Internal Knowledge Bases
* Production Support Documentation

---

# Prerequisites

## Infrastructure

### Recommended

* Ubuntu 22.04 or 24.04
* 4 vCPU
* 8 GB RAM
* 50 GB Storage

### Minimum

* 2 vCPU
* 4 GB RAM
* 20 GB Storage

---

## Software

* Python 3.11+
* Docker
* Docker Compose
* Git

---

# Deployment Modes

The application supports multiple deployment models based on organizational requirements.

---

## Option 1: Open Source Valkey

### Suitable For

* Development
* Personal Labs
* Proof of Concepts
* Small Teams
* On-Premise Deployments

### Docker Deployment

```bash
docker run -d \
  --name valkey \
  -p 6379:6379 \
  valkey/valkey:latest
```

### Configuration

```env
MEMORYDB_HOST=localhost
MEMORYDB_PORT=6379
MEMORYDB_USER=
MEMORYDB_PASSWORD=
```

### Advantages

* Open Source
* No Licensing Cost
* Lightweight
* Easy Deployment

---

## Option 2: Percona Valkey

### Suitable For

* Enterprise Open Source Deployments
* Production Workloads
* Percona Ecosystem Users

### Docker Deployment

```bash
docker run -d \
  --name percona-valkey \
  -p 6379:6379 \
  percona/percona-valkey:latest
```

### Configuration

```env
MEMORYDB_HOST=localhost
MEMORYDB_PORT=6379
MEMORYDB_USER=
MEMORYDB_PASSWORD=
```

### Advantages

* Enterprise Support
* Open Source
* Production Ready
* Operational Tooling

---

## Option 3: AWS MemoryDB Vector Search

### Suitable For

* Enterprise Production Environments
* High Availability Deployments
* Multi-AZ Architectures
* AWS Native Workloads

### Configuration

```env
MEMORYDB_HOST=clustercfg.<cluster>.memorydb.<region>.amazonaws.com
MEMORYDB_PORT=6379
MEMORYDB_USER=admin
MEMORYDB_PASSWORD=<password>
```

### Advantages

* Fully Managed
* Automatic Failover
* Multi-AZ Availability
* TLS Encryption
* AWS Security Integration

---

# Deployment Comparison

| Deployment     | Cost        | Complexity | Recommended Use        |
| -------------- | ----------- | ---------- | ---------------------- |
| Valkey         | Low         | Low        | Development / POC      |
| Percona Valkey | Medium      | Medium     | Enterprise Open Source |
| AWS MemoryDB   | Medium-High | Low        | Enterprise Production  |

---

# Migration Path

Organizations can start small and scale seamlessly:

```text
Valkey
   │
   ▼
Percona Valkey
   │
   ▼
AWS MemoryDB
   │
   ▼
RAG Platform
   │
   ▼
Enterprise Knowledge Management Solution
```

No application code changes are required.

Only environment variables need to be updated.

---

# Vector Index Creation

Create the vector index once.

```sql
FT.CREATE docs_idx
ON HASH
PREFIX 1 "doc:"
SCHEMA
document TEXT
chunk TEXT
embedding VECTOR HNSW 6
TYPE FLOAT32
DIM 384
DISTANCE_METRIC COSINE
```

Verify:

```sql
FT._LIST
```

Expected:

```text
docs_idx
```

---

# Repository Structure

```text
db-knowledge-assistant/

├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── docs/
│   ├── ARCHITECTURE.md
│   ├── DEPLOYMENT_MODES.md
│   ├── LIMITATIONS.md
│   ├── ROADMAP.md
│   ├── DEMO_QUERIES.md
│   └── TROUBLESHOOTING.md
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── memorydb_store.py
│   └── search.py
│
├── app.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── deploy.sh
├── README.md
├── .env.example
└── .gitignore
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/db-knowledge-assistant.git

cd db-knowledge-assistant
```

---

## Environment Configuration

```bash
cp .env.example .env
```

Update:

```env
MEMORYDB_HOST=
MEMORYDB_PORT=6379
MEMORYDB_USER=admin
MEMORYDB_PASSWORD=
```

---

## Python Setup

```bash
python3 -m venv myenv

source myenv/bin/activate

pip install -r requirements.txt
```

---

## Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# Docker Deployment

Build and start:

```bash
docker compose up -d
```

Verify:

```bash
docker ps
```

Application URL:

```text
http://<server-ip>:8501
```

---

# GitHub Actions CI/CD

## Required Secrets

Add the following GitHub Secrets:

```text
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

---

## Deployment Flow

```text
Developer
    │
    ▼
git push
    │
    ▼
GitHub Actions
    │
    ▼
Copy Files to EC2
    │
    ▼
Docker Build
    │
    ▼
Docker Restart
    │
    ▼
Application Available
```

---

# Demo Workflow

1. Upload PostgreSQL Administration Guide
2. Upload PostgreSQL Backup & Recovery Documentation
3. Upload MySQL Operational Runbooks
4. Upload SQL Server DR Procedures
5. Ask natural language questions
6. Review semantic search results

---

# Example Questions

### PostgreSQL

* How do I restore PostgreSQL?
* What is PITR?
* How do I configure streaming replication?
* How do I check replication lag?
* How do I perform failover?

### MySQL

* How do I create a replica?
* How do I troubleshoot replication issues?
* How do I perform backup and recovery?

### SQL Server

* How do I perform disaster recovery?
* How do I failover a cluster?
* How do I restore a backup?

---

# Recommended Deployments

## Small Scale

```text
Streamlit
    │
    ▼
Valkey
```

Suitable for:

* Less than 1,000 documents
* Internal teams
* Development environments

---

## Medium Scale

```text
EC2
 │
 ▼
Percona Valkey
 │
 ▼
Streamlit
```

Suitable for:

* 1,000 to 25,000 documents
* Production deployments
* Multiple teams

---

## Enterprise Scale

```text
EKS / EC2
     │
     ▼
AWS MemoryDB
     │
     ▼
Streamlit
     │
     ▼
LLM Integration
```

Suitable for:

* 25,000+ documents
* Enterprise deployments
* High availability requirements

---

# Additional Documentation

See the following documents for more information:

* docs/ARCHITECTURE.md
* docs/DEPLOYMENT_MODES.md
* docs/LIMITATIONS.md
* docs/ROADMAP.md
* docs/DEMO_QUERIES.md
* docs/TROUBLESHOOTING.md

---

# Security Recommendations

* Never commit `.env` files
* Use TLS for AWS MemoryDB
* Store credentials in GitHub Secrets
* Restrict network access using Security Groups
* Follow least-privilege access principles

---

# Release Information

Version: 1.0

Status: Proof of Concept (POC)

Supported Vector Databases:

* Open Source Valkey
* Percona Valkey
* AWS MemoryDB Vector Search

---

# License

MIT License

---

# Author

Database Operations Knowledge Assistant

Powered by Valkey Vector Search, Percona Valkey, and AWS MemoryDB.

