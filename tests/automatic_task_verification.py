import os
import importlib.util
import pytest
from sklearn.datasets import load_iris


def test_submission_files_exist(developer):
    base_path = f"submissions/developer-{developer}"
    folders = ["tests", "results"]

    for folder in folders:
        assert os.path.exists(
            os.path.join(base_path, folder)
        ), f"{folder.capitalize()} directory does not exist"

        files = os.listdir(os.path.join(base_path, folder))
        assert len(files) > 0, f"No {folder} files found"


def test_data_loading(solution):
    data = load_iris()
    assert data.data.shape == (150, 4)  # Checks if the data shape is correct


def test_preprocessing(solution):
    data = load_iris()
    X_train, X_test, y_train, y_test = solution.preprocess_data(data.data, data.target)
    assert X_train.shape[0] == 120  # Assuming 80% training data


def test_model_accuracy(solution):
    data = load_iris()
    X_train, X_test, y_train, y_test = solution.preprocess_data(data.data, data.target)
    model, accuracy = solution.train_model(X_train, y_train, X_test, y_test)
    assert accuracy > 0.90  # Check if accuracy is above 90%
