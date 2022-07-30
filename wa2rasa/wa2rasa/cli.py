import json
from typing import Optional

import typer
from rich.console import Console

from wa2rasa import read_wa_object

app = typer.Typer(name="wa2rasa", 
    add_completion=False, 
    help="Convert Watson Assistant skill object to rasa nlu.yml file.")

console = Console()

@app.command()
def introduce_app(name: str = typer.Argument("bro", help="Your name.")):
    """App intro."""
    console.print(
        f"Hey {name}! This app helps you to convert your watson Assistant skill object to rasa nlu.yml file. For that, use the argument 'convert'.",
        style="green"
    )

@app.command()
def convert(wa_file: str = typer.Argument(..., help="The path to your Watson Assistant json file."),
            save_in: str = typer.Argument(..., help="Path to the directory where you want to store the output.")):
    """
    Convert Watson Assistant skill object to rasa nlu.yml file.
    """
    wa_object = read_wa_object(file_path=wa_file)
    # Do pipeline here

    # output
    print(json.dumps(wa_object, sort_keys=False, indent=2))
    print(f"Output saved in {save_in}")

if __name__ == "__main__":
    app()