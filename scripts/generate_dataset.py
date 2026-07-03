import os
import pandas as pd
import numpy as np

# configuration
np.random.seed(42)
NUM_CUSTOMERS = 5000

# customer profile
customer_ids = [
    f"CUST{str(i).zfill(4)}"
    for i in range(1, NUM_CUSTOMERS + 1)
]
genders = np.random.choice (
    ["Male", "Female"],
    size=NUM_CUSTOMERS,
    p=[0.48,0.52]
)
ages = np.random.randint(18, 71, NUM_CUSTOMERS)

# customer history
tenure_months = np.random.randint(1,61, NUM_CUSTOMERS)
total_orders = []

for tenure in tenure_months:
    max_orders = max(1, tenure * 2)
    orders = np.random.randint(1, max_orders + 1)
    total_orders.append(orders)

total_orders = np.array(total_orders)

# spending
avg_order_value = np.random.randint(500, 5001, NUM_CUSTOMERS)
total_spent = total_orders * avg_order_value

# Days since last purchase (0–180)
last_purchase_days = np.random.randint(0, 181, NUM_CUSTOMERS)

# App opens in the last 30 days
app_opens_last_30d = np.maximum(
    0,
    30 - (last_purchase_days // 6) + np.random.randint(-3, 4, NUM_CUSTOMERS)
)

# Number of support tickets
support_tickets = np.random.randint(0, 6, NUM_CUSTOMERS)

# Satisfaction score (1.0–5.0)
satisfaction_score = np.round(
    np.random.uniform(1.0, 5.0, NUM_CUSTOMERS),
    1
)

# Number of referrals
referrals = np.random.randint(0, 6, NUM_CUSTOMERS)

# Discount usage
discount_usage = np.random.choice(
    ["Yes", "No"],
    size=NUM_CUSTOMERS,
    p=[0.6, 0.4]
)

# Membership type
membership = np.random.choice(
    ["Free", "Silver", "Gold", "Platinum"],
    size=NUM_CUSTOMERS,
    p=[0.40, 0.30, 0.20, 0.10]
)
# churn logic
churn = []

for i in range(NUM_CUSTOMERS):

    risk_score = 0

    if last_purchase_days[i] > 60:
        risk_score += 2

    if app_opens_last_30d[i] < 5:
        risk_score += 2

    if satisfaction_score[i] < 3:
        risk_score += 2

    if support_tickets[i] >= 3:
        risk_score += 1

    if tenure_months[i] < 6:
        risk_score += 1

    if total_orders[i] < 5:
        risk_score += 1

    if risk_score >= 5:
        churn.append("Yes")
    else:
        churn.append("No")

 # create dataframe
df = pd.DataFrame({
    "customer_id": customer_ids,
    "age": ages,
    "gender": genders,
    "tenure_months": tenure_months,
    "total_orders": total_orders,
    "avg_order_value": avg_order_value,
    "total_spent": total_spent,
    "last_purchase_days": last_purchase_days,
    "app_opens_last_30d": app_opens_last_30d,
    "support_tickets": support_tickets,
    "satisfaction_score": satisfaction_score,
    "referrals": referrals,
    "discount_usage": discount_usage,
    "membership": membership,
    "churn": churn
   
})
# save dataset
os.makedirs("data",exist_ok=True)
df.to_csv(
    "data/customer_churn_data.csv",
     index=False
)
# Output
print("=" * 50)
print("Dataset created successfully!")
print("=" * 50)

print("\nFirst 5 Rows:\n")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nChurn Distribution:")
print(df["churn"].value_counts())

print("\nDataset saved to:")
print("data/customer_churn_data.csv")