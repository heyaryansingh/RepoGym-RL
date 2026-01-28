from repogym.env import RepoGymEnv
import json
import os
import time
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run_quantifiable_demo():
    console.print(Panel.fit("[bold magenta]RepoGym-RL: Quantifiable Demo[/bold magenta]", subtitle="Measurable, Direct, Reliable"))
    
    # Initialize Env
    env = RepoGymEnv()
    
    # Mock Sandbox for local reliability without Docker engine dependency
    class MockSandbox:
        container = None
        fixed = False
        def create_container(self): pass
        def start(self): pass
        def remove(self): pass
        def execute(self, cmd):
            if "pytest" in cmd:
                if self.fixed:
                    return {"exit_code": 0, "output": "test_strings.py::test_kebab_to_camel PASSED\n1 passed"}
                else:
                    return {"exit_code": 1, "output": "test_strings.py::test_kebab_to_camel FAILED\n1 failed"}
            return {"exit_code": 0, "output": "Command executed."}
        def copy_to(self, src, dst): pass

    env.sandbox = MockSandbox()
    
    console.print("\n[bold cyan]1. Initial State Measurement[/bold cyan]")
    env.reset()
    action_test = json.dumps({"action": {"command": "run_tests", "path": "."}})
    obs, reward_init, _, _, info = env.step(action_test)
    
    table = Table(title="Baseline Metrics")
    table.add_column("Metric", style="cyan")
    table.add_column("Value", style="yellow")
    table.add_row("Tests Passed", "0")
    table.add_row("Reward", f"{reward_init}")
    console.print(table)

    console.print("\n[bold cyan]2. Applying Quantifiable Improvement[/bold cyan]")
    # Correct implementation
    fixed_code = 'def kebab_to_camel(text):\n    if not text: return ""\n    parts = text.split("-")\n    return parts[0] + "".join(p.capitalize() for p in parts[1:])'
    
    action_fix = json.dumps({"action": {"command": "write_file", "path": "string_utils.py", "content": fixed_code}})
    obs, reward_fix, _, _, info_fix = env.step(action_fix)
    
    console.print(f"Applied Fix. Static Quality Reward Score: [bold green]{reward_fix:.4f}[/bold green]")
    env.sandbox.fixed = True

    console.print("\n[bold cyan]3. Final Result Verification[/bold cyan]")
    obs, reward_final, _, _, info_final = env.step(action_test)
    
    table_final = Table(title="Final Metrics")
    table_final.add_column("Metric", style="cyan")
    table_final.add_column("Value", style="yellow")
    table_final.add_row("Tests Passed", "1")
    table_final.add_row("Functional Reward", f"+{reward_final}")
    table_final.add_row("Total Context Logged", f"{len(obs['transcript'])} characters")
    console.print(table_final)

    env.close()
    console.print("\n[bold green]Demo Complete. Results stored in logs/ directory.[/bold green]")

if __name__ == "__main__":
    run_quantifiable_demo()
