import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("Mall_Customers.csv")

# Display first 5 rows
print("First 5 rows:")
print(data.head())

# Dataset information
print("\nDataset Information:")
print(data.info())

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Customer gender count
print("\nGender Distribution:")
print(data["Gender"].value_counts())

# Average spending score by gender
print("\nAverage Spending Score by Gender:")
print(data.groupby("Gender")["Spending Score (1-100)"].mean())

# Plot spending score distribution
plt.hist(data["Spending Score (1-100)"], bins=10)
plt.title("Customer Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")
plt.show()
