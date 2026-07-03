import joblib
import pandas as pd

# Load the trained model
model = joblib.load("ml/churn_model.pkl")


def predict_churn(customer_data):
    """
    Predict customer churn.

    Args:
        customer_data (dict): Customer information.

    Returns:
        dict: Prediction and confidence.
    """

    # Convert input to DataFrame
    input_df = pd.DataFrame([customer_data])

    # Predict
    prediction = model.predict(input_df)[0]

    # Predict probability
    probability = model.predict_proba(input_df)[0]

    confidence = max(probability) * 100

    result = {
        "prediction": "Churn" if prediction == 1 else "No Churn",
        "confidence": float(round(confidence, 2))
    }

    return result
if __name__ == "__main__":

    sample_customer = {
        "age": 45,
        "gender": 1,
        "tenure_months": 24,
        "total_orders": 30,
        "avg_order_value": 550,
        "total_spent": 16500,
        "last_purchase_days": 40,
        "app_opens_last_30d": 8,
        "support_tickets": 3,
        "satisfaction_score": 5,
        "referrals": 1,
        "discount_usage": 1,
        "membership": 1
    }

    result = predict_churn(sample_customer)

    print(result)