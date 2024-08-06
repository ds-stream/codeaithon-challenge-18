def validate_model(user_model):
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    predictions = user_model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    if accuracy > 0.90:
        print("Model passed with high accuracy")
    else:
        print("Model accuracy is too low")

validate_model(user_model)
