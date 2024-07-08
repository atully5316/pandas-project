import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Date': ['2023-01-15', '2023-02-20', '2023-03-10', '2023-04-25', '2023-05-30'],
    'Product': ['Widget A', 'Widget B', 'Widget C', 'Widget A', 'Widget B'],
    'Price': [9.99, 19.99, 39.99, 19.99, 29.99],
    'Quantity': [5, 3, 4, 2, 7]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Writing DataFrame to a CSV file
df.to_csv('sales_data.csv', index=False)

print("CSV file 'sales_data.csv' created successfully.")

#------------------------------------------------------------------------------------

# Step 1: Reading the data
df = pd.read_csv('sales_data.csv')

# Step 2: Cleaning and preprocessing
# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract month and year from 'Date'
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Handling missing values if any
df.dropna(inplace=True)  # Drop rows with missing values

# Step 3: Aggregations and calculations
# Total sales per month
monthly_sales = df.groupby(['Year', 'Month'])['Price'].sum().reset_index()

# Average price per product
average_price_per_product = df.groupby('Product')['Price'].mean().reset_index()

# Step 4: Visualization
# Plotting total sales per month
plt.figure(figsize=(10, 6))
plt.plot(monthly_sales.index, monthly_sales['Price'], marker='o', linestyle='-')
plt.title('Total Sales per Month')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(ticks=monthly_sales.index, labels=monthly_sales['Month'].astype(str) + '/' + monthly_sales['Year'].astype(str), rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart of average price per product
plt.figure(figsize=(10, 6))
plt.bar(average_price_per_product['Product'], average_price_per_product['Price'])
plt.title('Average Price per Product')
plt.xlabel('Product')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
