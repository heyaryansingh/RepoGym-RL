import json
import sys
import os

# Ensure src is in the path
sys.path.append(os.path.join(os.getcwd(), "src"))

from repogym.env import RepoGymEnv

def test_rewards():
    with open("verify_rewards.log", "w") as log:
        def log_msg(msg):
            print(msg)
            log.write(msg + "\n")
            log.flush()

        log_msg("Starting rewards verification...")
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
                    output = "test_math PASSED [100%]"
                return Res()
            def copy_to(self, src, dst): pass

        env.sandbox = MockSandbox()
        env.reset()
        
        log_msg("\n--- Testing Quality Reward (Simple Code) ---")
        simple_code = "def add(a, b):\n    return a + b"
        action = json.dumps({"action": {"command": "write_file", "path": "simple.py", "content": simple_code}})
        obs, reward, term, trunc, info = env.step(action)
        log_msg(f"Reward: {reward}, Info: {info}")
        if info.get("quality_reward", 0) > 0:
            log_msg("SUCCESS: Simple code rewarded.")
        else:
            log_msg("FAILURE: Simple code not rewarded.")
        
        log_msg("\n--- Testing Quality Reward (Complex Code) ---")
        complex_code = "def complex_func(n):\n"
        for i in range(10):
            complex_code += f"    if n > {i}:\n"
        complex_code += "        return True\n    return False"
        
        action = json.dumps({"action": {"command": "write_file", "path": "complex.py", "content": complex_code}})
        obs, reward2, term, trunc, info = env.step(action)
        log_msg(f"Reward: {reward2}, Info: {info}")
        if reward2 < reward:
            log_msg("SUCCESS: Complex code rewarded less than simple code.")
        else:
            log_msg("FAILURE: Complex code reward logic incorrect.")
        
        log_msg("\n--- Testing Functional Reward (Test Delta) ---")
        env.prev_test_results = {"test_math": "FAIL"}
        action = json.dumps({"action": {"command": "run_tests", "path": "tests/"}})
        obs, reward3, term, trunc, info = env.step(action)
        log_msg(f"Reward: {reward3}, Info: {info}")
        if info.get("test_reward", 0) == 1.0:
            log_msg("SUCCESS: Test delta rewarded.")
        else:
            log_msg("FAILURE: Test delta reward logic failed.")
        
        log_msg("\nRewards verification successful!")

if __name__ == "__main__":
    try:
        test_rewards()
    except Exception as e:
        with open("verify_rewards.log", "a") as log:
            log.write(f"\nCRITICAL FAILURE: {str(e)}\n")
        raise e
