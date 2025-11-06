from .db import Database
import pandas as pd

class KennelService:
    def __init__(self, db: Database):
        self.db = db

    def add_kennel(self, name: str, capacity: int):
        """Új kennel hozzáadása"""
        sql = "INSERT INTO Kennel(name, capacity) VALUES (%s, %s)"
        self.db.query(sql, (name, capacity), fetch=False)
        print(f"Kennel '{name}' added successfully")

    def list_kennels(self) -> pd.DataFrame:
        """Az összes kennel listázása"""
        sql = "SELECT * FROM Kennel"
        return self.db.query(sql)
