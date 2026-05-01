from connect import connect
import csv

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table created successfully")


# ---------------- ADD / UPDATE ----------------
def add_update_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO contacts (name, phone)
    VALUES (%s, %s)
""", (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Contact added/updated")


# ---------------- SHOW ALL ----------------
def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ---------------- SEARCH ----------------
def search():
    name = input("Enter name to search: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts WHERE name ILIKE %s", (f"%{name}%",))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


# ---------------- DELETE ----------------
def delete():
    name = input("Enter name to delete: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM contacts WHERE name = %s", (name,))

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted successfully")


# ---------------- CSV IMPORT ----------------
def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
            name, phone = row
            cur.execute("""
                INSERT INTO contacts (name, phone)
                VALUES (%s, %s)
            """, (name, phone))

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported")


# ---------------- PAGINATION ----------------
def show_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM contacts LIMIT %s OFFSET %s", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Add/Update contact")
        print("3. Import from CSV")
        print("4. Show all contacts")
        print("5. Search")
        print("6. Show paginated")
        print("7. Delete contact")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            add_update_contact()
        elif choice == "3":
            insert_from_csv(r"c:\Users\Aknur\Documents\PP2_LAB\Practice 8\contacts.csv")
        elif choice == "4":
            show_all()
        elif choice == "5":
            search()
        elif choice == "6":
            show_paginated()
        elif choice == "7":
            delete()
        elif choice == "8":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    menu()
