# ADIA — Audit Data Intelligence Assistant, Version 1

## Purpose
Display total recovered Bhutanese Ngultrum from authorized SQL records, with no AI-generated arithmetic. Future phases: natural-language questions, receipt/document ingestion, permission-aware RAG, and agent orchestration.

## Data and modalities
- **Now:** structured SQL payment rows. `amount_nu` and `status` are read; the demo exposes one aggregate and a count.
- **Later:** receipt images and PDFs referenced by SQL paths/URLs; OCR and document extraction. Optional text questions. Audio and video are out of scope for audit-recovery use case unless later justified.

## Task
Deterministic SQL retrieval/aggregation, *not* visual recognition/classification. Labels and transformer training are unnecessary for Version 1.

## Demo semantics
`POSTED` payments count as recovered; `PENDING` and `VOID` do not. Multiple posted payments against one observation are summed. All values are fictional. Real RAA status definitions, reversals, adjustments, currencies, fiscal dates and duplicate handling must be approved before production.

## Acceptance criteria
- Demo shows Nu. 80,000.00 from 3 posted records.
- Totals match trusted SQL reference queries on each test dataset.
- Pending/void values excluded, empty returns Nu. 0.00, partial payments included.
- No production write capability. Fail closed on unavailable database.

## Security boundary
Use dedicated read-only credentials, approved SQL views, per-user row permissions, no generic network URL fetching, no external LLM access to confidential data, parameterized queries, and no secrets in source control. A UI connected to production also requires authentication and audit logging.

## Known failure modes
Incorrect status mapping, accounting adjustments, duplicate rows after joins, cancelled/reversed payments, missing authorization filters, unreachable database, and stale records.
