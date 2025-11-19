import mysql.connector

def connect_mysql_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="8333080717@Vnr",
        database="connecting_python"
    )
    return conn


def load_mysql_table(clean_customers_df, table_name):
    conn = connect_mysql_data()
    cursor = conn.cursor()

    # 1️⃣ Create table if not exists
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            customer_id INT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(150),
            phone VARCHAR(50),
            address VARCHAR(200),
            registration_date DATE,
            loyalty_status VARCHAR(50)
        );
    """)

    # 2️⃣ Insert rows
    insert_query = f"""
        INSERT INTO {table_name}
        (customer_id, name, email, phone, address, registration_date, loyalty_status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for _, row in clean_customers_df.iterrows():
        cursor.execute(insert_query, (
            row.customer_id,
            row.name,
            row.email,
            row.phone,
            row.address,
            row.registration_date,
            row.loyalty_status
        ))

    conn.commit()
    cursor.close()
    conn.close()

    print(f"Data inserted successfully into {table_name}")
