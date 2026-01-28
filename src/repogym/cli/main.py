import click
from rich.console import Console

console = Console()

@click.group()
def main():
    """RepoGym-RL Developer Tools."""
    pass

@main.command()
@click.option("--task", "task_id", help="Task ID to load.")
def shell(task_id):
    """Start an interactive environment shell."""
    from repogym.cli.shell import run_shell
    run_shell(task_id)

@main.command()
@click.argument("log_file", type=click.Path(exists=True))
def inspect(log_file):
    """Inspect an episode log file."""
    from repogym.cli.inspector import run_inspect
    run_inspect(log_file)

if __name__ == "__main__":
    main()
