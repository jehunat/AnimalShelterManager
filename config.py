import os
from dotenv import load_dotenv

load_dotenv()
# ez szep. tegyel ra valamit, hogy itt elhasaljon, ha valami hianyzik. Aztan ha valami nem jo, akkor elfailel connectionnal
def db_config():
    db ={
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD")
    }
    return db
