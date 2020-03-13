# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 07:54:43 2020

@author: nsde
"""

__version__ = "0.1"
__author__ = "Nicki Skafte Detlefsen"
__author_email__ = "nsde@dtu.dk"
__docs__ = (
    "Pytorch-metrics is a simple add on library to pytorch that adds "
    "many commonly used metrics within deep learning"
)

from .base import Metric, RegressionMetric, ClassificationMetric

from .wrappers import MetricCollection, RunningAverage, Mean, Sum, Product

from .regression import (
    MeanSquaredError,
    MeanAbsoluteError,
    RootMeanSquaredError,
    ExplainedVariance,
    R2Score,
    MaxError,
    MeanSquaredLogarithmicError,
    MeanTweedieDeviance,
    MeanPoissonDeviance,
    MeanGammaDeviance,
    CosineSimilarity,
)

from .classification import (
    Accuracy,
    FilteredAccuracy,
    Precision,
    Recall,
    BalancedAccuracy,
    F1,
    TopKAccuracy,
    ROC,
    AUC,
    ConfusionMatrix,
)

__all__ = [
    "Metric",
    "MetricDict",
    "RunningAverage" "MeanSquaredError",
    "MeanAbsoluteError",
    "RootMeanSquaredError",
    "ExplainedVariance",
    "R2Score",
    "MaxError",
    "MeanSquaredLogarithmicError" "MeanTweedieDeviance",
    "MeanPoissonDeviance",
    "MeanGammaDeviance",
    "Accuracy",
    "FilteredAccuracy",
    "Precision",
    "Recall",
    "BalancedAccuracy",
    "F1",
    "TopKAccuracy",
    "ROC",
    "AUC",
    "ConfusionMatrix"
]
