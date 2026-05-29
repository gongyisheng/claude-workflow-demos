"""CLI / config / serialization dependencies.

One function per dependency: pyyaml (yaml), python-dotenv (dotenv), click,
typer, fire, toml, orjson, msgpack, attrs (attr), environs.
"""

import yaml
from dotenv import load_dotenv, dotenv_values
import click
import typer
import fire
import toml
import orjson
import msgpack
import attr
from environs import Env


def load_yaml(text: str) -> dict:
    """pyyaml: parse a YAML document from a string."""
    return yaml.safe_load(text)


def read_env_file(path: str = ".env") -> dict:
    """python-dotenv: read key/values from a .env file."""
    load_dotenv(path)
    return dict(dotenv_values(path))


def build_click_command():
    """click: define a simple command-line command."""

    @click.command()
    @click.option("--name", default="world")
    def greet(name):
        click.echo(f"hello {name}")

    return greet


def build_typer_app() -> "typer.Typer":
    """typer: define a Typer application with one command."""
    app = typer.Typer()

    @app.command()
    def greet(name: str = "world"):
        typer.echo(f"hello {name}")

    return app


def expose_with_fire(obj=None):
    """fire: expose a callable/object as a CLI (returns the Fire entry)."""
    return lambda: fire.Fire(obj or (lambda name="world": f"hello {name}"))


def load_toml(text: str) -> dict:
    """toml: parse a TOML document from a string."""
    return toml.loads(text)


def dumps_orjson(data) -> bytes:
    """orjson: serialize an object to JSON bytes."""
    return orjson.dumps(data)


def pack_msgpack(data) -> bytes:
    """msgpack: serialize an object to MessagePack bytes."""
    return msgpack.packb(data)


@attr.s(auto_attribs=True)
class Point:
    """attrs: a small value class used by make_point."""

    x: int
    y: int


def make_point(x: int, y: int) -> "Point":
    """attrs: build a Point instance."""
    return Point(x=x, y=y)


def read_environment(prefix: str = "APP_") -> "Env":
    """environs: build an Env reader for parsing environment variables."""
    env = Env()
    env.read_env()
    return env
