"""Task queue / scheduling dependencies.

One function per dependency: celery, apscheduler.
"""

from celery import Celery
from apscheduler.schedulers.background import BackgroundScheduler


def make_celery_app(name: str = "demo", broker: str = "memory://") -> "Celery":
    """celery: build a Celery app with an in-memory broker."""
    app = Celery(name, broker=broker)

    @app.task
    def add(a, b):
        return a + b

    return app


def make_scheduler() -> "BackgroundScheduler":
    """apscheduler: build a background scheduler with a sample job."""
    scheduler = BackgroundScheduler()
    scheduler.add_job(lambda: None, "interval", seconds=60)
    return scheduler
