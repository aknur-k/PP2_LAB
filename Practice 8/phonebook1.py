from connect import get_connection

conn = get_connection()
cur = conn.cursor()

def search(pattern):
    cur.execute("SELECT * FROM search_contacts(%s)", (pattern,))
    print("Search result:", cur.fetchall())

def paginate(limit, offset):
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    print("Paginated:", cur.fetchall())

def upsert(name, phone):
    cur.execute("CALL upsert_contact(%s, %s)", (name, phone))
    conn.commit()

def delete(value):
    cur.execute("CALL delete_contact(%s)", (value,))
    conn.commit()

def insert_many():
    cur.execute("CALL insert_many(%s, %s)",
                (['Ali','Bob','Eve'], ['123','abc','999']))
    conn.commit()


# ТЕСТЫ
upsert("Ali", "111")
upsert("Bob", "222")

search("A")

paginate(2, 0)

insert_many()

delete("Ali")

cur.close()
conn.close()