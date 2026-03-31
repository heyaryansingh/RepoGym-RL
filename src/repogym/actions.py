"""Action models for the RepoGym environment.

This module defines Pydantic models for all actions that an agent can take
within the RepoGym RL environment. Actions are parsed as discriminated unions
based on the `command` field.
"""

from typing import Literal, Optional, Union

from pydantic import BaseModel, Field


class ListFiles(BaseModel):
    """Action to list files in a directory."""

    command: Literal["list_files"] = "list_files"
    path: str = Field(description="The directory path to list files from.")


class ReadFile(BaseModel):
    """Action to read the contents of a file."""

    command: Literal["read_file"] = "read_file"
    path: str = Field(description="The path of the file to read.")


class WriteFile(BaseModel):
    """Action to write content to a file."""

    command: Literal["write_file"] = "write_file"
    path: str = Field(description="The path of the file to write to.")
    content: str = Field(description="The content to write to the file.")


class RunTests(BaseModel):
    """Action to run tests in the repository."""

    command: Literal["run_tests"] = "run_tests"
    path: Optional[str] = Field(
        default=None, description="The path to the test file or directory."
    )


class RunCommand(BaseModel):
    """Action to execute a shell command."""

    command: Literal["run_command"] = "run_command"
    cmd: str = Field(description="The shell command to execute.")


#: Union type for discriminated union parsing of all action types
Action = Union[ListFiles, ReadFile, WriteFile, RunTests, RunCommand]


class ActionWrapper(BaseModel):
    """Wrapper to handle discriminated union parsing of actions.

    This wrapper is used to parse JSON/dict input into the appropriate
    action model based on the `command` discriminator field.
    """

    action: Action
