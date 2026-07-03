def strategy_agent(prediction, priority):
    """
    Suggest retention strategies based on prediction and priority.
    """

    if prediction == "No Churn":
        strategies = [
            "Continue regular engagement.",
            "Send personalized offers occasionally.",
            "Reward customer loyalty."
        ]

    elif priority == "High":
        strategies = [
            "Contact the customer immediately.",
            "Offer a special discount or cashback.",
            "Assign a dedicated customer support representative.",
            "Provide exclusive membership benefits."
        ]

    elif priority == "Medium":
        strategies = [
            "Send personalized promotional emails.",
            "Offer limited-time discounts.",
            "Recommend products based on purchase history."
        ]

    else:
        strategies = [
            "Monitor customer activity.",
            "Send occasional reminders and offers."
        ]

    return {
        "strategy": strategies
    }


# Test
if __name__ == "__main__":

    result = strategy_agent("Churn", "High")

    print(result)