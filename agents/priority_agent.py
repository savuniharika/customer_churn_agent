def priority_agent(prediction, confidence):
    """
    Determines the priority level for customer retention.
    """

    if prediction == "No Churn":
        priority = "Low"

    else:
        if confidence >= 90:
            priority = "High"
        elif confidence >= 70:
            priority = "Medium"
        else:
            priority = "Low"

    return {
        "priority": priority
    }


# Test
if __name__ == "__main__":

    result = priority_agent("Churn", 95)

    print(result)