# RepoGym-RL

[![Project Status: Active](https://img.shields.io/badge/Project%20Status-Active-brightgreen.svg)](https://github.com/heyaryansingh/RepoGym-RL)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.9+](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)

**RepoGym-RL** is a high-fidelity, containerized Reinforcement Learning (RL) environment designed to train and evaluate AI agents on real-world software engineering tasks. It transforms repository-level interactions—like fixing bugs, refactoring, and implementing features—into a quantifiable Gymnasium-compatible environment.

---

## Why RepoGym-RL?

Evaluating LLMs on code is easy; evaluating them on **Software Engineering** is hard. RepoGym-RL provides the missing infrastructure for:

*   **Measurable Evaluation**: Direct, non-subjective reward signals based on test pass-rates and code quality.
*   **Safety & Isolation**: Mandatory Docker sandboxing ensures agents can't harm the host machine.
*   **Local-First Design**: Run complex evaluations on your local machine without relying on external APIs.
*   **Scientific Rigor**: Structured JSONL telemetry tracks Every single action, reward, and state transition.

---

## How It Works

RepoGym-RL follows the standard **Reinforcement Learning Loop**, specialized for the software development lifecycle:

1.  **Environment**: A Docker container containing a target repository (the "Task Pack").
2.  **Observation**: The agent receives the current directory structure and a persistent **Transcript** of all previous terminal outputs and file reads.
3.  **Actions**: The agent performs structured tool-calls via JSON (e.g., `write_file`, `run_tests`, `read_file`).
4.  **Reward**:
    *   **Functional**: Significant positive/negative reward based on `pytest` delta transitions.
    *   **Quality**: Continuous "nudges" based on **Radon** metrics (Cyclomatic Complexity & Maintainability Index).

---

## Installation

### Prerequisites
*   Python 3.9+
*   **Docker Desktop**: Ensure the Docker daemon is running and accessible.

### Setup
```bash
# Clone and enter repo
git clone https://github.com/heyaryansingh/RepoGym-RL.git
cd RepoGym-RL

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/macOS

# Install in editable mode
pip install -e .
```

---

## Quick Start

### 1. View the Web Dashboard
I've built a landing page to visualize the project architecture and interactive demo.
```bash
cd web
npm install
npm run dev
```
*Visit `http://localhost:5173` to experience the "Nano Banana" designed UI.*

### 2. Run the Quantifiable Demo
See the reward system in action with a standalone bugfix scenario:
```bash
# Run from the project root
$env:PYTHONPATH="src"
python demo/run_demo.py
```

### 3. Manual Exploration (Shell)
Play the role of an agent yourself in any task pack:
```bash
repogym shell --task bugfix-simple
```

---

## Developer Tools

*   **`repogym shell`**: Interactive environment for human-in-the-loop testing.
*   **`repogym inspect <logfile>`**: Beautiful terminal visualization of agent trajectories using `Rich`.
*   **`demo/run_demo.py`**: A standalone verification script for direct measurement.

---

## Roadmap

- [x] **Phase 1-9**: Core Environment, Docker Sandboxing, Grading, and CLI.
- [x] **Phase 10**: Refinement & Documentation.
- [ ] **Multi-Agent Support**: Collaborative bug fixing.
- [ ] **Task Library Expansion**: Integrated support for SWE-bench and HumanEval repositories.
- [ ] **Real-world GitHub Integration**: Automated task generation from live Issues.

---

## Project Structure

```text
src/repogym/
├── env.py          # Main Gymnasium Environment API
├── sandbox/        # Docker orchestration & Isolation
├── actions.py      # Pydantic schemas for agent tools
├── grader/         # Reward logic (Functional & Static)
└── telemetry.py    # JSONL logging & Trajectory tracking
web/                # Premium React Dashboard
demo/               # Quantifiable verification scripts
docs/               # Detailed ENV_SPEC and Technical Docs
```

---

## License

MIT © [Aryan Singh](https://github.com/heyaryansingh)
