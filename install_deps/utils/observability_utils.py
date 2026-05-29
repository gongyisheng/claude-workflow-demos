"""Logging / observability / system dependencies.

One function per dependency: tqdm, rich, loguru, structlog, psutil.
"""

from tqdm import tqdm
from rich.console import Console
from rich.table import Table
from loguru import logger as loguru_logger
import structlog
import psutil


console = Console()


def progress_sum(n: int = 100) -> int:
    """tqdm: iterate with a progress bar and accumulate a sum."""
    total = 0
    for i in tqdm(range(n), disable=True):
        total += i
    return total


def print_table(rows: list[dict]) -> None:
    """rich: pretty-print a list of dicts as a table."""
    if not rows:
        return
    table = Table(*rows[0].keys())
    for row in rows:
        table.add_row(*[str(v) for v in row.values()])
    console.print(table)


def get_loguru_logger():
    """loguru: return the configured loguru logger."""
    return loguru_logger


def get_structlog_logger():
    """structlog: return a bound structlog logger."""
    return structlog.get_logger()


def system_stats() -> dict:
    """psutil: report basic CPU/memory utilization."""
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
    }
