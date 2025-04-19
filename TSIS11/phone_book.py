import psycopg2
import csv
from config import host, database, password, user

conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

def create_table():
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phone_book(
               id serial PRIMARY KEY,
               first_name varchar(100) NOT NULL,
               last_name varchar(100),
               phone_number varchar(20) NOT NULL UNIQUE,
               job varchar(100));"""
        )
    conn.commit()

# 1 Function that returns all records based on a pattern
def search_by_pattern(pattern):
    with conn.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM phone_book 
            WHERE first_name ILIKE %s OR 
                  last_name ILIKE %s OR 
                  phone_number LIKE %s""",
            (f'%{pattern}%', f'%{pattern}%', f'%{pattern}%')
        )
        results = cursor.fetchall()
        if results:
            print("\nSearch results:")
            for row in results:
                print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}, Job: {row[4]}")
        else:
            print("No contacts found.")

# 2 Procedure to insert or update contact
def upsert_contact():
    print("\n Add/Update Contact =)")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    
    if not name or not phone:
        print("Error: Name and phone are required!")
        return
    
    with conn.cursor() as cursor:
        cursor.execute(
            """INSERT INTO phone_book (first_name, phone_number) 
            VALUES (%s, %s)
            ON CONFLICT (phone_number) 
            DO UPDATE SET first_name = EXCLUDED.first_name""",
            (name, phone)
        )
    conn.commit()
    print("Contact saved successfully!")

# 3 Procedure to insert many users with validation
def bulk_insert_contacts():
    print("\n=== Bulk Add Contacts ===")
    print("Enter contacts in format: name,phone (one per line)")
    print("Type 'done' when finished")
    
    contacts = []
    while True:
        entry = input("> ").strip()
        if entry.lower() == 'done':
            break
        if ',' not in entry:
            print("Invalid format! Use 'name,phone'")
            continue
        name, phone = entry.split(',', 1)
        contacts.append((name.strip(), phone.strip()))
    
    if not contacts:
        print("No contacts to add.")
        return
    
    errors = []
    with conn.cursor() as cursor:
        for name, phone in contacts:
            if not phone.isdigit():
                errors.append(f"Invalid phone: {name} - {phone}")
                continue
            try:
                cursor.execute(
                    """INSERT INTO phone_book (first_name, phone_number)
                    VALUES (%s, %s)""",
                    (name, phone)
                )
            except psycopg2.Error as e:
                errors.append(f"Failed to add {name}: {e}")
                conn.rollback()
    
    conn.commit()
    print(f"\nSuccessfully added {len(contacts)-len(errors)} contacts")
    if errors:
        print("\nErrors:")
        for error in errors:
            print(error)

# 4 Function to query data with pagination
def paginated_view():
    print("\nPaginated View =)")
    limit = input("Enter number of contacts per page (default 5): ").strip()
    limit = int(limit) if limit.isdigit() else 5
    page = 0
    
    while True:
        offset = page * limit
        with conn.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM phone_book 
                ORDER BY first_name
                LIMIT %s OFFSET %s""",
                (limit, offset)
            )
            results = cursor.fetchall()
        
        print(f"\nPage {page+1}:")
        if not results:
            print("No more contacts.")
            break
        
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Phone: {row[3]}")
        
        action = input("\n[N]ext page, [P]revious page, [Q]uit: ").lower()
        if action == 'n':
            page += 1
        elif action == 'p' and page > 0:
            page -= 1
        elif action == 'q':
            break

# 5 Procedure to delete by username or phone
def delete_contact():
    print("\ Delete Contact =)")
    print("Delete by:")
    print("1. Name")
    print("2. Phone number")
    print("3. Both")
    choice = input("Your choice: ").strip()
    
    if choice == '1':
        name = input("Enter name to delete: ").strip()
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM phone_book WHERE first_name = %s",
                (name,)
            )
    elif choice == '2':
        phone = input("Enter phone number to delete: ").strip()
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM phone_book WHERE phone_number = %s",
                (phone,)
            )
    elif choice == '3':
        name = input("Enter name: ").strip()
        phone = input("Enter phone number: ").strip()
        with conn.cursor() as cursor:
            cursor.execute(
                "DELETE FROM phone_book WHERE first_name = %s AND phone_number = %s",
                (name, phone)
            )
    else:
        print("Invalid choice!")
        return
    
    conn.commit()
    print("Contact(s) deleted successfully!")

# main menu
def main_menu():
    create_table()
    while True:
        print("\n~~ MENU ~~")
        print("1. Search contacts")
        print("2. Add/Update contact")
        print("3. Bulk add contacts") 
        print("4. View contacts (paginated)")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("Select option: ").strip()
        
        if choice == '1':
            pattern = input("Enter the search template for the person you need: ").strip()
            search_by_pattern(pattern)
        elif choice == '2':
            upsert_contact()
        elif choice == '3':
            bulk_insert_contacts()
        elif choice == '4':
            paginated_view()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye ~~ :)")
            break
        else:
            print("Wrong option! Please choose the option :(")

if __name__ == "__main__":
    try:
        main_menu()
    finally:
        conn.close()