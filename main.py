import psycopg2
from TSIS10.config import host, database, user, password

# try to connect with our db 
try:
    # connect to exist db 
    conn = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = database
    )

    conn.autocommit = True

    # the cursor for perfoming database operations 
    with conn.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version {cursor.fetchone()}")

    # create a new table 
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS users(
               id serial PRIMARY KEY,
               first_name varchar(50) NOT NULL,
               nick_name varchar(50) NOT NULL);"""
        )

        print("[INFO] Table created successfully")

    
    # insert data into a table 
    with conn.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (first_name, nick_name) VALUES
                ('Tomiris', 'tomatoma');"""
        )

        print("[INFO] Data was successfully insert")

    # get data from a table 
    with conn.cursor() as cursor:
        cursor.execute(
            """SELECT nick_name FROM users WHERE first_name = 'Tomiris;'"""
        )

        print(cursor.fetchone())

    #  delete a table
    with conn.cursor() as cursor:
        cursor.execute(
            """DROP TABLE users;"""
        )

        print("[INFO] Table was deleted")




# if expect any errors 
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if conn:
        conn.close()
        print("[INFO] PostgreSQL connection closed")