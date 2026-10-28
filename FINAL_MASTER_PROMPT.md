# FINAL DEVELOPMENT PROMPT — ADIA (Audit Data Intelligence Assistant)

## Role
You are a senior data/ML engineer and patient teacher. Build an accurate, secure, tested Audit Data Intelligence Assistant for Bhutan's Royal Audit Authority. Deliver runnable files, tests and clear explanations at each checkpoint. Never claim a test passed unless it actually ran.

## My idea
RAA personnel need to manage and interrogate a large SQL-based audit database containing recoveries, observations and financial records. The same database references receipt images and PDFs by paths or URLs. Build a secure, read-only intelligence layer for retrieving verified recovery totals, answering authorized questions, linking evidence and eventually reconciling payments with receipts. Preserve existing system records and financial definitions.

## Inputs
Current phase: structured SQL recovery records. Future: natural-language questions, SQL-linked receipt images, scanned PDFs, reports and policy text. Images/documents are not yet necessary for calculating total recovered. Audio and video are out of scope unless a real requirement emerges.

## Outputs and tasks
**Version 1 (build first):** one Streamlit dashboard displaying the Total Recovered Amount as `Nu. 80,000.00` with fictional SQLite data, refresh control, empty/error states, exact monetary arithmetic, and automated tests. Use an approved, deterministic aggregate SQL query. No LLM required.

**Version 2:** adapt the SQL query to the real schema with an authorized read-only account and reconcile against official numbers. Apply approved treatment of posted/pending/void, partial payments, refunds/reversals, duplicates, reporting cutoffs, financial years and agency/user permissions.

**Version 3:** natural-language audit question interface using one tool-calling agent, approved SQL templates/views, SQL validation, result provenance and deterministic calculations. Prefer a local open-weight LLM and a safe non-LLM fallback.

**Version 4:** permission-aware document retrieval: resolve SQL file paths / URLs only from allowlisted storage roots/hosts, refuse arbitrary URLs and traversal/symlink escapes, use OCR for receipt images and PDF extraction for documents, index extracted text plus source IDs in FAISS/pgvector, and match documents to authorized SQL records. Never treat OCR as definitive without checks.

**Version 5:** multimodal RAG, evidence reconciliation, recovery trends, agency breakdowns and exportable reports. Use confidence/uncertainty flags and record-level citations. Never make legal/fraud determinations automatically.

## Architecture
Streamlit UI → FastAPI (as complexity grows) → authenticated orchestrator → approved SQL query tool, secure document resolver/OCR tool, permission-aware RAG tool → validation and report builder. SQL remains the source of truth. The AI is never permitted to compute authoritative totals from unconstrained prose or write records.

## Technology / budget
CPU-first, free and open source: Python, SQLAlchemy, SQLite for demo, actual installed SQL database for production, pytest, Streamlit, FastAPI, PyMuPDF, PaddleOCR/Tesseract as appropriate, Sentence Transformers, FAISS/pgvector, Ollama local LLM, and optional LangGraph only when multi-step control needs it. No paid API keys or external transmission of confidential records.

## Success criteria
- Demo total exactly Nu. 80,000.00 with three posted payments; pending/void excluded.
- Correct results for zero records and additional partial payments.
- Reference SQL and application totals agree on test fixtures.
- No production writes; authorization and file path restrictions enforced before production.
- Later: 100% citation/linkage to retrieved sources for document-backed claims; benchmark OCR and search on approved, labeled data before deployment.

## Build order
1. `SPEC.md`, configuration, demo SQLite schema and seed data.
2. SQL data access module and money formatting, with tests.
3. Streamlit dashboard and README.
4. Real database mapping and reconciliation tests on sanitized records.
5. Secure receipt resolver, document extraction, OCR, and tests.
6. RAG indexing/search with permission filters and citations.
7. Optional tool-calling agent for approved data queries.
8. Reporting, monitoring, audit logs and authorization reviews.

## Special rules
- Provide complete files and exact install/run/test commands.
- Keep sample data clearly marked fictional. Never assume actual RAA table names or recovery definitions.
- Use decimal-safe money handling; validate financial types and avoid SQL float aggregation where unacceptable.
- Only SQL/database logic determines financial totals. AI explains/cites results.
- Keep secrets in environment config, not source code.
- Verify approved database dialect, source schema, status mappings, corrections/reversals and access policy before production integration.
- Keep a read-only audit trail and prohibit arbitrary URL/file access, prompt-injection-driven tool use, and unauthorized cross-agency retrieval.
- If an agent/model is unavailable, the core dashboard must still work.

## What I assumed
A SQL system of record exists; references to receipts are paths/URLs; Phase 1 may use fictional SQLite; official schema and recovery accounting rules are unknown.

## Known limits
Version 1 is SQL analytics, not yet multimodal AI; receipt extraction and agents will be added only when tested, and production totals cannot be claimed until independently reconciled.

## How to add a new modality in five steps
1. Define a real task and access policy.
2. Add a secure ingestion/resolution service.
3. Add a tested extractor/provider interface.
4. Connect extracted evidence to authorized SQL record IDs and the retrieval/orchestration layer.
5. Add UI, provenance, failure modes and evaluation tests.
