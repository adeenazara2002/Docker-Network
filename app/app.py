import mysql.connector

def main():
    try:
        connection = mysql.connector.connect(
            host="mysql_db_container",
            user="adinazara",
            password="adina123",
            database="testdb"
        )
        print("Successfully connected to the database!")

        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")

        tables = cursor.fetchall()
        print("Tables in the database:")
        for table in tables:
            print(table)

        cursor.close()
        connection.close()

    except mysql.connector.Error as err:
        print(f"Error: {err}")

if __name__ == "__main__":
    main()
