from repogym.env import RepoGymEnv

def test_task_loading():
    env = RepoGymEnv(render_mode="human")
    
    print("\nTesting reset without task_id...")
    obs, info = env.reset()
    assert env.current_task is None
    
    print("\nTesting reset with valid task_id (repogym-internal)...")
    obs, info = env.reset(options={"task_id": "repogym-internal"})
    assert env.current_task is not None
    assert env.current_task.id == "repogym-internal"
    print(f"Transcript: {env.transcript}")
    assert "Loaded task: RepoGym Internal" in env.transcript
    
    print("\nTesting reset with invalid task_id...")
    obs, info = env.reset(options={"task_id": "non-existent"})
    assert "Warning: Failed to load task" in env.transcript
    
    print("\nTask loading verification successful!")

if __name__ == "__main__":
    test_task_loading()
