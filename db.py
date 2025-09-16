import psycopg2
from psycopg2.extras import RealDictCursor
from config import db_config


def connect():
    """ Create and return a new database connection using psycopg2"""
    try:
        params = db_config()
        print("Connecting to the postgreSQL database...")
        conn = psycopg2.connect(**params, cursor_factory=RealDictCursor)
        return conn
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)


def init_db():
    """ Initialize database tables if they don't exist yet."""
    conn = connect()
    cursor = conn.cursor()

    # Create Kennel table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Kennel (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        capacity INT NOT NULL
    )
    """)

    # Create Animal table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Animal (
        id SERIAL PRIMARY KEY,
        name VARCHAR(80) NOT NULL,
        species VARCHAR(80) NOT NULL,
        breed VARCHAR(80),
        birth_date DATE,
        arrival_date DATE DEFAULT CURRENT_DATE NOT NULL,
        status VARCHAR(50) DEFAULT 'active',
        kennel_id INT REFERENCES Kennel(id)
    )
    """)

    # Create Vaccination table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vaccination (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        validity_month INT
    )
    """)

    # Create AnimalVaccination table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS AnimalVaccination (
        id SERIAL PRIMARY KEY,
        animal_id INT REFERENCES Animal(id),
        vaccination_id INT REFERENCES Vaccination(id),
        date DATE DEFAULT CURRENT_DATE
    )
    """)

    # Create Log table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS KennelHistory (
        id SERIAL PRIMARY KEY,
        animal_id INT REFERENCES Animal(id),
        kennel_id INT REFERENCES Kennel(id),
        start_date DATE NOT NULL,
        end_date DATE
    )
    """)

    conn.commit()
    cursor.close()
    conn.close()
