import sys
sys.path.append('src')
from repogym.sandbox.docker import DockerSandbox
import os

def test_sandbox():
    ds = DockerSandbox()
    print("Creating container...")
    ds.create_container('python:3.11-slim', 'sleep 60')
    ds.start()
    
    print("Testing execution...")
    res = ds.execute('echo "hello from sandbox"')
    print(f"Result: {res['output'].strip()}")
    assert "hello from sandbox" in res['output']
    
    print("Testing copy_to...")
    with open("test_file_local.txt", "w") as f:
        f.write("test content")
    ds.copy_to("test_file_local.txt", "/tmp/test_file_remote.txt")
    
    res = ds.execute("cat /tmp/test_file_remote.txt")
    print(f"Cat result: {res['output'].strip()}")
    assert "test content" in res['output']
    
    print("Testing copy_from...")
    if not os.path.exists("downloaded"):
        os.makedirs("downloaded")
    ds.copy_from("/tmp/test_file_remote.txt", "downloaded")
    
    # tar extractall puts it in its original name or directory structure
    downloaded_path = os.path.join("downloaded", "test_file_remote.txt")
    with open(downloaded_path, "r") as f:
        content = f.read()
        print(f"Downloaded content: {content}")
        assert "test content" in content
    
    print("Cleaning up...")
    ds.stop()
    ds.remove()
    os.remove("test_file_local.txt")
    import shutil
    shutil.rmtree("downloaded")
    print("Verification successful!")

if __name__ == "__main__":
    try:
        test_sandbox()
    except Exception as e:
        print(f"Verification failed: {e}")
        sys.exit(1)
