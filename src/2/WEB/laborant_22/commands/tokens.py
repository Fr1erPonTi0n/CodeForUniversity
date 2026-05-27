from typing import Annotated
from rich import print
from api.api_v1.auth.services.redis_tokens_helper import redis_tokens
from rich.markdown import Markdown


import typer


app = typer.Typer(
    help="Tokens management",
    name="token",
    rich_markup_mode="rich",
    no_args_is_help=True,
)


@app.command(help="Checking the token's validity—whether it exists or not.")
def check(
    token: Annotated[
        str,
        typer.Argument(
            help="Token to check.",
        ),
    ],
):
    if redis_tokens.token_exists(token=token):
        print(f"Token [bold]{token}[/bold] [green]exists[/green]")
    else:
        print(f"Token [bold]{token}[/bold] [red]does not exist.[/red]")


@app.command(
    help="Get list tokens",
    name="list",
)
def list_tokens():
    print(Markdown("# Available API Tokens"))
    print(Markdown("\n- ".join([""] + redis_tokens.get_tokens())))
    print()


@app.command(
    help="Delete by token",
    name="rm",
)
def delete_tokens(
    token: Annotated[
        str,
        typer.Argument(help="Token to delete."),
    ],
):
    if redis_tokens.delete_token(token=token):
        print(f"Token [bold]{token}[/bold] deleted.")
    else:
        print(f"Token [bold]{token}[/bold] [red]does not exist.[/red]")


@app.command(
    help="Create new token and add to storage",
    name="create",
)
def create_new_token():
    print(f"Token {redis_tokens.generate_and_save_token()} added successful.")


@app.command(
    help="Token to add",
    name="add",
)
def add_token(
    token: Annotated[
        str,
        typer.Argument(),
    ],
):
    redis_tokens.add_token(token)
    print(f"Token {token} added successful.")
