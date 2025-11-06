import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def db_config():
    """
    Returns the database configuration.
    - Streamlit Cloud: using st.secrets
    - Local development: .env variables
    """
    try:
        if "DB_HOST" in st.secrets:
            return {
                "host": st.secrets["DB_HOST"],
                "database": st.secrets["DB_NAME"],
                "user": st.secrets["DB_USER"],
                "password": st.secrets["DB_PASSWORD"],
                "port": int(st.secrets.get("DB_PORT", 5432))
            }
    except Exception:
        pass

    return {
        "host": os.getenv("DB_HOST"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
        "port": int(os.getenv("DB_PORT", 5432))
    }
