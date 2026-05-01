from connect import get_connection
import json
import csv

conn = get_connection()
cur = conn.cursor()

# ---------------- ADD CONTACT ----------------
def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday (YYYY-MM-DD): ")

    cur.execute("""
        INSERT INTO contacts(name, email, birthday)
        VALUES (%s, %s, %s)
    """, (name, email, birthday))

    conn.commit()
    print("Contact added")


# ---------------- SHOW ALL ----------------
def show_all_contacts():
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)
    print(cur.fetchall())


# ---------------- SEARCH ----------------
def search_contacts():
    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s)", (q,))
    print(cur.fetchall())


def search_by_email():
    email = input("Email: ")
    cur.execute("""
        SELECT * FROM contacts
        WHERE email ILIKE %s
    """, ('%' + email + '%',))
    print(cur.fetchall())


# ---------------- FILTER BY GROUP ----------------
def filter_by_group():
    g = input("Group: ")

    cur.execute("""
        SELECT c.*
        FROM contacts c
        JOIN groups g2 ON c.group_id = g2.id
        WHERE g2.name = %s
    """, (g,))

    print(cur.fetchall())


# ---------------- SORT ----------------
def sort_contacts():
    field = input("Sort by (name/birthday/id): ")

    if field not in ["name", "birthday", "id"]:
        print("Invalid field")
        return

    cur.execute(f"""
        SELECT * FROM contacts ORDER BY {field}
    """)
    print(cur.fetchall())


# ---------------- PAGINATION ----------------
def pagination():
    page = 0
    size = 5

    while True:
        cur.execute("""
            SELECT * FROM contacts
            ORDER BY id
            LIMIT %s OFFSET %s
        """, (size, page * size))

        print("\nPAGE:", page)
        print(cur.fetchall())

        cmd = input("next / prev / quit: ")

        if cmd == "next":
            page += 1
        elif cmd == "prev" and page > 0:
            page -= 1
        else:
            break


# ---------------- ADD PHONE ----------------
def add_phone_to_contact():
    name = input("Contact name: ")
    phone = input("Phone: ")
    type = input("Type (home/work/mobile): ")

    cur.execute("CALL add_phone(%s, %s, %s)", (name, phone, type))
    conn.commit()


# ---------------- MOVE TO GROUP ----------------
def move_contact_to_group():
    name = input("Contact name: ")
    group = input("Group name: ")

    cur.execute("CALL move_to_group(%s, %s)", (name, group))
    conn.commit()


# ---------------- CSV IMPORT (FIXED) ----------------
def import_csv():
    with open("contacts.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            email = row["email"]
            birthday = row["birthday"]
            group_name = row["group"]
            phone = row["phone"]
            phone_type = row["type"]

            # group
            cur.execute("SELECT id FROM groups WHERE name=%s", (group_name,))
            g = cur.fetchone()

            if g:
                group_id = g[0]
            else:
                cur.execute("INSERT INTO groups(name) VALUES (%s) RETURNING id", (group_name,))
                group_id = cur.fetchone()[0]

            # contact
            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id
            """, (name, email, birthday, group_id))

            contact_id = cur.fetchone()[0]

            # phone
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s)
            """, (contact_id, phone, phone_type))

    conn.commit()
    print("CSV imported")


# ---------------- JSON EXPORT ----------------
def export_json():
    cur.execute("""
        SELECT c.id, c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    print("Exported")


# ---------------- JSON IMPORT ----------------
def import_json():
    with open("contacts.json", "r") as f:
        data = json.load(f)

    for c in data:
        cur.execute("SELECT id FROM contacts WHERE name=%s", (c[1],))
        exists = cur.fetchone()

        if exists:
            choice = input(f"{c[1]} exists (skip/overwrite): ")

            if choice == "skip":
                continue

            if choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name=%s", (c[1],))

        cur.execute("""
            INSERT INTO contacts(name, email, birthday)
            VALUES (%s, %s, %s)
        """, (c[1], c[2], c[3]))

    conn.commit()
    print("JSON imported")


# ---------------- MENU ----------------
def menu():
    while True:
        print("""
================ PHONEBOOK =================

1. Add contact
2. Show all contacts
3. Search contacts
4. Filter by group
5. Search by email
6. Sort contacts
7. Pagination
8. Add phone to contact
9. Move contact to group
10. Import CSV
11. Export JSON
12. Import JSON
0. Exit

===========================================
        """)

        choice = input("Choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            show_all_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            filter_by_group()
        elif choice == "5":
            search_by_email()
        elif choice == "6":
            sort_contacts()
        elif choice == "7":
            pagination()
        elif choice == "8":
            add_phone_to_contact()
        elif choice == "9":
            move_contact_to_group()
        elif choice == "10":
            import_csv()
        elif choice == "11":
            export_json()
        elif choice == "12":
            import_json()
        elif choice == "0":
            print("Bye!")
            break


menu()