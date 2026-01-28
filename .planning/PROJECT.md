# RepoGym-RL

A local-first, containerized reinforcement learning environment for real-world software engineering tasks, providing quantifiable, verifiable reward signals.

## Goal
To build a high-fidelity simulation environment where RL agents can be evaluated on long-horizon software engineering tasks (bug fixes, features, refactors) with objective, non-subjective scoring.

## Requirements

### Validated
(None yet — ship to validate)

### Active
- [ ] **High-Fidelity Simulation**: Real Git repositories, real test suites, and Docker container isolation.
- [ ] **Quantifiable Reward Signals**: Scalar rewards based on test pass/fail deltas and static analysis (Radon/Cyclomatic complexity).
- [ ] **Structured Action Space**: Typed interactions (read, edit, run tests) rather than raw shell access.
- [ ] **Telemetery & Dataset Generation**: Episode transcripts, diffs, and reward timelines exportable to JSONL.
- [ ] **Platform-Agnostic Sandbox**: Docker-based execution that works across Linux, Windows, and macOS.
- [ ] **CLI Interface**: For running tasks, replaying episodes, and exporting data.

### Out of Scope
- [ ] **Model Training**: The goal is environment and evaluation, not the trainer itself.
- [ ] **Cloud-Native orchestration**: Initial focus is local-first developer/researcher machines.
- [ ] **Frontier Model Hosting**: No built-in LLM inference service (agnostic to agent implementation).

## Key Decisions
| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Static Analysis Rewards | Ensure quantifiable, verifiable signals without subjective LLM "vibes". | Purely Static (Radon) — Pending |
| Docker Isolation | Platform-agnostic, reproducible, and safe execution environment. | Native Docker — Pending |
| Tool-Call Action Space | Constrains agent to manageable, loggable actions for better telemetry. | Structured Action Map — Pending |
| Phase 1 Focus | Single-file Python bugfix to validate the E2E pipeline. | Python Minimal Slice — Pending |

## System Architecture (Proposed)
- `core/`: Gymnasium environment and episode lifecycle logic.
- `sandbox/`: Docker container runner and resource management.
- `tasks/`: Self-contained task packs with hidden/public tests.
- `grader/`: Scorecard generation based on test deltas and static metrics.
- `telemetry/`: Transcript logging and dataset export utilities.

---
*Last updated: 2026-01-27 after initialization*
