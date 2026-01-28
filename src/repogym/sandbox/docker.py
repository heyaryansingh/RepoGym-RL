import docker
import logging
import os
import tarfile
import io
import time
from typing import Optional, Dict, Any, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DockerSandbox:
    """
    Manages Docker container lifecycle and interaction for isolated execution.
    """
    DEFAULT_IMAGE = "python:3.11-slim"
    DEFAULT_MEM_LIMIT = "512m"
    DEFAULT_NANO_CPUS = 1000000000  # 1 CPU

    def __init__(self):
        self.client = None
        try:
            self.client = docker.from_env()
            # Test connection
            self.client.ping()
            logger.info("Docker client initialized successfully from environment.")
        except Exception:
            logger.warning("Failed to initialize Docker from environment. Trying common Windows pipes...")
            
            common_pipes = [
                "npipe:////./pipe/docker_engine",
                "npipe:////./pipe/dockerDesktopLinuxEngine",
                "npipe:////./pipe/dockerDesktopEngine"
            ]
            
            for pipe in common_pipes:
                try:
                    logger.info(f"Attempting to connect to {pipe}")
                    self.client = docker.DockerClient(base_url=pipe)
                    self.client.ping()
                    logger.info(f"Connected to Docker via {pipe}")
                    return
                except Exception:
                    continue
            
            logger.error("Failed to connect to Docker engine after multiple attempts.")
            # Do not raise here to allow instantiation of Env for mocks/testing
            # Methods that require the client will still fail correctly later.

        self.container = None

    def create_container(
        self, 
        image: str = DEFAULT_IMAGE, 
        command: Optional[str] = None,
        working_dir: str = "/workspace",
        **kwargs
    ):
        """
        Creates a new Docker container.
        """
        logger.info(f"Creating container with image: {image}")
        try:
            self.container = self.client.containers.create(
                image=image,
                command=command,
                working_dir=working_dir,
                mem_limit=kwargs.get("mem_limit", self.DEFAULT_MEM_LIMIT),
                nano_cpus=kwargs.get("nano_cpus", self.DEFAULT_NANO_CPUS),
                detach=True,
                tty=True, # Keep it open
                **kwargs
            )
            logger.info(f"Container created: {self.container.id[:12]}")
            return self.container
        except Exception as e:
            logger.error(f"Failed to create container: {e}")
            raise

    def start(self):
        """
        Starts the created container.
        """
        if not self.container:
            raise RuntimeError("No container created. Call create_container first.")
        
        logger.info(f"Starting container: {self.container.id[:12]}")
        try:
            self.container.start()
        except Exception as e:
            logger.error(f"Failed to start container: {e}")
            raise

    def stop(self, timeout: int = 10):
        """
        Stops the container.
        """
        if self.container:
            logger.info(f"Stopping container: {self.container.id[:12]}")
            try:
                self.container.stop(timeout=timeout)
            except Exception as e:
                logger.error(f"Failed to stop container: {e}")

    def remove(self, v: bool = True, force: bool = True):
        """
        Removes the container.
        """
        if self.container:
            logger.info(f"Removing container: {self.container.id[:12]}")
            try:
                self.container.remove(v=v, force=force)
                self.container = None
            except Exception as e:
                logger.error(f"Failed to remove container: {e}")

    def execute(self, command: str, workdir: Optional[str] = None) -> Dict[str, Any]:
        """
        Executes a command inside the container.
        """
        if not self.container:
            raise RuntimeError("Container not created or started.")

        logger.info(f"Executing command: {command}")
        try:
            exec_res = self.container.exec_run(command, workdir=workdir)
            return {
                "exit_code": exec_res.exit_code,
                "output": exec_res.output.decode("utf-8") if exec_res.output else ""
            }
        except Exception as e:
            logger.error(f"Execution failed: {e}")
            raise

    def copy_to(self, local_path: str, remote_path: str):
        """
        Copies a file or directory to the container.
        """
        if not self.container:
            raise RuntimeError("Container not created or started.")

        logger.info(f"Copying {local_path} to {remote_path}")
        
        # Docker SDK requires a tar archive for put_archive
        stream = io.BytesIO()
        with tarfile.open(fileobj=stream, mode='w') as tar:
            tar.add(local_path, arcname=os.path.basename(local_path))
        
        stream.seek(0)
        try:
            self.container.put_archive(os.path.dirname(remote_path), stream)
        except Exception as e:
            logger.error(f"Failed to copy file to container: {e}")
            raise

    def copy_from(self, remote_path: str, local_path: str):
        """
        Copies a file or directory from the container.
        """
        if not self.container:
            raise RuntimeError("Container not created or started.")

        logger.info(f"Copying {remote_path} from container to {local_path}")
        try:
            bits, stat = self.container.get_archive(remote_path)
            stream = io.BytesIO()
            for chunk in bits:
                stream.write(chunk)
            stream.seek(0)
            
            with tarfile.open(fileobj=stream, mode='r') as tar:
                tar.extractall(path=local_path)
        except Exception as e:
            logger.error(f"Failed to copy file from container: {e}")
            raise
