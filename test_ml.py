import pytest
# TODO: add necessary import
import pandas as pd
import numpy as np
from ml.data import process_data
from ml.model import train_model, compute_model_metrics, inference
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


# TODO: implement the first test. Change the function name and input as needed
def test_train_model_type():
    """
    Test to ensure that train_model returns a RFC instance
    """
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y_train = np.array([0, 1, 0])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier)


# TODO: implement the second test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Test that compute_model_metrics returns the correct precision, recall, and fbeta scores
    """
    y_true = np.array([0, 1, 1, 0, 1, 0, 1, 1])
    y_preds = np.array([0, 1, 0, 0, 1, 1, 1, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    # The expected values are pre-calculated for these inputs
    expected_precision = 0.75
    expected_recall = 0.6
    expected_fbeta = 0.6666666666666666
    assert precision == pytest.approx(expected_precision)
    assert recall == pytest.approx(expected_recall)
    assert fbeta == pytest.approx(expected_fbeta)


# TODO: implement the third test. Change the function name and input as needed
def test_inference_output_shape():
    """
    Test that inference returns predictions of the correct shape
    """
    model = RandomForestClassifier(random_state=42)
    X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y_train = np.array([0, 1, 0])
    model.fit(X_train, y_train)
    X_test = np.array([[10, 11, 12], [13, 14, 15]])
    preds = inference(model, X_test)
    assert preds.shape[0] == X_test.shape[0]