from repogym.env import RepoGymEnv
import json
import time

def test_lifecycle_e2e():
    print("Initializing RepoGymEnv...")
    env = RepoGymEnv(render_mode="human")
    
    try:
        print("\n--- Resetting with 'repogym-internal' task ---")
        obs, info = env.reset(options={"task_id": "repogym-internal"})
        assert env.current_task is not None
        assert env.sandbox.container is not None
        print("Container created and started successfully.")
        
        print("\n--- Testing RunCommand action (echo hello) ---")
        action = json.dumps({"action": {"command": "run_command", "cmd": "echo hello from inside"}})
        obs, reward, term, trunc, info = env.step(action)
        print(f"Info: {info}")
        assert info["action_valid"] == True
        assert "hello from inside" in env.transcript
        
        print("\n--- Testing ListFiles action (ls -R . ) ---")
        action = json.dumps({"action": {"command": "list_files", "path": "."}})
        obs, reward, term, trunc, info = env.step(action)
        assert info["action_valid"] == True
        assert "pyproject.toml" in env.transcript
        
        print("\n--- Testing WriteFile and ReadFile cycle ---")
        action = json.dumps({"action": {"command": "write_file", "path": "/workspace/test_lifecycle.txt", "content": "lifecycle test content"}})
        env.step(action)
        
        action = json.dumps({"action": {"command": "read_file", "path": "/workspace/test_lifecycle.txt"}})
        obs, reward, term, trunc, info = env.step(action)
        assert "lifecycle test content" in env.transcript
        
        print("\n--- Testing invalid action format penalty ---")
        obs, reward, term, trunc, info = env.step("not a json")
        assert info["action_valid"] == False
        assert reward == -1.0
        
        print("\nE2E Lifecycle verification successful!")
        
    finally:
        print("\n--- Closing Environment (Cleanup) ---")
        env.close()
        print("Cleanup initiated.")

if __name__ == "__main__":
    test_lifecycle_e2e()
