import psycopg2
from config import config


def connect():
    connection = None

    try:
        params = config()
        print("Connecting to the postgreSQL database...")
        connection = psycopg2.connect(**params)

        cursor = connection.cursor()
        print("PostgreSQL database version: ")
        cursor.execute("SELECT version()")
        db_verison = cursor.fetchone()
        print(db_verison)
        cursor.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print("Database connection terminated.")

if __name__ == "__main__":
    connect()