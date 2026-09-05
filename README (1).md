# VaayuNetra

VaayuNetra is a multi-source environmental intelligence and
decision-support platform.

## Core Product

VaayuNetra combines: - official air-quality monitoring, - local/IoT
sensors, - citizen reports and images, - satellite/thermal evidence, -
meteorological context, - population and sensitive-receptor data, -
economic-corridor geospatial data.

It converts these observations into environmental events, estimates
likely source categories, forecasts propagation, assesses exposure,
prioritizes risk, and routes actionable intelligence to authorities.

## Core Loop

Observe → Normalize → Spatial/Temporal Alignment → Local Baseline →
Detect → Corroborate → Source Hypothesis → Forecast → Exposure → Risk →
Authority Action → Outcome → Learning

## Primary Product Surface

The Authority Dashboard is the main operational interface. It is
event-centric rather than AQI-centric.

An authority should be able to answer: 1. What is happening? 2. Where?
3. Why does VaayuNetra believe it? 4. What is the likely source
category? 5. Where will it move? 6. Who will be exposed? 7. How urgent
is it? 8. Which authority should act? 9. What action is recommended? 10.
What happened afterward?

## Current MVP

P0: - ingestion - PostgreSQL/PostGIS - H3 - local baseline - event
detection - citizen reports - basic CV validation - evidence fusion -
weather - first propagation forecast - exposure - risk - authority
dashboard - alert workflow

P1: - FIRMS - Sentinel-5P - source hypothesis - corridor intelligence -
improved forecasting - interoperability API

P2: - ST-GNN - advanced physics/ML ensemble - federated learning -
multi-city federation

## Development

Claude is used primarily for architecture, reasoning, research, ML
design, and review.

Codex is used primarily for repository inspection, implementation,
testing, integration, and refactoring.

GitHub is the durable source of truth.
