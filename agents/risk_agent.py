from ml.predict import predict_churn


def risk_agent(customer_data):
    """
    Predicts the customer's churn risk.

    Args:
        customer_data (dict): Customer details.

    Returns:
        dict: Prediction result.
    """

    result = predict_churn(customer_data)

    return {
        "prediction": result["prediction"],
        "confidence": result["confidence"]
    }


# Test the agent
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

    response = risk_agent(sample_customer)

    print(response)