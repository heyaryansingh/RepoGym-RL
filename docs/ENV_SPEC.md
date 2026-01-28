# RepoGym-RL Environment Specification

This document details the Gymnasium API implementation for RepoGym-RL.

## Observation Space

The observation space is a `gymnasium.spaces.Dict` containing:

- `transcript` (`Text`): A rolling log of all environment interactions, including command outputs, status messages, and error reports.
- `working_directory` (`Text`): The current absolute path within the sandbox.

## Action Space

The action space is a `gymnasium.spaces.Text` space where agents provide a JSON string corresponding to the following schema:

### Action Wrapper
```json
{
  "action": {
    "command": "command_name",
    "arg1": "value1",
    ...
  }
}
```

### Available Commands

| Command | Arguments | Description |
|---------|-----------|-------------|
| `list_files` | `path` | Recursively list files in a directory. |
| `read_file` | `path` | Read the content of a file. |
| `write_file` | `path`, `content` | Write or overwrite a file with specific content. |
| `run_tests` | `path` (optional) | Run pytest on the specified path or project root. |
| `run_command` | `cmd` | Execute an arbitrary shell command. |

## Reward Function

The total reward is the sum of functional and quality components.

### Functional Rewards (Test Deltas)
Triggered on `run_tests`:
- **+1.0**: Each test that transitions from FAIL/ERROR to PASS.
- **-1.0**: Each test that transitions from PASS to FAIL/ERROR.

### Quality Rewards (Static Analysis)
Triggered on `write_file`:
- A "nudge" reward calculated from:
  - **Complexity Score**: Normalized Radon cyclomatic complexity (0.0 for complex, 1.0 for simple).
  - **Maintainability Index**: Normalized Radon MI (0.0 to 1.0).
- Scale: `(Complexity + Maintainability) / 10.0` (Max +0.2 per file write).

## Reset & Task Loading

`env.reset(options={"task_id": "taskId"})` loads a specific task pack.
- It cleans up any existing Docker container.
- Creates a fresh container.
- Deploys the task repository to `/workspace`.

## Closing

`env.close()` ensures:
- The Docker container is stopped and removed.
- The episode trajectory is written to a JSONL log in the `logs/` directory.
