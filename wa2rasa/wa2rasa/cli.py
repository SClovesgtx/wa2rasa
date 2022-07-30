import json
import pathlib

import typer
from rich.console import Console
from rich.theme import Theme

from wa2rasa import read_wa_object, intents_parser, entities_parser, save_rasa_yaml_file

app = typer.Typer(
    name="wa2rasa",
    add_completion=False,
    help="Convert Watson Assistant skill object to rasa nlu.yml file.",
)

custom_theme = Theme({"info": "dim cyan", "warning": "magenta", "danger": "bold red"})
console = Console(theme=custom_theme)


@app.command()
def introduce_app(name: str = typer.Argument("bro", help="Your name.")):
    """App intro."""
    console.print(
        f"Hey {name}! This app helps you to convert your watson Assistant skill object to rasa nlu.yml file. For that, use the argument 'convert'.",
        style="info",
    )


@app.command()
def convert(
    wa_file: str = typer.Argument(
        ..., help="The path to your Watson Assistant json file."
    ),
    save_in: str = typer.Argument(
        ..., help="Path to the directory where you want to store the output."
    ),
    rasa_version: str = typer.Argument("3.1", help="The version of your rasa app."),
):
    """
    Convert Watson Assistant skill object to rasa nlu.yml file.
    """
    wa_object = read_wa_object(file_path=wa_file)
    intents = wa_object.get("intents", [])
    entities = wa_object.get("entities", [])
    if intents:
        intents = intents_parser(intents)
    if entities:
        entities = entities_parser(entities)
    nlu_yml_obj = {"version": rasa_version, "nlu": intents + entities}
    if not entities:
        console.print(
            "[warning]Warning: No entity found in your Watson Assistant object.[/warning]"
        )
    if not intents:
        console.print(
            "[warning]Warning: No entities found in your Watson Assistant object.[/warning]"
        )
    file_path = pathlib.Path(save_in, "nlu.yml")
    save_rasa_yaml_file(file_path=file_path, object=nlu_yml_obj)
    console.print(f"Output saved in '{file_path}'.", style="info")


if __name__ == "__main__":
    app()
