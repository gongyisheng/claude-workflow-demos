"""Plotting / visualization dependencies.

One function per dependency: matplotlib, seaborn, plotly, altair, bokeh.
"""

import matplotlib
matplotlib.use("Agg")  # headless backend for demo
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt
import bokeh.plotting as bk
import pandas as pd


def save_line_plot(values, path: str = "line.png") -> str:
    """matplotlib: render a line plot to a PNG file."""
    fig, ax = plt.subplots()
    ax.plot(list(values))
    fig.savefig(path)
    plt.close(fig)
    return path


def save_histogram(values, path: str = "hist.png") -> str:
    """seaborn: render a histogram to a PNG file."""
    fig, ax = plt.subplots()
    sns.histplot(list(values), ax=ax)
    fig.savefig(path)
    plt.close(fig)
    return path


def scatter_figure(df: "pd.DataFrame"):
    """plotly: build an interactive scatter figure."""
    return px.scatter(df, x="id", y="value", color="category")


def altair_chart(df: "pd.DataFrame"):
    """altair: build a declarative scatter chart."""
    return alt.Chart(df).mark_point().encode(x="id", y="value", color="category")


def bokeh_figure(df: "pd.DataFrame"):
    """bokeh: build a scatter figure."""
    fig = bk.figure(title="demo")
    fig.scatter(list(df["id"]), list(df["value"]))
    return fig
