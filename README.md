# HarshaOS (Local Edition v1.1)

HarshaOS is a local-first personal operating system designed for privacy-conscious professionals who rely on automation, knowledge management, and analytics to run their day-to-day workflows. This repository tracks the product blueprint for **HarshaOS Local Edition v1.1** and captures the phased roadmap that will guide engineering execution.

## Vision
> Local-first personal operating system unifying automation, knowledge management, AI, and analytics. Fully private and extensible with free open-source integrations.

## Target User Profile
- **Persona:** Tech-oriented professional focused on productivity, automation, and security.
- **Core Skills:** Data Integration, Scripting, System Administration, Cyber Security.
- **Preferences:** Local control, privacy, automation, extensible tools.

## Guiding Principles
1. **Local First:** All data and computation remain on-device.
2. **Modular by Design:** Each service runs independently via clearly defined APIs.
3. **Automation First:** Every repeatable action should be automatable.
4. **Explainable AI:** AI outputs are traceable back to local data sources.
5. **Free Integrations Only:** Integrations must rely on open or free APIs.

## Product Objectives
- Automate digital tasks such as email management, file organization, and finance tracking.
- Provide local AI summarization and contextual insights.
- Integrate free APIs and SDKs for enrichment (apivault.dev, 21st.dev, animejs.com).
- Centralize all personal data and metrics in a single local dashboard.
- Maintain a modular design for future plugin-based extensions.

## High-Level Architecture
HarshaOS follows a layered architecture with a FastAPI backend, modular services, and an Electron + React frontend.

- **Frontend:** Electron shell with a React + Tailwind UI, animated via anime.js, visualizations through Chart.js and Plotly, communicating with the backend over REST and WebSockets.
- **Backend:** Python 3.11 FastAPI application orchestrated with APScheduler. Core modules include `mail_service`, `file_service`, `system_monitor`, `notes_engine`, `finance_service`, and `ai_engine`. Integrations live under `backend/integrations/` and follow a plugin contract.
- **Data Layer:** SQLite/DuckDB for structured storage, ChromaDB for vector search, and a local caching layer.
- **AI Runtime:** Ollama to host models such as Mistral 7B, Phi-3 Mini, and Llama 3 Instruct with contextual aggregation from local notes, mail, and logs.
- **Security:** Encrypted configuration and secrets using Fernet AES256, offline-by-default data policy, and local log rotation under `/logs/`.

See [`docs/architecture.md`](docs/architecture.md) for detailed diagrams, component responsibilities, and API boundaries.

## Development Phases & Roadmap
HarshaOS ships in five incremental phases. Each phase builds on the previous foundations while preserving offline-first guarantees.

| Phase | Title | Focus | ETA |
| ----- | ----- | ----- | --- |
| 1 | Foundation & Automation | Core FastAPI API, email automation, file watcher, system monitoring, encrypted config manager. | 2 weeks |
| 2 | Knowledge & Notes | Markdown vault, semantic search via ChromaDB, document summarization, learning digest feeds. | 4 weeks |
| 3 | Finance & Life Analytics | Transaction parser, subscription tracker, expense analytics, personal goal tracking dashboards. | 6 weeks |
| 4 | AI Companion (Noah Core) | Local LLM engine, contextual querying, command interpreter, optional voice module. | 8 weeks |
| 5 | Integrations & UI Enhancements | External API enrichment, dynamic animations, extended visualizations, RSS integration. | 10 weeks |

Detailed deliverables and success criteria for each phase are documented in [`docs/roadmap.md`](docs/roadmap.md).

## Success Metrics
- Email digest accuracy ≥ 95%.
- AI response latency ≤ 3 seconds.
- Classification accuracy ≥ 90%.
- File automation latency ≤ 1 second.
- Integration toggles offer 100% manual override.
- Offline availability at 100%.

## Future Extensions
Potential post-v1.1 enhancements include:
- Plugin marketplace for community scripts.
- Local API builder using imported schemas.
- Encrypted USB export to support multi-device workflows.
- Focus Economy module for time valuation.
- Containerized Linux build support.

## Repository Structure
```
.
├── README.md              # Product overview and quick reference
└── docs/
    ├── architecture.md    # Service-level architecture and contracts
    └── roadmap.md         # Phased delivery plan and milestone tracker
```

## Contributing
This repository currently tracks the product specification. Implementation tasks will be broken down per phase with detailed tickets. Contributions should respect the guiding principles above, maintain local-first privacy guarantees, and rely solely on open/free integrations.

