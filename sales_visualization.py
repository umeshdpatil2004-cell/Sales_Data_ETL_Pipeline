import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# ---------------------------
# Step 1: Connect to MySQL
# ---------------------------
username = 'root'
password = quote_plus('WJ28@krhps')  # encode @
host = 'localhost'
database = 'sales_db'

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# ---------------------------
# Step 2: Extract Data
# ---------------------------
df = pd.read_sql('SELECT * FROM sales_data', con=engine)
print("✅ Data loaded from MySQL successfully!")
print(df)

# ---------------------------
# Step 3: Visualization
# ---------------------------

# 1️⃣ Bar chart – Total Sales by Product
sales_by_product = df.groupby('Product')['Total_Sales'].sum()
sales_by_product.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('💰 Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Total Sales (₹)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2️⃣ Pie chart – Sales Share by Product
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('📊 Sales Share by Product')
plt.ylabel('')  # remove y-label
plt.tight_layout()
plt.show()

print("🎉 Visualization Completed Successfully!")
