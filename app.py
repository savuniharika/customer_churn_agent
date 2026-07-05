import streamlit as st
from graphs.supervisor import supervisor

st.set_page_config(
    page_title="Customer Churn AI Agent",
    page_icon="📊"
)

st.title("📊 Customer Churn AI Agent")

st.header("Enter Customer Details")

customer_data = {
    "age": st.number_input("Age", min_value=18, max_value=100, value=30),
    "gender": st.selectbox("Gender", ["Female", "Male"]),
    "tenure_months": st.number_input("Tenure Months", min_value=0, value=12),
    "total_orders": st.number_input("Total Orders", min_value=0, value=10),
    "avg_order_value": st.number_input("Average Order Value", min_value=0.0, value=500.0),
    "total_spent": st.number_input("Total Spent", min_value=0.0, value=5000.0),
    "last_purchase_days": st.number_input("Days Since Last Purchase", min_value=0, value=30),
    "app_opens_last_30d": st.number_input("App Opens (Last 30 Days)", min_value=0, value=15),
    "support_tickets": st.number_input("Support Tickets", min_value=0, value=1),
    "satisfaction_score": st.slider("Satisfaction Score", 1, 10, 7),
    "referrals": st.number_input("Referrals", min_value=0, value=0),
    "discount_usage": st.selectbox("Discount Usage", ["No", "Yes"]),
    "membership": st.selectbox("Membership", ["Free", "Gold", "Platinum"])
}

# Convert selections to numbers
customer_data["gender"] = 1 if customer_data["gender"] == "Male" else 0
customer_data["discount_usage"] = 1 if customer_data["discount_usage"] == "Yes" else 0
customer_data["membership"] = {
    "Free": 0,
    "Gold": 1,
    "Platinum": 2
}[customer_data["membership"]]

if st.button("Predict Churn"):

    state = {"customer_data": customer_data}

    result = supervisor.invoke(state)

    st.success("Prediction Complete!")

    st.subheader("Prediction")
    st.write(result["prediction"])

    st.subheader("Confidence")
    st.write(f"{result['confidence']}%")

    st.subheader("Priority")
    st.write(result["priority"])

    st.subheader("Explanation")
    for item in result["explanation"]:
        st.write(f"• {item}")

    st.subheader("Recommended Strategy")
    for item in result["strategy"]:
        st.write(f"• {item}")