"""Database / ORM dependencies.

One function per dependency: sqlalchemy, redis, pymongo, psycopg2, pymysql,
elasticsearch, peewee.
"""

import sqlalchemy
from sqlalchemy import create_engine, text
import redis
import pymongo
import psycopg2
import pymysql
from elasticsearch import Elasticsearch
import peewee


def create_sqlite_engine(url: str = "sqlite:///:memory:"):
    """sqlalchemy: create an in-memory SQLite engine and run a query."""
    engine = create_engine(url)
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))
    return engine


def redis_client(host: str = "localhost", port: int = 6379) -> "redis.Redis":
    """redis: build a Redis client (no connection made until used)."""
    return redis.Redis(host=host, port=port, db=0)


def mongo_client(uri: str = "mongodb://localhost:27017") -> "pymongo.MongoClient":
    """pymongo: build a MongoDB client."""
    return pymongo.MongoClient(uri)


def postgres_dsn(host: str = "localhost", db: str = "postgres") -> str:
    """psycopg2: build a connection string (connection is lazy)."""
    # psycopg2.connect would be called with this DSN against a live server.
    _ = psycopg2.connect  # reference the entrypoint
    return f"host={host} dbname={db}"


def mysql_connect_kwargs(host: str = "localhost", db: str = "mysql") -> dict:
    """pymysql: build connect kwargs (connection is lazy)."""
    _ = pymysql.connect  # reference the entrypoint
    return {"host": host, "database": db}


def elasticsearch_client(url: str = "http://localhost:9200") -> "Elasticsearch":
    """elasticsearch: build an Elasticsearch client."""
    return Elasticsearch(url)


def define_peewee_model():
    """peewee: define an ORM model bound to an in-memory SQLite db."""
    db = peewee.SqliteDatabase(":memory:")

    class User(peewee.Model):
        name = peewee.CharField()

        class Meta:
            database = db

    return User
