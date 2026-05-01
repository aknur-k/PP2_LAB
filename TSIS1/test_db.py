import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="phonebook",
    user="postgres",
    password="1234"
)

print("Connected!")
conn.close()
