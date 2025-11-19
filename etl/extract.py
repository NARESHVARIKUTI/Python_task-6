import mysql.connector
import pandas as pd

def extract_mysql_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8333080717@Vnr",
        database="connecting_python"
    )

    query = "SELECT * FROM us_customer_data;"
    df = pd.read_sql(query, conn)  
    conn.close()
    return df

print(extract_mysql_data())



