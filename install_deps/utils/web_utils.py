"""Web framework / API dependencies.

One function per dependency: fastapi, flask, starlette, uvicorn, gunicorn,
pydantic, marshmallow, strawberry.
"""

from fastapi import FastAPI
from flask import Flask
from starlette.applications import Starlette
import uvicorn
import gunicorn
from pydantic import BaseModel
from marshmallow import Schema, fields
import strawberry


def create_fastapi_app() -> "FastAPI":
    """fastapi: build an app with a single health route."""
    app = FastAPI()

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


def create_flask_app() -> "Flask":
    """flask: build an app with a single health route."""
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


def create_starlette_app() -> "Starlette":
    """starlette: build a bare Starlette app."""
    return Starlette(debug=True)


def uvicorn_config(app) -> "uvicorn.Config":
    """uvicorn: build a server config (without running it)."""
    return uvicorn.Config(app, host="127.0.0.1", port=8000)


def gunicorn_version() -> str:
    """gunicorn: report the installed gunicorn version."""
    return gunicorn.__version__


class Item(BaseModel):
    """pydantic: a validated model used by parse_item."""

    id: int
    name: str


def parse_item(data: dict) -> "Item":
    """pydantic: validate a dict into an Item model."""
    return Item(**data)


class ItemSchema(Schema):
    """marshmallow: a serialization schema used by dump_item."""

    id = fields.Int()
    name = fields.Str()


def dump_item(data: dict) -> dict:
    """marshmallow: serialize a dict through ItemSchema."""
    return ItemSchema().dump(data)


@strawberry.type
class Query:
    """strawberry: a GraphQL query type used by build_graphql_schema."""

    @strawberry.field
    def hello(self) -> str:
        return "world"


def build_graphql_schema():
    """strawberry: build a GraphQL schema from the Query type."""
    return strawberry.Schema(query=Query)
