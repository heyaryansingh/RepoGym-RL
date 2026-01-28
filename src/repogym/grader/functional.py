from typing import Dict

def calculate_test_reward(prev_results: Dict[str, str], current_results: Dict[str, str]) -> float:
    """
    Calculates a reward based on the change in test statuses.
    Status can be 'PASS', 'FAIL', or 'ERROR'.
    
    Reward logic:
    - +1.0 for each test that goes from FAIL/ERROR to PASS.
    - -1.0 for each test that goes from PASS to FAIL/ERROR.
    - 0.0 otherwise.
    """
    reward = 0.0
    
    # Iterate through current tests
    for test_id, current_status in current_results.items():
        prev_status = prev_results.get(test_id)
        
        if current_status == "PASS" and prev_status in ["FAIL", "ERROR"]:
            reward += 1.0
        elif current_status in ["FAIL", "ERROR"] and prev_status == "PASS":
            reward -= 1.0
            
    return reward

def parse_pytest_output(output: str) -> Dict[str, str]:
    """
    A simple (and likely incomplete) parser for pytest output.
    Returns a dictionary mapping test names/IDs to their status.
    In a real scenario, this would be much more robust or use --json-report.
    """
    results = {}
    lines = output.splitlines()
    for line in lines:
        if " PASSED " in line:
            parts = line.split(" PASSED ")
            test_name = parts[0].strip().split("::")[-1]
            results[test_name] = "PASS"
        elif " FAILED " in line:
            parts = line.split(" FAILED ")
            test_name = parts[0].strip().split("::")[-1]
            results[test_name] = "FAIL"
    return results
