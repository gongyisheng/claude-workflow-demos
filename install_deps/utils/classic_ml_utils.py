"""Classic machine-learning dependencies.

One function per dependency: scikit-learn, xgboost, lightgbm, catboost,
optuna, shap.
"""

import numpy as np
import pandas as pd

import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import xgboost as xgb
import lightgbm as lgb
import catboost as cb
import optuna
import shap


def train_linear(df: "pd.DataFrame") -> "LinearRegression":
    """scikit-learn: fit a linear regression of value ~ id."""
    X = df[["id"]].values
    y = df["value"].values
    model = LinearRegression()
    model.fit(X, y)
    return model


def train_xgb(df: "pd.DataFrame"):
    """xgboost: train a small gradient-boosted regressor."""
    model = xgb.XGBRegressor(n_estimators=10, max_depth=2)
    model.fit(df[["id"]].values, df["value"].values)
    return model


def train_lgb(df: "pd.DataFrame"):
    """lightgbm: train a small gradient-boosted regressor."""
    model = lgb.LGBMRegressor(n_estimators=10, max_depth=2)
    model.fit(df[["id"]].values, df["value"].values)
    return model


def train_catboost(df: "pd.DataFrame"):
    """catboost: train a small gradient-boosted regressor."""
    model = cb.CatBoostRegressor(iterations=10, depth=2, verbose=False)
    model.fit(df[["id"]].values, df["value"].values)
    return model


def optimize_demo(n_trials: int = 5) -> float:
    """optuna: minimise (x - 2) ** 2 over a few trials."""
    def objective(trial):
        x = trial.suggest_float("x", -10, 10)
        return (x - 2) ** 2

    study = optuna.create_study(direction="minimize")
    study.optimize(objective, n_trials=n_trials)
    return study.best_value


def shap_values(df: "pd.DataFrame"):
    """shap: explain a linear model with a SHAP explainer."""
    model = train_linear(df)
    explainer = shap.Explainer(model.predict, df[["id"]].values)
    return explainer(df[["id"]].values)


def train_random_forest(df: "pd.DataFrame"):
    """scikit-learn (extra): train/test split + random forest classifier."""
    X_train, X_test, y_train, y_test = train_test_split(
        df[["id"]].values, df["category"].values, test_size=0.2, random_state=0
    )
    clf = RandomForestClassifier(n_estimators=10)
    clf.fit(X_train, y_train)
    return clf.score(X_test, y_test)
