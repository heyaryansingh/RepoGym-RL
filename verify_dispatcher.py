from repogym.env import RepoGymEnv
import json

def test_dispatcher():
    env = RepoGymEnv(render_mode="human")
    env.reset()
    
    print("\nTesting valid ListFiles action...")
    action = json.dumps({"action": {"command": "list_files", "path": "src"}})
    obs, reward, term, trunc, info = env.step(action)
    print(f"Info: {info}")
    assert info["action_valid"] == True
    assert info["action_type"] == "list_files"
    
    print("\nTesting valid WriteFile action...")
    action = json.dumps({"action": {"command": "write_file", "path": "test.txt", "content": "hello"}})
    obs, reward, term, trunc, info = env.step(action)
    print(f"Info: {info}")
    assert info["action_valid"] == True
    
    print("\nTesting invalid JSON...")
    obs, reward, term, trunc, info = env.step("{invalid_json}")
    print(f"Info: {info}")
    assert info["action_valid"] == False
    assert reward == -1.0
    
    print("\nTesting invalid Schema (missing field)...")
    action = json.dumps({"action": {"command": "list_files"}}) # Missing path
    obs, reward, term, trunc, info = env.step(action)
    print(f"Info: {info}")
    assert info["action_valid"] == False
    
    env.render()
    print("\nDispatcher verification successful!")

if __name__ == "__main__":
    test_dispatcher()
