import unittest
from sklearn.datasets import load_iris
from submissions.developer_your_id import preprocess_data, train_model

class TestIrisClassification(unittest.TestCase):
    def test_data_loading(self):
        data = load_iris()
        self.assertEqual(data.data.shape, (150, 4))  # Checks if the data shape is correct

    def test_preprocessing(self):
        data = load_iris()
        X_train, X_test, y_train, y_test = preprocess_data(data.data, data.target)
        self.assertEqual(X_train.shape[0], 120)  # Assuming 80% training data

    def test_model_accuracy(self):
        data = load_iris()
        X_train, X_test, y_train, y_test = preprocess_data(data.data, data.target)
        model, accuracy = train_model(X_train, y_train, X_test, y_test)
        self.assertGreater(accuracy, 0.90)  # Check if accuracy is above 90%

if __name__ == '__main__':
    unittest.main()
