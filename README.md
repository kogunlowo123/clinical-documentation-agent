# Clinical Documentation Agent

[![CI](https://github.com/kogunlowo123/clinical-documentation-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/clinical-documentation-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Healthcare | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Clinical documentation agent that generates structured clinical notes from physician dictation, applies medical coding suggestions, ensures compliance with documentation standards, and identifies documentation gaps.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `transcribe_dictation` | Transcribe physician dictation into structured clinical note |
| `suggest_codes` | Suggest ICD-10, CPT, and HCPCS codes from clinical documentation |
| `check_completeness` | Check clinical documentation for required elements and gaps |
| `apply_template` | Apply a documentation template for a specific encounter type |
| `audit_quality` | Audit documentation quality and CDI opportunities |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/clinical-documentation/process` | Process request |
| `POST` | `/api/v1/clinical-documentation/query` | Query data |
| `POST` | `/api/v1/clinical-documentation/validate` | Validate |
| `POST` | `/api/v1/clinical-documentation/report` | Generate report |
| `GET` | `/api/v1/clinical-documentation/audit` | Get audit trail |

## Features

- Clinical
- Documentation
- Compliance
- Interoperability

## Integrations

- Epic Ehr
- Cerner Ehr
- Allscripts
- Fhir Server
- Clearinghouse

## Architecture

```
clinical-documentation-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── clinical_documentation_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**EHR + Healthcare Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
