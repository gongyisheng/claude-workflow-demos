#!/usr/bin/env python3
from utils import (
    numerical_utils,
    plotting_utils,
    classic_ml_utils,
    deep_learning_utils,
    vision_utils,
    http_scraping_utils,
    web_utils,
    cli_config_utils,
    databases_utils,
    cloud_utils,
    tasks_utils,
    text_dates_utils,
    security_utils,
    observability_utils,
    ai_sdks_utils,
)


def summarize(df) -> dict:
    """Return basic summary stats for a dataframe."""
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "mean_value": float(df["value"].mean()),
        "std_value": float(df["value"].std()),
    }


def main() -> None:
    console = observability_utils.console
    console.print("[bold green]Demo script loaded successfully.[/bold green]")
    console.print(f"system: {observability_utils.system_stats()}")

    df = numerical_utils.make_dataframe(50)
    console.print(summarize(df))

    fig = plotting_utils.scatter_figure(df)
    console.print(f"plotly figure: {type(fig).__name__}")

    model = classic_ml_utils.train_linear(df)
    console.print(f"linear coef: {float(model.coef_[0]):.4f}")

    console.print(f"torch sum: {deep_learning_utils.torch_tensor_sum([1, 2, 3]):.1f}")

    gray = vision_utils.to_grayscale(vision_utils.random_rgb_image())
    console.print(f"grayscale shape: {gray.shape}")

    links = http_scraping_utils.parse_links('<a href="/a">a</a><a href="/b">b</a>')
    console.print(f"parsed links: {links}")

    app = web_utils.create_fastapi_app()
    console.print(f"fastapi routes: {len(app.routes)}")

    console.print(f"yaml: {cli_config_utils.load_yaml('name: demo\ncount: 3')}")

    engine = databases_utils.create_sqlite_engine()
    console.print(f"sqlalchemy engine: {engine.dialect.name}")

    s3 = cloud_utils.s3_client()
    console.print(f"boto3 client: {s3.meta.service_model.service_name}")

    celery_app = tasks_utils.make_celery_app()
    console.print(f"celery app: {celery_app.main}")

    records = text_dates_utils.fake_records(5)
    observability_utils.print_table(records)

    console.print(f"fernet roundtrip: {security_utils.fernet_roundtrip('hello')}")

    console.print(f"langchain version: {ai_sdks_utils.langchain_version()}")


if __name__ == "__main__":
    main()
