import typer
from commands.hello import hello_app
from commands.tokens import tokens_app

app = typer.Typer(
    no_args_is_help=True,
    rich_markup_mode='rich'
)

@app.callback()
def callback():
    """
    This is a sample CLI application.
    """
    pass

app.add_typer(hello_app)
app.add_typer(tokens_app)