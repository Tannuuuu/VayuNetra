# VaayuNetra — Agent Context

VaayuNetra is a pollution-event detection platform (Smart India Hackathon).
Full specs live in docs/ — read these before making changes:
- docs/product-spec.md — what we're building and why
- docs/architecture.md — system architecture, DB schema, pipelines
- docs/decisions/data-contract.md — the JSON record schema for the ingestion→engine boundary
- docs/ml/event-detection-design.md — target variable, features, labeling, evaluation for the detection model

## Current focus
Building the event-detection engine (backend/intelligence/detection/) against a
synthetic data source first, decoupled from the real ingestion pipeline via a
DataSource interface (stream/latest). See the ticket in the current task.

## Rules
- Never compute the baseline using future timestamps relative to the query point (leakage).
- Match the JSON schema in docs/decisions/data-contract.md exactly — don't invent fields.
- Keep the DataSource interface abstract; don't hardcode against one implementation.
