import psycopg2
import csv
from config import host, database, password, user

conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

# create a new table phone book if it doesn't exist 
def create_table():
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS phone_book(
               id serial PRIMARY KEY,
               first_name varchar(100) NOT NULL,
               last_name varchar(100),
               phone_number varchar(20) NOT NULL,
               job varchar(100));"""
        )
    conn.commit()


# insert data from console 
def insert_from_console():
    try: 
        first_name = input("Enter first name:").strip()
        if not first_name:
            raise ValueError("First name cannot be empty")
        
        last_name = input("Enter second name:").strip()  # or None
        phone_number = input("Enter phone number:").strip()
        if not phone_number:
            raise ValueError("Phone number cannot be empty")
        
        job = input("Enter job name:").strip() # or None 

        with conn.cursor() as cursor:
            cursor.execute(

                """INSERT INTO phone_book (first_name, last_name, phone_number, job) VALUES (%s, %s, %s, %s)""",
                (first_name, last_name, phone_number, job)
            )
        conn.commit()
        print("Data inserting successfully :)")
    
    except Exception as ex:
        if type(ex).__name__ == "UniqueViolation":
            print("Error: duplicate data")
        elif type(ex).__name__ == "ConnectionError":
            print("Error connecting to the database")


# insert data from csv file
def insert_from_csv():
    try:
        with conn.cursor() as cursor, open(r'C:\Users\Huawei\Desktop\PP2_TSIS\TSIS10\ph_book_data.csv', 'r') as file:
            reader = csv.DictReader(file) # read csv file like a dictionary
            for row in reader:
                try:
                    cursor.execute(

                        """INSERT INTO phone_book (first_name, last_name, phone_number, job) VALUES (%s, %s, %s, %s)""",
                        (row["first_name"], row["last_name"], row["phone_number"], row["job"])
                        )
                    
                except psycopg2.Error as e:
                    print(f"Skipping row due to error: {e}")
                    conn.rollback()
                    continue

        conn.commit()
        print("Data inserting successfully :)")

    except FileNotFoundError:
        print("Error: CSV file not found")
    except Exception as ex:
        conn.rollback()
        print(f"Unexpected error: {ex}")

# Updating contact information by phone number
def update_contact():
    try: 
        phone_number = input("Enter phone number:").strip()
        if not phone_number:
            print("Error: Phone number cannot be empty")
            return
        
        first_name = input("Enter first name:").strip()
        if not first_name:
            print("Error: First name cannot be empty")
            return
        
        with conn.cursor() as cursor:
            cursor.execute(

                """UPDATE phone_book SET first_name = %s WHERE phone_number = %s""",
                (first_name, phone_number)
            )

        # checking data 
        if cursor.rowcount == 0:
            print(f"Warning: No records were updated. Phone number {phone_number} not found.")
        else:
            conn.commit()
            print(f"Updated {cursor.rowcount} record(s) successfully :)")

    except psycopg2.IntegrityError as ex:
        print(f"Database error: {ex}")
    except psycopg2.OperationalError:
        print("Error connecting to the database")
    except Exception as ex:
        print(f"Unexpected error: {ex}")


def data_querying():
    try:
        filter = input("Choose one of the filtering methods: fname | lname | phone_num | job").lower().strip()
        if filter not in ['fname', 'lname', 'phone_num', 'job']:
            print("Invalid filter option")
            return
        
        with conn.cursor() as cursor:
            if filter == "fname":
                first_name = input("Enter first name: ").strip()
                cursor.execute(

                    """SELECT * FROM phone_book WHERE first_name = %s""",
                    (first_name,)
                )
            elif filter == "lname":
                last_name = input("Enter second name: ").strip()
                cursor.execute(

                    """SELECT * FROM phone_book WHERE last_name = %s""",
                    (last_name,)
                )
            elif filter == "phone_num":
                phone_number = input("Enter phone number: ").strip()
                cursor.execute(

                    """SELECT * FROM phone_book WHERE phone_number = %s""",
                    (phone_number,)
                )
            elif filter == "job":
                job = input("Enter job: ").strip()
                cursor.execute(

                    """SELECT * FROM phone_book WHERE job = %s""",
                    (job,)
                )

            results = cursor.fetchall()

            if not results:
                print("No matches found :(")
            else:
                for row in results:
                    print(row)

    except psycopg2.Error as ex:
        print(f"Database error: {ex}")
    except Exception as ex:
        print(f"Unexpected error: {ex}")
        

def data_deleting():
    try:
        first_name = input("Enter first name:").strip()
        phone_number = input("Enter phone number:").strip()

        if not first_name or not phone_number:
            print("Error: First name and phone number cannot be empty")
            return
        
        with conn.cursor() as cursor:
            cursor.execute(

                """DELETE FROM phone_book WHERE first_name = %s AND phone_number = %s""",
                (first_name, phone_number)
            )

            if cursor.rowcount == 0:
                print("Warning: No records were deleted. Check if first name and phone number are correct.")
            else:
                conn.commit() 
                print(f"Success: Deleted {cursor.rowcount} record(s).")


    except psycopg2.Error as ex:
        conn.rollback()  # Roll back the changes in case of an error
        print(f"Database error: {ex}")
    except Exception as ex:
        conn.rollback()  # roll back the changes in case of an unexpected error.
        print(f"Unexpected error: {ex}")

def main_menu():
    while True:
        print("\nHello~~ This is PHONEBOOK MENU")
        print("1 - Upload data from CSV") # upload data from csv file
        print("2 - Add new contact ") # entering user name, phone from console
        print("3 - Update contact") # updating data in the table
        print("4 - Search contacts") # querying data from the tables
        print("5 - Delete contact") # deleting data from tables by username of phon
        print("6 - exit")

        choice = input("Please choose one of this option :): ")

        if choice == '1':
            insert_from_csv()
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            data_querying()
        elif choice == '5':
            data_deleting()
        elif choice == '6':
            print("Goodbye ~~ :)")
            break
        else:
            print("Wrong option! Please choose the option :(")
    

create_table()

# start 
main_menu()

# the end
conn.close()


