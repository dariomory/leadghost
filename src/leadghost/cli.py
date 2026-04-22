"""Console script for leadghost."""

import typer
from rich.console import Console

app = typer.Typer()
console = Console()


@app.command()
def main() -> None:
    """Run LeadGhost - LinkedIn lead generation automation tool."""
    console.print("[bold blue]LeadGhost[/bold blue] - LinkedIn lead generation tool")
    console.print("Run 'leadghost' to start the interactive bot.")
    console.print("")
    console.print("For configuration, edit config.txt before running.")


@app.command()
def run() -> None:
    """Run the LeadGhost bot in interactive or automatic mode."""
    from leadghost.bot import Bot

    bot = Bot()
    while True:
        bot.run()


if __name__ == "__main__":
    app()
