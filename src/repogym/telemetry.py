from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
import time
import json
import os

class StepLog(BaseModel):
    """
    Represents a single step in an episode.
    """
    timestamp: float = Field(default_factory=time.time)
    step: int
    action: str
    reward: float
    info: Dict[str, Any]
    observation_summary: Optional[str] = None

class EpisodeLogger:
    """
    Collects steps and metadata for a single episode.
    """
    def __init__(self, episode_id: str, task_id: Optional[str] = None):
        self.episode_id = episode_id
        self.task_id = task_id
        self.steps: List[StepLog] = []
        self.start_time = time.time()
        self.metadata: Dict[str, Any] = {
            "episode_id": episode_id,
            "task_id": task_id,
            "start_time": self.start_time
        }

    def log_step(self, step: int, action: str, reward: float, info: Dict[str, Any], observation_summary: Optional[str] = None):
        """
        Adds a step log entry.
        """
        log_entry = StepLog(
            step=step,
            action=action,
            reward=reward,
            info=info,
            observation_summary=observation_summary
        )
        self.steps.append(log_entry)

    def get_trajectory(self) -> List[Dict[str, Any]]:
        """
        Returns the episode trajectory as a list of dictionaries.
        """
        return [step.model_dump() for step in self.steps]

    def write_jsonl(self, file_path: str):
        """
        Writes the episode trajectory to a JSONL file.
        The first line is metadata, subsequent lines are steps.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            # Metadata
            f.write(json.dumps(self.metadata) + "\n")
            # Steps
            for step in self.steps:
                f.write(step.model_dump_json() + "\n")
