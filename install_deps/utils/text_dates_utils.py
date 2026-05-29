"""Templating / dates / text-utility dependencies.

One function per dependency: jinja2, python-dateutil (dateutil), pendulum,
arrow, humanize, tabulate, faker, validators, phonenumbers.
"""

from jinja2 import Template
from dateutil import parser as date_parser
import pendulum
import arrow
import humanize
import tabulate as tabulate_mod
from faker import Faker
import validators
import phonenumbers


def render_template(template_str: str, **kwargs) -> str:
    """jinja2: render a template string with the given context."""
    return Template(template_str).render(**kwargs)


def parse_date(text: str):
    """python-dateutil: parse a free-form date string."""
    return date_parser.parse(text)


def now_pendulum():
    """pendulum: return the current time as a pendulum datetime."""
    return pendulum.now()


def now_arrow():
    """arrow: return the current time as an arrow datetime."""
    return arrow.now()


def humanize_count(n: int) -> str:
    """humanize: render an integer with thousands separators as words-ish."""
    return humanize.intcomma(n)


def tabulate_rows(rows: list[dict]) -> str:
    """tabulate: render a list of dicts as an ASCII table."""
    if not rows:
        return ""
    return tabulate_mod.tabulate(rows, headers="keys")


def fake_records(n: int = 5) -> list[dict]:
    """faker: generate fake person records."""
    fake = Faker()
    return [{"name": fake.name(), "email": fake.email()} for _ in range(n)]


def is_valid_email(value: str) -> bool:
    """validators: validate an email address."""
    return bool(validators.email(value))


def parse_phone(number: str, region: str = "US"):
    """phonenumbers: parse a phone number for a region."""
    return phonenumbers.parse(number, region)
