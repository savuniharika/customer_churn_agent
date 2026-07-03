def explanation_agent(customer_data):
    """
    Explains why the customer is predicted to churn or not.
    """

    reasons = []

    if customer_data["satisfaction_score"] <= 5:
        reasons.append("Low customer satisfaction.")

    if customer_data["last_purchase_days"] > 30:
        reasons.append("Customer has not purchased recently.")

    if customer_data["app_opens_last_30d"] < 10:
        reasons.append("Customer rarely uses the application.")

    if customer_data["support_tickets"] > 3:
        reasons.append("Customer has raised many support tickets.")

    if len(reasons) == 0:
        reasons.append("Customer shows healthy engagement and activity.")

    return {
        "explanation": reasons
    }


# Test
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
        "support_tickets": 4,
        "satisfaction_score": 5,
        "referrals": 1,
        "discount_usage": 1,
        "membership": 1
    }

    result = explanation_agent(sample_customer)

    print(result)