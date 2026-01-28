from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, Union, Literal

class ListFiles(BaseModel):
    command: Literal["list_files"] = "list_files"
    path: str = Field(description="The directory path to list files from.")

class ReadFile(BaseModel):
    command: Literal["read_file"] = "read_file"
    path: str = Field(description="The path of the file to read.")

class WriteFile(BaseModel):
    command: Literal["write_file"] = "write_file"
    path: str = Field(description="The path of the file to write to.")
    content: str = Field(description="The content to write to the file.")

class RunTests(BaseModel):
    command: Literal["run_tests"] = "run_tests"
    path: Optional[str] = Field(default=None, description="The path to the test file or directory.")

class RunCommand(BaseModel):
    command: Literal["run_command"] = "run_command"
    cmd: str = Field(description="The shell command to execute.")

# Union type for discriminated union parsing
Action = Union[ListFiles, ReadFile, WriteFile, RunTests, RunCommand]

class ActionWrapper(BaseModel):
    """
    Wrapper to handle discriminated union parsing of actions.
    """
    action: Action
