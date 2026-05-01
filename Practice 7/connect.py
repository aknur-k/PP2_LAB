import psycopg2

def connect():
    return psycopg2.connect(
        dbname="phonebook_db",
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432"
    )


if __name__ == "_main_":
    try:
        conn = connect()
        print("Connected successfully!")
        conn.close()
    except Exception as e:
        print("Error:", e)