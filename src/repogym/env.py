import gymnasium as gym
from gymnasium import spaces
import numpy as np
import json
import os
import time
from pydantic import ValidationError
from repogym.actions import ActionWrapper

from repogym.tasks import TaskManager
from repogym.sandbox.docker import DockerSandbox

class RepoGymEnv(gym.Env):
    """
    A local-first, containerized reinforcement learning environment for software engineering tasks.
    """
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self, render_mode=None):
        super(RepoGymEnv, self).__init__()
        
        # Placeholder spaces: will be refined in Phase 5 (Lifecycle)
        self.observation_space = spaces.Dict({
            "transcript": spaces.Text(min_length=0, max_length=100000), # Increased limit
            "working_directory": spaces.Text(min_length=0, max_length=1000),
        })
        
        # Action space: JSON string tool calls
        self.action_space = spaces.Text(min_length=0, max_length=10000)
        
        self.render_mode = render_mode
        self.transcript = "Repository initialized. Ready for agent actions."
        self.task_manager = TaskManager()
        self.current_task = None
        self.sandbox = DockerSandbox()

    def reset(self, seed=None, options=None):
        """
        Resets the environment to an initial state.
        """
        super().reset(seed=seed)
        
        self.transcript = "Environment reset."
        
        # Cleanup existing sandbox
        if self.sandbox.container:
            self.sandbox.remove()
        
        # Select task if provided in options
        if options and "task_id" in options:
            try:
                self.current_task = self.task_manager.get_task(options["task_id"])
                self.transcript += f" Loaded task: {self.current_task.name}"
            except KeyError as e:
                self.transcript += f"\n> Warning: Failed to load task. {str(e)}"
        
        # Orchestrate sandbox
        self.sandbox.create_container()
        self.sandbox.start()
        
        # If a task is loaded, copy it into the sandbox
        if self.current_task:
            self.transcript += f"\nDeploying task {self.current_task.id} to sandbox..."
            try:
                self.sandbox.copy_to(self.current_task.repo_path_or_url, "/workspace")
                self.transcript += " Done."
            except Exception as e:
                self.transcript += f" Failed: {str(e)}"
        
        observation = self._get_obs()
        info = self._get_info()
        
        if self.render_mode == "human":
            self.render()
            
        return observation, info

    def step(self, action: str):
        """
        Executes one timestep within the environment.
        """
        reward = 0.0
        terminated = False
        truncated = False
        info = {}

        try:
            # Dispatch action
            action_data = self._dispatch_action(action)
            action_obj = action_data.action
            
            self.transcript += f"\n> Executing: {action_obj.command}"
            
            # Route to sandbox
            res = None
            if action_obj.command == "list_files":
                res = self.sandbox.execute(f"ls -R {action_obj.path}")
            elif action_obj.command == "read_file":
                res = self.sandbox.execute(f"cat {action_obj.path}")
            elif action_obj.command == "write_file":
                # Create a temporary file locally to copy it to the sandbox
                # This is a bit hacky but works with our current copy_to implementation
                temp_filename = f"temp_{int(time.time())}.txt"
                with open(temp_filename, "w") as f:
                    f.write(action_obj.content)
                self.sandbox.copy_to(temp_filename, action_obj.path)
                os.remove(temp_filename)
                res = {"exit_code": 0, "output": f"File {action_obj.path} written successfully."}
            elif action_obj.command == "run_tests":
                test_path = action_obj.path if action_obj.path else "."
                cmd = f"pytest {test_path}" # Simple default, could come from TaskPack
                res = self.sandbox.execute(cmd)
            elif action_obj.command == "run_command":
                res = self.sandbox.execute(action_obj.cmd)
            
            if res:
                output = res["output"] if isinstance(res, dict) else res.output
                exit_code = res["exit_code"] if isinstance(res, dict) else res.exit_code
                self.transcript += f"\nOutput (exit {exit_code}):\n{output}"
                info["exit_code"] = exit_code

            info["action_valid"] = True
            info["action_type"] = action_obj.command
            
        except (ValidationError, json.JSONDecodeError) as e:
            self.transcript += f"\n> Error: Invalid action format. {str(e)}"
            reward = -1.0 # Penalty for invalid action format
            info["action_valid"] = False
            info["error"] = str(e)
        except Exception as e:
            self.transcript += f"\n> Error: Execution failed. {str(e)}"
            reward = -0.5 # Penalty for system/execution errors
            info["action_valid"] = True # It was a valid attempt, but failed
            info["error"] = str(e)
        
        observation = self._get_obs()
        info.update(self._get_info())
        
        return observation, reward, terminated, truncated, info

    def render(self):
        """
        Renders the environment state.
        """
        if self.render_mode == "human":
            print(f"--- Transcript ---\n{self.transcript}\n-------------------")

    def close(self):
        """
        Closes the environment and releases resources.
        """
        if self.sandbox:
            self.sandbox.remove()

    def _dispatch_action(self, action_str: str) -> ActionWrapper:
        """
        Parses and validates the action JSON string.
        """
        # Pydantic handles the union via ActionWrapper
        return ActionWrapper.model_validate_json(action_str)

    def _get_obs(self):
        """
        Generates the current observation.
        """
        return {
            "transcript": self.transcript,
            "working_directory": "/workspace"
        }

    def _get_info(self):
        """
        Generates auxiliary diagnostic information.
        """
        return {}
