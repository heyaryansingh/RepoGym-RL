from repogym.env import RepoGymEnv
import json
import os
import glob

def test_pipeline():
    print("Starting E2E Pipeline Validation...")
    env = RepoGymEnv(render_mode="human")
    
    # Mock sandbox to bypass Docker issues
    class MockSandbox:
        container = None
        def create_container(self): pass
        def start(self): pass
        def remove(self): pass
        def execute(self, cmd):
            if "pytest" in cmd:
                # Simulate initial failure then success
                if getattr(self, "fixed", False):
                    output = "test_math.py::test_average PASSED\n1 passed in 0.01s"
                    exit_code = 0
                else:
                    output = "test_math.py::test_average FAILED\n1 failed in 0.01s"
                    exit_code = 1
                return {"exit_code": exit_code, "output": output}
            return {"exit_code": 0, "output": "mock output"}
        def copy_to(self, src, dst): pass

    sandbox = MockSandbox()
    env.sandbox = sandbox
    
    print("\n[Step 1] Reset with bugfix-simple")
    env.reset(options={"task_id": "bugfix-simple"})
    
    print("\n[Step 2] Run initial tests (Expected: Fail)")
    action_test = json.dumps({"action": {"command": "run_tests", "path": "."}})
    _, reward_init, _, _, info_init = env.step(action_test)
    print(f"Initial Reward: {reward_init}, Info: {info_init}")
    
    print("\n[Step 3] Apply fix to math_utils.py")
    fixed_code = "def calculate_average(numbers):\n    if not numbers: return 0\n    return sum(numbers) / len(numbers)"
    action_fix = json.dumps({"action": {"command": "write_file", "path": "math_utils.py", "content": fixed_code}})
    _, reward_fix, _, _, info_fix = env.step(action_fix)
    print(f"Fix Reward (Static): {reward_fix}")
    sandbox.fixed = True # Signal mock to pass tests now
    
    print("\n[Step 4] Run tests again (Expected: Pass)")
    _, reward_final, _, _, info_final = env.step(action_test)
    print(f"Final Reward (Functional): {reward_final}, Info: {info_final}")
    
    print("\n[Step 5] Closing and verifying logs")
    env.close()
    
    log_files = glob.glob("logs/ep_*.jsonl")
    latest_log = max(log_files, key=os.path.getctime)
    with open(latest_log, "r") as f:
        lines = f.readlines()
        
    print(f"Log {latest_log} has {len(lines)} lines.")
    assert len(lines) == 4 # Metadata + 3 steps
    
    # Assert functional reward for passing tests
    # reward_final should be 1.0 (assuming calculate_test_reward gives +1 for pass)
    assert reward_final > 0
    
    print("\nE2E Pipeline Validation Successful!")

if __name__ == "__main__":
    test_pipeline()
