

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("sales.csv")

print(" First 5 rows:")
print(df.head())

print("\n Dataset Info:")
print(df.info())

print("\nSummary Stats:")
print(df.describe())

print("\n Missing Values:")
print(df.isnull().sum())

df = df.fillna(0)

print("\n Missing values handled.")
df['Total'] = df['Quantity'] * df['Price']

print("\n Total Sales Column Added:")
print(df.head())

product_sales = df.groupby('Product')['Total'].sum()
print("\n Total Revenue by Product:")
print(product_sales)

plt.figure(figsize=(8,5))
product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

df['Date'] = pd.to_datetime(df['Date'])
monthly_sales = df.groupby(df['Date'].dt.to_period('M'))['Total'].sum()

plt.figure(figsize=(8,5))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

top_product = product_sales.idxmax()
top_value = product_sales.max()

print(f"\n Top Selling Product: {top_product} (Revenue: {top_value})")

df.to_csv("cleaned_sales.csv", index=False)
print("\nCleaned file saved as cleaned_sales.csv")