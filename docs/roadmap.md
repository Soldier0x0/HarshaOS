# Roadmap & Milestones

This roadmap translates the HarshaOS v1.1 product strategy into actionable milestones. Each phase includes the primary features, success criteria, and integration considerations.

## Phase 1 – Foundation & Automation (ETA: 2 weeks)
**Goal:** Establish the backend API core, critical automation services, and system observability.

- **Deliverables**
  - FastAPI service skeleton with module scaffolding and dependency injection.
  - Config Manager with encrypted YAML storage (Fernet AES256) and secret rotation CLI.
  - Email automation pipeline: IMAP/SMTP connectors, classification, summarization, daily digest.
  - File watcher service with regex rule engine and dashboard notifications.
  - System monitor capturing CPU/RAM/disk/uptime metrics with alert thresholds.
- **Success Criteria**
  - 95% accuracy on email categorization during pilot dataset evaluation.
  - 1000 emails processed under 2 minutes end-to-end.
  - File automation actions executed within 1 second of detection.
- **Dependencies**
  - Windows service registration for background agents.
  - Local queue (e.g., Redis in local-only mode or in-process scheduler) for task orchestration.

## Phase 2 – Knowledge & Notes (ETA: 4 weeks)
**Goal:** Build knowledge management features and semantic search.

- **Deliverables**
  - Markdown vault directory conventions with YAML front matter and tagging.
  - Notes ingestion API with metadata extraction and bidirectional sync to UI.
  - ChromaDB integration for embedding generation and semantic search endpoints.
  - PDF/Text summarizer using local LLM models.
  - Learning digest aggregator for RSS feeds (arXiv, CISA, ANN) with cached summaries.
- **Success Criteria**
  - Semantic search retrieves relevant notes with ≥90% precision@5 on internal benchmarks.
  - Summaries generated within 3 seconds using local models.
  - RSS feeds cached for offline access and refresh daily.
- **Dependencies**
  - Ollama runtime configured with selected models.
  - Background jobs scheduled via APScheduler.

## Phase 3 – Finance & Life Analytics (ETA: 6 weeks)
**Goal:** Deliver personal finance intelligence and lifestyle tracking dashboards.

- **Deliverables**
  - Transaction parser for SMS/email exports with category classification.
  - Subscription tracker to detect recurring charges and send alerts.
  - Expense analytics dashboards rendered with Chart.js/Plotly.
  - Goal tracker module for focus hours, gym time, and learning sessions.
- **Success Criteria**
  - Classification accuracy ≥90% on labeled finance dataset.
  - Subscription detection recall ≥85%.
  - Dashboards render within 200ms with cached data.
- **Dependencies**
  - Integration with Config Manager for secure storage of financial data sources.
  - Shared metrics service for dashboard components.

## Phase 4 – AI Companion (Noah Core) (ETA: 8 weeks)
**Goal:** Introduce the contextual AI assistant with command execution.

- **Deliverables**
  - Ollama-based LLM engine with prompt routing and model selection.
  - Contextual query builder aggregating data from notes, emails, and system logs.
  - Command interpreter translating natural-language instructions into backend API calls.
  - Optional voice module with Whisper.cpp (STT) and Coqui/Piper (TTS).
- **Success Criteria**
  - AI response latency ≤3 seconds with traceable context references.
  - ≥95% accuracy for command interpreter on curated test suite.
  - Voice module achieves ≥92% transcription accuracy on local vocabulary set.
- **Dependencies**
  - Fine-tuned prompt templates and evaluation harness.
  - Security audit for command execution permissions.

## Phase 5 – Integrations & UI Enhancements (ETA: 10 weeks)
**Goal:** Polish the user experience, expand free integrations, and finalize dashboards.

- **Deliverables**
  - apivault.dev connector for weekly cached API catalog updates.
  - 21st.dev integration to import OpenAPI schemas and auto-generate FastAPI connector stubs.
  - anime.js-driven UI animations and transitions for dashboards.
  - Enhanced visualizations with Chart.js/Plotly for finance, focus, and productivity metrics.
  - RSS feed enhancements for knowledge streams with summarization hooks.
- **Success Criteria**
  - UI transitions under 100ms on reference hardware.
  - Manual override toggles for every external integration.
  - Offline dashboards fully functional with cached data.
- **Dependencies**
  - Plugin interface finalized and documented.
  - Frontend build pipeline optimized for Electron packaging.

## Success Metrics Recap
- Email digest success rate ≥95%.
- AI response latency ≤3 seconds.
- Classification accuracy ≥90%.
- File automation latency ≤1 second.
- Integration toggle control at 100%.
- Offline availability at 100%.

## Tracking & Governance
- **Issue Management:** Each feature tracked as GitHub issue linked to respective phase.
- **Documentation:** Living design docs maintained under `/docs` with updates per milestone.
- **Quality Gates:** Automated test suites and manual review checklists enforced before phase closure.
- **Security Reviews:** Configuration and AI command execution reviewed at the end of Phases 1, 3, and 4.

