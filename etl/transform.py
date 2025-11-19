import pandas as pd
import re

def transform_customer_data(us_customer_data):

    # Remove duplicates
    us_customer_data = us_customer_data.drop_duplicates(subset="customer_id", keep="first")

    # Normalize name
    us_customer_data["name"] = (
        us_customer_data["name"]
        .astype(str)
        .str.strip()
        .str.title()
        .str.replace(r'^(mr|mrs|miss|smt|dr|prof|ms|shri)\.? ', '', case=False, regex=True)
    )

    # Fix email
    us_customer_data["email"] = us_customer_data.apply(
        lambda row: (
            f"{re.sub(r'\\s+', '', row['name'].lower())}@gmail.com"
            if pd.isna(row["email"]) or row["email"] == ""
            else row["email"].lower()
        ),
        axis=1
    )

    # Clean phone: remove characters
    us_customer_data["phone"] = (
        us_customer_data["phone"]
        .astype(str)
        .str.replace(r"[A-Za-z]", "", regex=True)
        .str.replace(r"\D", "", regex=True)
    )

    # If empty → assign default
    us_customer_data["phone"] = us_customer_data["phone"].apply(
        lambda row: "0000000000" if row.strip() == "" or row == "nan" else row
    )

    # Format phone correctly
    us_customer_data["phone"] = us_customer_data["phone"].apply(
        lambda row: f"({row[:3]})-{row[3:6]}-{row[6:10]}" if len(row) >= 10 else row
    )

    #sortig customer_id
    us_customer_data = us_customer_data.sort_values(by="customer_id")


     # Convert to datetime
    us_customer_data["registration_date"] = pd.to_datetime(
        us_customer_data["registration_date"], errors="coerce"
    )

    return us_customer_data

