import typer
from typing import Annotated
from rich import print

hello_app = typer.Typer()

@hello_app.command(help="[red][bold]Greet[/red][bold] user by name")
def hello(name: Annotated[str, typer.Argument(help="Name to greet")]):
    print(f"Hello, [bold][green]{name}[/green][/bold]!")