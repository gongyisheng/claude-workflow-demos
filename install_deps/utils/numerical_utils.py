"""Numerical / scientific computing dependencies.

One function per dependency: numpy, pandas, scipy, statsmodels, sympy,
networkx, numba, dask, polars, pyarrow, duckdb, h5py, openpyxl.
"""

from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import scipy.stats as stats
import statsmodels.api as sm
import sympy
import networkx as nx
import numba
import dask.dataframe as dd
import polars as pl
import pyarrow as pa
import duckdb
import h5py
import openpyxl


def random_array(n: int = 10) -> "np.ndarray":
    """numpy: return an array of n standard-normal samples."""
    return np.random.randn(n)


def make_dataframe(n: int = 100) -> "pd.DataFrame":
    """pandas: build a small demo dataframe."""
    return pd.DataFrame({
        "id": range(n),
        "value": np.random.randn(n),
        "category": np.random.choice(["a", "b", "c"], size=n),
        "timestamp": [datetime.now() - timedelta(hours=i) for i in range(n)],
    })


def zscores(values) -> "np.ndarray":
    """scipy: compute z-scores for a sequence of values."""
    return stats.zscore(np.asarray(values, dtype=float))


def ols_fit(df: "pd.DataFrame"):
    """statsmodels: fit an ordinary least squares model value ~ id."""
    X = sm.add_constant(df["id"].astype(float))
    return sm.OLS(df["value"].astype(float), X).fit()


def symbolic_derivative(expr: str = "x**2 + 3*x"):
    """sympy: symbolically differentiate an expression w.r.t. x."""
    x = sympy.symbols("x")
    return sympy.diff(sympy.sympify(expr), x)


def shortest_path_length(edges: list[tuple], source, target) -> int:
    """networkx: shortest path length between two nodes."""
    g = nx.Graph()
    g.add_edges_from(edges)
    return nx.shortest_path_length(g, source, target)


@numba.njit
def _jit_sum(arr):
    total = 0.0
    for v in arr:
        total += v
    return total


def fast_sum(values) -> float:
    """numba: JIT-compiled sum over an array."""
    return float(_jit_sum(np.asarray(values, dtype=float)))


def dask_mean(df: "pd.DataFrame", npartitions: int = 2) -> float:
    """dask: compute a column mean via a dask dataframe."""
    ddf = dd.from_pandas(df, npartitions=npartitions)
    return float(ddf["value"].mean().compute())


def polars_frame(df: "pd.DataFrame") -> "pl.DataFrame":
    """polars: convert a pandas dataframe into a polars dataframe."""
    return pl.from_pandas(df)


def to_arrow(df: "pd.DataFrame") -> "pa.Table":
    """pyarrow: convert a pandas dataframe to an Arrow table."""
    return pa.Table.from_pandas(df)


def duckdb_query(df: "pd.DataFrame", sql: str = "SELECT count(*) AS n FROM df"):
    """duckdb: run a SQL query directly over a dataframe."""
    return duckdb.query_df(df, "df", sql).to_df()


def write_h5(path: str, values) -> str:
    """h5py: write an array to an HDF5 file and return the path."""
    with h5py.File(path, "w") as f:
        f.create_dataset("values", data=np.asarray(values, dtype=float))
    return path


def write_xlsx(path: str, rows: list[dict]) -> str:
    """openpyxl: write rows to an .xlsx workbook."""
    wb = openpyxl.Workbook()
    ws = wb.active
    if rows:
        ws.append(list(rows[0].keys()))
        for row in rows:
            ws.append(list(row.values()))
    wb.save(path)
    return path
