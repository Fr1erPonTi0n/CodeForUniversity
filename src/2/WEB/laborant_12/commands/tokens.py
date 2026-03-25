import typer
from typing import Annotated
from rich.markdown import Markdown
from rich import print
from api.api_v1.auth.service.redis_tokens_helper import redis_tokens

tokens_app = typer.Typer(
    name="token",
)


@tokens_app.command(help="Checking the token's validity-whether it exists or not")
def check(
    token: Annotated[str, typer.Argument(help="Token for verification")]
):
    if redis_tokens.token_exists(token):
        print(f"Token [bold]{token}[/bold][green] exists[/green]")
    else:
        print(f"Токен [bold]{token}[/bold][red] does not exist[/red]")


@tokens_app.command(help="Get list tokens")
def list():
    tokens = redis_tokens.get_tokens()
    if not tokens:
        print("[yellow]Tokens not found[/yellow]")
        return
    markdown_text = f"""# Available API Tokens\n"""
    for token in tokens:
        markdown_text += f"- {token}\n"
    print(Markdown(markdown_text))


@tokens_app.command(help="Create a new token and add to storage")
def create():
    token = redis_tokens.generate_and_save_token()
    print(f"[green]The new token has been successfully created![/green]")
    print(f"[bold]Token:[/bold] [yellow]{token}[/yellow]")


@tokens_app.command(help="Token to add")
def add(
    token: Annotated[str, typer.Argument(help="Token to add")]
):
    if redis_tokens.token_exists(token):
        print(f"Token [bold]{token}[/bold][red] exists[/red]")
        return
    redis_tokens.add_token(token)
    print("Token [bold]{token}[/bold][green] successfully created[/green]")


@tokens_app.command(help="Delete by token")
def rm(
    token: Annotated[str, typer.Argument(help="Token to delete")]
):
    if not redis_tokens.token_exists(token):
        print(f"Token [bold]{token}[/bold][red] does not exists[/red]")
        return
    redis_tokens.delete_token(token)
    print(f"[green]Token [bold]{token}[/bold] successfully deleted[/green]")