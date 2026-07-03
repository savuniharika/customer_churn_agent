from graphs.supervisor import supervisor


def main():

    print("=" * 60)
    print("      CUSTOMER CHURN AI AGENT")
    print("=" * 60)

    customer_data = {
        "age": int(input("Age: ")),
        "gender": int(input("Gender (Male=1, Female=0): ")),
        "tenure_months": int(input("Tenure Months: ")),
        "total_orders": int(input("Total Orders: ")),
        "avg_order_value": float(input("Average Order Value: ")),
        "total_spent": float(input("Total Spent: ")),
        "last_purchase_days": int(input("Days Since Last Purchase: ")),
        "app_opens_last_30d": int(input("App Opens (Last 30 Days): ")),
        "support_tickets": int(input("Support Tickets: ")),
        "satisfaction_score": int(input("Satisfaction Score (1-10): ")),
        "referrals": int(input("Referrals: ")),
        "discount_usage": int(input("Discount Usage (Yes=1, No=0): ")),
        "membership": int(input("Membership (Free=0, Gold=1, Platinum=2): "))
    }

    state = {
        "customer_data": customer_data
    }

    result = supervisor.invoke(state)

    print("\n" + "=" * 60)
    print("CUSTOMER CHURN ANALYSIS")
    print("=" * 60)

    print(f"\nPrediction : {result['prediction']}")
    print(f"Confidence : {result['confidence']}%")
    print(f"Priority   : {result['priority']}")

    print("\nExplanation")
    print("-" * 40)
    for reason in result["explanation"]:
        print(f"• {reason}")

    print("\nRecommended Strategy")
    print("-" * 40)
    for strategy in result["strategy"]:
        print(f"• {strategy}")


if __name__ == "__main__":
    main()