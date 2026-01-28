import json
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def run_inspect(log_file: str):
    console.print(f"[bold blue]Inspecting log:[/bold blue] {log_file}")
    
    with open(log_file, "r") as f:
        lines = f.readlines()
        
    if not lines:
        console.print("[red]Log file is empty.[/red]")
        return
        
    # Metadata
    metadata = json.loads(lines[0])
    console.print(Panel(json.dumps(metadata, indent=2), title="Episode Metadata"))
    
    # Table of steps
    table = Table(title="Trajectory Summary")
    table.add_column("Step", justify="right", style="cyan")
    table.add_column("Command", style="magenta")
    table.add_column("Reward", justify="right", style="green")
    table.add_column("Action Valid", style="yellow")
    
    total_reward = 0.0
    for line in lines[1:]:
        step_data = json.loads(line)
        action_json = json.loads(step_data["action"])
        cmd = action_json.get("action", {}).get("command", "unknown")
        
        table.add_row(
            str(step_data["step"]),
            cmd,
            f"{step_data['reward']:.2f}",
            str(step_data["info"].get("action_valid", "N/A"))
        )
        total_reward += step_data["reward"]
        
    console.print(table)
    console.print(f"\n[bold green]Total Cumulative Reward:[/bold green] {total_reward:.2f}")
