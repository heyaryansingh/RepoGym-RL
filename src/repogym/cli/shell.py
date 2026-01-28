import json
from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from repogym.env import RepoGymEnv

console = Console()

def run_shell(task_id: str = None):
    console.print(Panel("[bold green]RepoGym Interactive Shell[/bold green]\nEnter JSON actions to interact with the environment. Type 'exit' to quit."))
    
    env = RepoGymEnv(render_mode="human")
    obs, info = env.reset(options={"task_id": task_id} if task_id else None)
    
    while True:
        try:
            user_input = console.input("\n[bold cyan]Action (JSON):[/bold cyan] ").strip()
            if user_input.lower() in ["exit", "quit"]:
                break
            
            # Allow short-hands or assume JSON
            if not user_input.startswith("{"):
                console.print("[yellow]Hint: Action must be a JSON string like {\"action\": {\"command\": \"list_files\", \"path\": \".\"}}[/yellow]")
                continue

            obs, reward, terminated, truncated, info = env.step(user_input)
            
            console.print(f"\n[bold green]Reward:[/bold green] {reward}")
            if info:
                console.print("[bold yellow]Info:[/bold yellow]")
                console.print(info)
            
            # Print last part of transcript
            lines = obs["transcript"].splitlines()
            last_lines = "\n".join(lines[-10:])
            console.print(Panel(last_lines, title="Transcript (Last 10 lines)"))
            
            if terminated or truncated:
                console.print("[bold red]Episode Ended.[/bold red]")
                break
                
        except KeyboardInterrupt:
            break
        except Exception as e:
            console.print(f"[bold red]CLI Error:[/bold red] {str(e)}")
            
    env.close()
    console.print("[bold blue]Environment closed.[/bold blue]")
