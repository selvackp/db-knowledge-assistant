# Installation

## Clone Repository

```bash
git clone https://github.com/selvackp/db-knowledge-assistant.git

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

# Vector Index Creation

Create the vector index once.

```sql
FT.CREATE docs_idx ON HASH PREFIX 1 "doc:" SCHEMA document TEXT chunk TEXT embedding VECTOR HNSW 6 TYPE FLOAT32 DIM 384 DISTANCE_METRIC COSINE
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
