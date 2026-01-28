from repogym.env import RepoGymEnv
import json
import os
import glob

def test_telemetry():
    print("Initializing RepoGymEnv for telemetry test...")
    env = RepoGymEnv(render_mode="human")
    
    # Mock sandbox to bypass Docker issues during verification
    class MockSandbox:
        container = None
        def create_container(self): pass
        def start(self): pass
        def remove(self): pass
        def execute(self, cmd):
            class Res:
                exit_code = 0
                output = "mock output"
            return Res()
        def copy_to(self, src, dst): pass

    env.sandbox = MockSandbox()
    
    print("\n--- Resetting ---")
    env.reset(options={"task_id": "repogym-internal"})
    
    print("\n--- Performing Step 1 (ls) ---")
    action1 = json.dumps({"action": {"command": "list_files", "path": "."}})
    env.step(action1)
    
    print("\n--- Performing Step 2 (write) ---")
    valid_python = "def hello():\n    print('world')"
    action2 = json.dumps({"action": {"command": "write_file", "path": "log_test.py", "content": valid_python}})
    env.step(action2)
    
    print("\n--- Closing Environment ---")
    env.close()
    
    print("\n--- Verifying Logs ---")
    log_files = glob.glob("logs/ep_*.jsonl")
    if not log_files:
        print("FAILURE: No log file found in logs/")
        return
    
    latest_log = max(log_files, key=os.path.getctime)
    print(f"Found log: {latest_log}")
    
    with open(latest_log, "r") as f:
        lines = f.readlines()
        
    print(f"Log has {len(lines)} lines.")
    
    # Check metadata
    metadata = json.loads(lines[0])
    assert metadata["task_id"] == "repogym-internal"
    print("Metadata verified.")
    
    # Check steps
    assert len(lines) == 3 # metadata + 2 steps
    step1 = json.loads(lines[1])
    assert "list_files" in step1["action"]
    print("Step 1 (ls) verified.")
    
    step2 = json.loads(lines[2])
    assert "write_file" in step2["action"]
    assert step2["reward"] > 0 # quality reward for simple content
    print("Step 2 (write) verified.")
    
    print("\nTelemetry verification successful!")

if __name__ == "__main__":
    test_telemetry()
