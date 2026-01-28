import gymnasium as gym
from gymnasium import spaces
import numpy as np
import json
from pydantic import ValidationError
from repogym.actions import ActionWrapper

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

    def reset(self, seed=None, options=None):
        """
        Resets the environment to an initial state.
        """
        super().reset(seed=seed)
        
        self.transcript = "Environment reset."
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
            # Update transcript with action call (Phase 5 will add actual execution results)
            self.transcript += f"\n> Executing: {action_data.action.command}"
            info["action_valid"] = True
            info["action_type"] = action_data.action.command
        except (ValidationError, json.JSONDecodeError) as e:
            self.transcript += f"\n> Error: Invalid action format. {str(e)}"
            reward = -1.0 # Penalty for invalid action format
            info["action_valid"] = False
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
        pass

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
