import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load dataset
df = pd.read_csv("data/customer_churn_data.csv")

# Display basic information
print("=" * 50)
print("First 5 Rows")
print("=" * 50)
print(df.head())

print("\n" + "=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\n" + "=" * 50)
print("Column Names")
print("=" * 50)
print(df.columns)

print("\n" + "=" * 50)
print("Missing Values")
print("=" * 50)
print(df.isnull().sum())

# Create LabelEncoder
encoder = LabelEncoder()

# Encode categorical columns
df["gender"] = encoder.fit_transform(df["gender"])
df["discount_usage"] = encoder.fit_transform(df["discount_usage"])
df["membership"] = encoder.fit_transform(df["membership"])
df["churn"] = encoder.fit_transform(df["churn"])

print("\n" + "=" * 50)
print("Encoded Dataset")
print("=" * 50)
print(df.head())

# Features and Target
X = df.drop(columns=["customer_id", "churn"])
y = df["churn"]

print("\n" + "=" * 50)
print("Features Shape")
print("=" * 50)
print(X.shape)

print("\n" + "=" * 50)
print("Target Shape")
print("=" * 50)
print(y.shape)

# Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 50)
print("Training Set")
print("=" * 50)
print("X_train:", X_train.shape)
print("y_train:", y_train.shape)

print("\n" + "=" * 50)
print("Testing Set")
print("=" * 50)
print("X_test:", X_test.shape)
print("y_test:", y_test.shape)