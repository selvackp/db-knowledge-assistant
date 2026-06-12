# Current Limitations

## Overview

This project is currently implemented as a lightweight semantic search platform using vector embeddings and vector similarity search.

The objective is to demonstrate document ingestion, vector indexing, and semantic retrieval capabilities.

---

## Current Design

Current workflow:

PDF
↓
Text Extraction
↓
Fixed Size Chunking
↓
Embedding Generation
↓
Vector Search
↓
Result Display

---

## Known Limitations

### Fixed Size Chunking

Documents are split using character-based chunking.

Potential impact:

- Sections may be split across chunks
- Context may be partially lost
- Search quality may vary

---

### No Metadata Awareness

Current implementation does not store:

- Page Numbers
- Chapter Names
- Section Headers

Potential impact:

- Reduced traceability
- Less user-friendly search results

---

### No Re-ranking Layer

Current retrieval uses vector similarity only.

Potential impact:

- Relevant results may not always appear first
- Table of contents sections may be returned

---

### No LLM-Based Answer Generation

Current implementation returns retrieved chunks.

Potential impact:

- Users must interpret source content
- No conversational answers

---

### No Authentication

Current implementation provides open access.

Potential impact:

- Not suitable for multi-user production deployments

---

## Intended Usage

Current version is intended for:

- Proof of Concepts
- Internal Demonstrations
- Learning
- Small Knowledge Bases

Not intended for:

- Enterprise Production Deployments
- Sensitive Data Storage
- Multi-Tenant Workloads
