import os
from dotenv import load_dotenv

load_dotenv()

def db_config():
    db ={
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    return db