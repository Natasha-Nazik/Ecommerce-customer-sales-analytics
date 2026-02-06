import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

#  .1 loading the datasets 
#  === loading basket and customer details for analysis

df_basket = pd.read_csv('basket_details.csv')
print("---- Dataset Successfully Loaded ----")

#  2. Data Cleaning
#  === Converting 'Basket_date' to datetime format for time-series  analysis ===

df_basket['basket_date'] =pd.to_datetime(df_basket['basket_date'])

# 3. Feature Engineering 
#  === Extracting Month & Year to analyze Monthly sales trends ===
df_basket['month_year'] = df_basket['basket_date'].dt.to_period('M')

# 4. Exploratory data analysis (EDA) 
#  === Calculating total items sold per day ===
daily_sales = df_basket.groupby('basket_date')['basket_count'].sum().reset_index()
print("\n--- Summary Statistics ---")
print(df_basket.describe())

# 5. Data Visualization
# === creating a visual trend of sales over time ===
plt.figure(figsize=(12,6))
sns.lineplot(data=daily_sales,x='basket_date',y='basket_count',
color='blue')
plt.title('Daily Sales Trend(E-commerceProject)',fontsize=15)
plt.xlabel('Date',fontsize=12)
plt.ylabel('Total Items Sold',fontsize=12)
plt.grid(True)
plt.show()
 
# 6. Top product Analysis
#  === Identifying the Top 10 most selling products ===
top_products = df_basket.groupby('product_id')['basket_count'].sum().sort_values(ascending=False).head(10)
print("\n--- Top 10 Best Selling Products ---")
print(top_products)

#  visualizing Top Product
plt.figure(figsize=(10,5))
top_products.plot(kind='bar',color='orange')
plt.title('Top Selling Product',fontsize=15)
plt.xlabel('Product ID')
plt.ylabel('Total Quantity Sold')
plt.show()

# 7. Checking For Missing Values 
# === Final data quality check ===
print("\n --- Missing Values Ckeck---")
print(df_basket.isnull().sum())

# 8. Merging Datasets
#  === Joining basket details with customer details to get demographic insights ===

# loading the 2nd dataset ........
df_customers = pd.read_csv('customer_details.csv')
# merging both file on customer_id column exists in both files 
df_final=pd.merge(df_basket,df_customers,on='customer_id',how='inner')

print('\n----Merged Data Preview First 5 Rows----')
print(df_final.head())

# 9. Gender-wise Sales Analysis 
#  Analyzing which gender is shopping more
gender_sales = df_final.groupby('sex')['basket_count'].sum()

print("\n--- Sales by Gender ---")
print(gender_sales)

plt.figure(figsize=(8, 5))
gender_sales.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightpink'], startangle=140)
plt.title('Sales Distribution by Gender', fontsize=15)
plt.ylabel('') 
plt.show()

# 10. Age Group Analysis (Extra Insight)
#  Visualizing the age distribution of customers
plt.figure(figsize=(10, 6))
sns.histplot(df_final['customer_age'], bins=20, kde=True, color='green')
plt.title('Customer Age Distribution', fontsize=15)
plt.xlabel('Age')
plt.ylabel('Number of Orders')
plt.show()
# ==========================================
# 11. Final Data Export & Status Report
# ==========================================

# Exporting the merged and cleaned dataset for further business use
df_final.to_csv('final_ecommerce_analysis_report.csv', index=False)

print("\n" + "="*50)
print("DATA ANALYSIS PIPELINE COMPLETED SUCCESSFULLY")
print("="*50)
print("Status: All processing steps executed.")
print("Output: 'final_ecommerce_analysis_report.csv' generated.")
print("Action: Processed data is ready for BI tools/Reporting.")
print("="*50)
