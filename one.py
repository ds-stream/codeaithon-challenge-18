from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

# Load data
iris = load_iris()
X = iris.data
y = iris.target

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Initialize and train models
knn = KNeighborsClassifier(n_neighbors=3)
logreg = LogisticRegression(max_iter=200)
knn.fit(X_train_scaled, y_train)
logreg.fit(X_train_scaled, y_train)

# Predict and evaluate
y_pred_knn = knn.predict(X_test_scaled)
y_pred_logreg = logreg.predict(X_test_scaled)
knn_accuracy = accuracy_score(y_test, y_pred_knn)
logreg_accuracy = accuracy_score(y_test, y_pred_logreg)

# Print accuracy report
print("Model Accuracy Report")
print("----------------------")
print(f"K-Nearest Neighbors accuracy: {knn_accuracy:.2f}")
print(f"Logistic Regression accuracy: {logreg_accuracy:.2f}")

# Confusion matrix data
cm = confusion_matrix(y_test, y_pred_knn)  # Using KNN predictions here
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)

# Plot confusion matrix
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix for K-Nearest Neighbors')
plt.show()
