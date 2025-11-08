import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# ---------------------------
# Step 1: Connect to MySQL
# ---------------------------
username = 'root'
password = quote_plus('WJ28@krhps')  # password encoding
host = 'localhost'
database = 'sales_db'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# ---------------------------
# Step 2: Extract Data from MySQL
# ---------------------------
df = pd.read_sql('SELECT * FROM sales_data', con=engine)
print("✅ Data loaded from MySQL:")
print(df)

# ---------------------------
# Step 3: Perform Analysis
# ---------------------------

# 1️⃣ Total Revenue
total_revenue = df['Total_Sales'].sum()

# 2️⃣ Top-Selling Product
top_product = df.groupby('Product')['Total_Sales'].sum().idxmax()
top_product_sales = df.groupby('Product')['Total_Sales'].sum().max()

# 3️⃣ Average Sales per Product
avg_sales = df.groupby('Product')['Total_Sales'].mean()

# 4️⃣ Total Quantity Sold per Product
total_quantity = df.groupby('Product')['Quantity'].sum()

# ---------------------------
# Step 4: Display Results
# ---------------------------
print("\n📈 SALES ANALYTICS REPORT 📊")
print(f"💰 Total Revenue: ₹{total_revenue}")
print(f"🏆 Top-Selling Product: {top_product} (₹{top_product_sales})")
print("\n📦 Total Quantity Sold per Product:")
print(total_quantity)
print("\n📊 Average Sales per Product:")
print(avg_sales)

print("\n🎉 Sales Data Analytics Completed Successfully!")
