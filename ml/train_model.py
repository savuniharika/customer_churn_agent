from preprocess import X, X_train, X_test, y_train, y_test

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd
# Initialize Models
lr = LogisticRegression(max_iter=1000)
dt = DecisionTreeClassifier(random_state=42)
rf = RandomForestClassifier(random_state=42)

# Train Models
lr.fit(X_train, y_train)
dt.fit(X_train, y_train)
rf.fit(X_train, y_train)

print("All models trained successfully!")

# Store Models
models = {
    "Logistic Regression": lr,
    "Decision Tree": dt,
    "Random Forest": rf
}

# Dictionary to store accuracy
accuracy = {}

# Evaluate Models
for name, model in models.items():
    y_pred = model.predict(X_test)

    accuracy[name] = accuracy_score(y_test, y_pred)

    print("\n" + "=" * 50)
    print(name)
    print("=" * 50)
    print(f"Accuracy: {accuracy[name]:.4f}")

    print("\nClassification Report")
    print(classification_report(y_test, y_pred))

    print("Confusion Matrix")
    print(confusion_matrix(y_test, y_pred))

# Compare Models
print("\n" + "=" * 50)
print("Model Comparison")
print("=" * 50)

for model_name, acc in accuracy.items():
    print(f"{model_name}: {acc:.4f}")

# Feature Importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(by="Importance", ascending=False)

print("\n" + "=" * 50)
print("Feature Importance")
print("=" * 50)
print(importance)
import joblib

# Save the trained Random Forest model
joblib.dump(rf, "ml/churn_model.pkl")

print("\nModel saved successfully as churn_model.pkl")