import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("telco_churn.csv")

print(df.head())

print(df.isnull().sum())

df = df.dropna()

df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

df = df.dropna()

df['ChurnValue'] = df['Churn'].map({
    'Yes': 1,
    'No': 0
})

total_customers = df['customerID'].count()

churned_customers = df['ChurnValue'].sum()

retained_customers = total_customers - churned_customers

churn_rate = (churned_customers / total_customers) * 100

retention_rate = (retained_customers / total_customers) * 100

print("===== KPI RESULTS =====")

print(f"Total Customers: {total_customers}")

print(f"Churned Customers: {churned_customers}")

print(f"Retention Rate: {retention_rate:.2f}%")

print(f"Churn Rate: {churn_rate:.2f}%")

contract_churn = df.groupby('Contract')['ChurnValue'].mean() * 100

print(contract_churn)

payment_churn = df.groupby('PaymentMethod')['ChurnValue'].mean() * 100

print(payment_churn)

average_tenure = df.groupby('Churn')['tenure'].mean()

print(average_tenure)

monthly_charge_analysis = df.groupby('Churn')['MonthlyCharges'].mean()

print(monthly_charge_analysis)

contract_churn.plot(
    kind='bar',
    figsize=(8,5)
)

plt.title("Churn Rate by Contract Type")

plt.xlabel("Contract Type")

plt.ylabel("Churn Rate (%)")

plt.show()

payment_churn.plot(
    kind='bar',
    figsize=(10,5)
)

plt.title("Churn Rate by Payment Method")

plt.xlabel("Payment Method")

plt.ylabel("Churn Rate (%)")

plt.show()

df.to_csv(
    "cleaned_churn_data.csv",
    index=False
)

print("Cleaned dataset exported successfully!")