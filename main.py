import pandas as pd

from etl.extract import extract_mysql_data
from etl.transform import transform_customer_data
from etl.load import load_mysql_table

# STEP 1: Extract
customers_df = extract_mysql_data()

# STEP 2: Transform
clean_customers_df = transform_customer_data(customers_df)

# STEP 3: Load
load_mysql_table(clean_customers_df, "customer_clean_data")

print(clean_customers_df)
