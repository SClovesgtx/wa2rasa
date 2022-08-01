import os

from importlib.resources import path
from typer.testing import CliRunner
import pathlib

from wa2rasa import __version__
from wa2rasa.cli import app

runner = CliRunner()


def test_version():
    assert __version__ == "0.1.2"


def test_introduce_app():
    result = runner.invoke(app, ["introduce-app", "Cloves"])
    assert result.exit_code == 0
    assert "Cloves" in result.stdout


def test_convert_command():
    source = pathlib.Path("wa2rasa", "wa2rasa", "wa_example", "My-WA-Skill-dialog.json")
    dest = pathlib.Path("wa2rasa", "wa2rasa", "my_rasa_dir")
    result = runner.invoke(
        app, ["convert", str(source.absolute()), str(dest.absolute())]
    )
    assert result.exit_code == 0
    saved_in = str(pathlib.Path(dest, "nlu.yml").absolute())
    assert result.stdout == f"Output saved in '{saved_in}'.\n"
