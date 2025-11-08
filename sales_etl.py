import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus  # हे नवीन import खूप महत्त्वाचं आहे

# ---------------------------
# Step 1: Extract (Read Excel)
# ---------------------------
df = pd.read_excel('sales_data.xlsx')

# ---------------------------
# Step 2: Transform
# ---------------------------
df['Date'] = pd.to_datetime(df['Date'])  # Date format change
df['Total_Sales'] = df['Quantity'] * df['Unit_Price']

# ---------------------------
# Step 3: Load (to MySQL)
# ---------------------------

# MySQL connection details
username = 'root'
password = quote_plus('WJ28@krhps')  # @ handle करण्यासाठी quote_plus वापरलं आहे
host = 'localhost'
database = 'sales_db'

# Connection तयार करणे
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}/{database}")

# Data लोड करणे
df.to_sql('sales_data', con=engine, if_exists='replace', index=False)

print("🎉 Sales Data ETL Pipeline (MySQL Version) Completed Successfully!")

# ---------------------------
# Step 4: Verify (Read back)
# ---------------------------
result = pd.read_sql('SELECT * FROM sales_data', con=engine)
print(result)
