from pydantic import BaseModel, Field
from typing import Optional, Dict, List
import os

class TaskPack(BaseModel):
    """
    Metadata for a software engineering task (repository, benchmark, etc.).
    """
    id: str
    name: str
    repo_path_or_url: str
    base_commit: str = "HEAD"
    test_cmd: str = "pytest"
    description: Optional[str] = None

class TaskManager:
    """
    Manages a collection of TaskPacks and handles their retrieval.
    """
    def __init__(self):
        self._tasks: Dict[str, TaskPack] = {}
        self._seed_tasks()

    def _seed_tasks(self):
        """
        Seeds the manager with some default/internal tasks.
        """
        # repogym-internal: Points to the current repository for self-testing
        internal_task = TaskPack(
            id="repogym-internal",
            name="RepoGym Internal",
            repo_path_or_url=".", # Current directory
            base_commit="HEAD",
            test_cmd="pytest tests",
            description="The RepoGym-RL project itself for testing purposes."
        )
        self.add_task(internal_task)

        # bugfix-simple: A simple bugfix task for testing
        bugfix_simple_task = TaskPack(
            id="bugfix-simple",
            name="Simple Bugfix Task",
            repo_path_or_url="tests/data/buggy_repo",
            base_commit="HEAD",
            test_cmd="pytest",
            description="A simple bugfix task for testing purposes."
        )
        self.add_task(bugfix_simple_task)

    def add_task(self, task: TaskPack):
        """
        Adds a new task pack to the manager.
        """
        self._tasks[task.id] = task

    def get_task(self, task_id: str) -> TaskPack:
        """
        Retrieves a task pack by its ID.
        """
        if task_id not in self._tasks:
            raise KeyError(f"Task with ID '{task_id}' not found.")
        return self._tasks[task_id]

    def list_tasks(self) -> List[TaskPack]:
        """
        Lists all available task packs.
        """
        return list(self._tasks.values())
