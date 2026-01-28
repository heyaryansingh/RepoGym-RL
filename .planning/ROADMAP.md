# Roadmap: RepoGym-RL

## Overview

RepoGym-RL is a local-first, containerized reinforcement learning environment designed for real-world software engineering tasks. This roadmap outlines the journey from building the core environment infrastructure to delivering a fully functional, verifiable RL gym with structured action spaces, quantifiable rewards, and automated telemetry.

## Domain Expertise

None

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

- [ ] **Phase 1: Project Foundation** - Base package structure and Environment API.
- [ ] **Phase 2: Sandbox Infrastructure** - Docker orchestration and isolation.
- [ ] **Phase 3: Action Space Framework** - Structured tool-calls and action mapping.
- [ ] **Phase 4: Task Pack Management** - Repository and test suite loading.
- [ ] **Phase 5: Environment Lifecycle** - State management and episode orchestration.
- [ ] **Phase 6: Grading & Reward System** - Test deltas and Radon-based rewards.
- [ ] **Phase 7: Telemetry & Logging** - Transcript generation and JSONL export.
- [ ] **Phase 8: CLI Developer Tools** - CLI for interaction and data export.
- [ ] **Phase 9: Pipeline Validation Task** - E2E validation with a simple bugfix.
- [ ] **Phase 10: Refinement & Documentation** - Final polish and docs.

## Phase Details

### Phase 1: Project Foundation
**Goal**: Establish the core package structure and the Gymnasium environment interface.
**Depends on**: Nothing
**Research**: Unlikely (Standard package setup)
**Plans**: 2 plans

Plans:
- [ ] 01-01: Initialize package structure and pyproject.toml
- [ ] 01-02: Implement base Gymnasium environment class

### Phase 2: Sandbox Infrastructure
**Goal**: Implement Docker-based isolation for executing agent actions safely.
**Depends on**: Phase 1
**Research**: Likely (Docker SDK usage)
**Research topics**: Docker SDK for Python, container resource limits, lifecycle management
**Plans**: 3 plans

Plans:
- [ ] 02-01: Create Docker management module
- [ ] 02-02: Implement container lifecycle (create, start, stop, remove)
- [ ] 02-03: Implement file transfer and execution inside container

### Phase 3: Action Space Framework
**Goal**: Define and implement the structured action space for the RL agent.
**Depends on**: Phase 2
**Research**: Unlikely (Standard schema design)
**Plans**: 2 plans

Plans:
- [ ] 03-01: Define Action Space schemas (JSON/Pydantic)
- [ ] 03-02: Implement action dispatcher and tool execution logic

### Phase 4: Task Pack Management
**Goal**: System for loading and managing software engineering tasks (repositories + tests).
**Depends on**: Phase 1
**Research**: Unlikely (File system operations)
**Plans**: 2 plans

Plans:
- [ ] 04-01: Implement task configuration loader
- [ ] 04-02: Implement repository checkout and setup logic

### Phase 5: Environment Lifecycle
**Goal**: Orchestrate the flow of an RL episode (reset, step, render).
**Depends on**: Phase 3, Phase 4
**Research**: Unlikely (State machine logic)
**Plans**: 2 plans

Plans:
- [ ] 05-01: Implement environment reset and task initialization
- [ ] 05-02: Implement step logic (action execution + state observation)

### Phase 6: Grading & Reward System
**Goal**: Calculate scalar rewards based on test pass/fail deltas and static analysis.
**Depends on**: Phase 5
**Research**: Likely (Radon/Static analysis)
**Research topics**: Radon API for cyclomatic complexity, test parsing strategies
**Plans**: 2 plans

Plans:
- [ ] 06-01: Implement test runner and result parser
- [ ] 06-02: Implement reward calculation logic (Deltas + Radon)

### Phase 7: Telemetry & Logging
**Goal**: Capture full episode transcripts and export them for training dataset generation.
**Depends on**: Phase 5
**Research**: Unlikely (Logging patterns)
**Plans**: 2 plans

Plans:
- [ ] 07-01: Implement episode transcript logger
- [ ] 07-02: Implement JSONL exporter for datasets

### Phase 8: CLI Developer Tools
**Goal**: CLI for manual task execution, replay, and data management.
**Depends on**: Phase 7
**Research**: Unlikely (Python Click/Typer)
**Plans**: 2 plans

Plans:
- [ ] 08-01: Implement basic CLI commands (run, export)
- [ ] 08-02: Implement episode replay utility

### Phase 9: Pipeline Validation Task
**Goal**: End-to-end validation of the entire pipeline with a real-world task.
**Depends on**: Phase 6, Phase 8
**Research**: Unlikely (Integration testing)
**Plans**: 1 plan

Plans:
- [ ] 09-01: Execute E2E validation with Python bugfix task

### Phase 10: Refinement & Documentation
**Goal**: API stabilization, documentation, and final polish.
**Depends on**: Phase 9
**Research**: Unlikely (Writing docs)
**Plans**: 2 plans

Plans:
- [ ] 10-01: Final API cleanup and type hinting
- [ ] 10-02: Complete README and technical documentation

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2 → 3 → 4 → 5 → 6 → 7 → 8 → 9 → 10

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Project Foundation | 2/2 | Complete | 2026-01-27 |
| 2. Sandbox Infrastructure | 3/3 | Complete | 2026-01-27 |
| 3. Action Space Framework | 2/2 | Complete | 2026-01-27 |
| 4. Task Pack Management | 2/2 | Complete | 2026-01-27 |
| 5. Environment Lifecycle | 2/2 | Complete | 2026-01-27 |
| 6. Grading & Reward System | 2/2 | Complete | 2026-01-27 |
| 7. Telemetry & Logging | 2/2 | Complete | 2026-01-27 |
| 8. CLI Developer Tools | 2/2 | Complete | 2026-01-27 |
| 9. Pipeline Validation Task | 1/1 | Complete | 2026-01-27 |
| 10. Refinement & Documentation | 2/2 | Complete | 2026-01-27 |
