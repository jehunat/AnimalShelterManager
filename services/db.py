import psycopg2
from psycopg2.extras import RealDictCursor
import pandas as pd
import logging
import streamlit as st
from config import db_config


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Database:
    def __init__(self):
        self.params = db_config()

    def connect(self):
        """ Create and return a new database connection using psycopg2"""
        try:
            conn = psycopg2.connect(**self.params, cursor_factory=RealDictCursor)
            return conn
        except psycopg2.DatabaseError as e:
            logging.error(f"Nem sikerült csatlakozni az adatbázishoz: {e}")
            st.error(f"Nem sikerült csatlakozni az adatbázishoz: {e}")
            raise

    def query(self, sql, params=None, fetch=True):
        """
                Paraméterezett lekérdezés.
                fetch=True -> SELECT lekérdezés, DataFrame-et ad vissza
                fetch=False -> INSERT/UPDATE/DELETE, commit automatikusan
        """
        conn = self.connect()
        try:
            cur = conn.cursor()
            cur.execute(sql, params)

            if fetch and cur.description:
                data = cur.fetchall()
                df = pd.DataFrame(data)
            else:
                conn.commit()
                df = pd.DataFrame()
        except psycopg2.DatabaseError as e:
            conn.rollback()
            logging.error(f"Adatbázis hiba: {e}")
            st.error(f"Adatbázis hiba történt: {e}")
            raise
        finally:
            cur.close()
            conn.close()

        return df


    def init_db(self):
        """ Initialize database tables if they don't exist yet."""
        conn = self.connect()
        try:
            cur = conn.cursor()
            # Create Kennel table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS Kennel (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                capacity INT NOT NULL
            )
            """)

            # Create Animal table
            cur.execute("""
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
            cur.execute("""
            CREATE TABLE IF NOT EXISTS Vaccination (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50) NOT NULL,
                validity_month INT
            )
            """)

            # Create AnimalVaccination table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS AnimalVaccination (
                id SERIAL PRIMARY KEY,
                animal_id INT REFERENCES Animal(id),
                vaccination_id INT REFERENCES Vaccination(id),
                date DATE DEFAULT CURRENT_DATE
            )
            """)

            # Create Log table
            cur.execute("""
            CREATE TABLE IF NOT EXISTS KennelHistory (
                id SERIAL PRIMARY KEY,
                animal_id INT REFERENCES Animal(id),
                kennel_id INT REFERENCES Kennel(id),
                start_date DATE NOT NULL,
                end_date DATE
            )
            """)
            conn.commit()
            logging.info("Adatbázis inicializálása kész.")
        except psycopg2.DatabaseError as e:
            conn.rollback()
            logging.error(f"Hiba az adatbázis inicializálásakor: {e}")
            st.error(f"Hiba az adatbázis inicializálásakor: {e}")
            raise
        finally:
            cur.close()
            conn.close()

# Mitől profi ez a verzió?
# OOP alapú: minden DB funkció egy osztályban, könnyen bővíthető.
# Hibakezelés: try-except minden kritikus ponton + rollback + log + st.error.
# Biztonságos: paraméterezett lekérdezés (%s + tuple) → SQL injection ellen.
# SELECT → DataFrame automatikus: Streamlit-be közvetlenül beadható.
# Tranzakciók kezelése: minden nem-SELECT automatikusan commitol, hiba esetén rollback.
# Init DB: táblák létrehozása hibakezeléssel.
# Logging: minden fontos esemény logolva van, nem csak print.
