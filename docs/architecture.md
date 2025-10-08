# Architecture Overview

HarshaOS is designed as a modular, local-first operating environment composed of independent services that communicate over well-defined APIs. This document expands on the high-level description in the README and captures the core responsibilities, data flows, and security considerations.

## System Context
- **Primary User:** Security-conscious professional running HarshaOS on Windows 10/11.
- **Deployment Mode:** Offline-first desktop deployment with optional, user-controlled network calls for free/open integrations.
- **Execution Environment:** Python 3.11 backend, Electron desktop shell for the user interface, SQLite/DuckDB persistent storage, and Ollama for local model execution.

## Component Breakdown

### 1. Frontend Shell
- **Frameworks:** Electron + React + TailwindCSS + anime.js.
- **Responsibilities:**
  - Provide responsive dashboards for automation, knowledge, finance, and AI companion modules.
  - Communicate with the backend via REST for CRUD operations and WebSockets for real-time notifications (system alerts, task status updates).
  - Render charts using Chart.js/Plotly and orchestrate transitions via anime.js.
- **Key Modules:**
  - `dashboard`: unified overview of automation status, metrics, and alerts.
  - `notes`: markdown vault access with tagging and search.
  - `finance`: expense analytics, subscription tracking visualizations.
  - `noah`: conversational AI interface with contextual insights.

### 2. Backend API Layer
- **Framework:** FastAPI with Pydantic models and dependency injection.
- **Scheduler:** APScheduler running background jobs for polling mailboxes, file system watchers, RSS feeds, and analytics refreshes.
- **Modules:**
  - `mail_service`: IMAP/SMTP connectors, classification pipeline, summarization jobs, digest generation.
  - `file_service`: Folder watchers, regex-based sorting rules, archival automation.
  - `system_monitor`: CPU/RAM/disk tracking with threshold-based alerts pushed to the dashboard.
  - `config_manager`: Encrypted configuration management using Fernet AES256 and secrets rotation.
  - `notes_engine`: Markdown ingestion, metadata extraction, semantic indexing via ChromaDB embeddings.
  - `finance_service`: Transaction parsing, recurring charge detection, budgeting analytics.
  - `ai_engine`: Local LLM orchestration through Ollama, prompt templating, context assembly.
- **Integration Plugins:** Under `backend/integrations/`, each integration implements a standard interface (`register()`, `fetch()`, `sync()`) and operates in offline or cached modes.

### 3. Data & Storage Layer
- **Relational Storage:** SQLite (default) or DuckDB for structured datasets (emails, transactions, system logs).
- **Vector Store:** ChromaDB for embeddings and semantic search across notes, emails, and documents.
- **File Storage:** Local directories for Markdown vault, document cache, and export archives.
- **Caching:** On-disk caches for RSS feeds, API catalogs, and generated digests.
- **Backup/Recovery:** Periodic snapshots with optional encrypted USB export (future extension).

### 4. AI Runtime (Noah Core)
- **Models:** Mistral 7B, Phi-3 Mini, Llama 3 Instruct, all running locally via Ollama.
- **Capabilities:**
  - Contextual aggregation of notes, emails, and system logs.
  - Document summarization (PDF/Text) using local embeddings and compression techniques.
  - Command interpreter mapping natural language to backend API calls.
  - Optional voice interface with Whisper.cpp (STT) and Coqui/Piper (TTS).
- **Explainability:** Each AI response references source documents and commands executed, satisfying the explainable AI principle.

### 5. Security & Privacy Controls
- **Encryption:** Fernet AES256 for configs/secrets. Secrets stored under `config/secure/` with rotation policies.
- **Access Control:** Local-only accounts with biometric/PIN unlock (future iteration). Administrative operations gated by local OS permissions.
- **Audit & Logging:** Structured logs under `/logs/` with rotation. Audit trails for automation actions and AI commands.
- **Network Policy:** Offline by default. Integrations (apivault.dev, 21st.dev, RSS feeds) require explicit toggle and provide cached data.

## Data Flows
1. **Email Automation:** APScheduler triggers `mail_service` polling → messages classified and summarized → results stored in SQLite → digest pushed to frontend via WebSocket notification.
2. **File Watcher:** File system events captured by watchdog → `file_service` applies regex routing rules → files moved/renamed → operations logged and surfaced in dashboard.
3. **Knowledge Ingestion:** Notes saved locally → metadata extracted → embeddings generated with local models → indexed in ChromaDB for semantic search.
4. **Finance Analytics:** Transaction exports ingested → parser categorizes entries → recurring payments flagged → dashboards update with Chart.js visualizations.
5. **AI Queries:** Frontend sends prompt with context request → `ai_engine` assembles relevant data from SQLite/ChromaDB → Ollama executes model → response returned alongside trace metadata.

## Non-Functional Requirements
- **Performance Targets:**
  - Process 1000 emails in under 2 minutes.
  - Generate AI summaries in under 3 seconds.
  - File automation latency under 1 second.
  - UI panel transitions under 100ms.
- **Reliability:** Services must resume gracefully after restart with persisted job state.
- **Storage Budget:** Total footprint ≤ 2GB (including models and caches).
- **Offline Availability:** Full functionality without internet access using cached data snapshots.

## Open Questions
- Finalize plugin interface schema and packaging format for future marketplace.
- Determine strategy for encrypted USB export and synchronization conflicts.
- Evaluate hardware requirements for simultaneous Ollama model usage and analytics workloads.

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Ollama](https://ollama.ai/)
- [ChromaDB](https://docs.trychroma.com/)
- [anime.js](https://animejs.com/)
- [Chart.js](https://www.chartjs.org/)

