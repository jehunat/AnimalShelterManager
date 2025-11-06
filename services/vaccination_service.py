from .db import Database
import pandas as pd

class VaccinationService:
    def __init__(self, db: Database):
        self.db = db

    def add_vaccination(self, name: str, validity_month: int):
        sql = "INSERT INTO Vaccination(name, validity_month) VALUES (%s, %s)"
        self.db.query(sql, (name, validity_month), fetch=False)
        print(f"Vaccination '{name}' added successfully!")

    def assign_vaccination(self, animal_id: int, vaccination_id: int):
        sql = """
            INSERT INTO AnimalVaccination(animal_id, vaccination_id, date)
            VALUES (%s, %s, CURRENT_DATE)
        """
        self.db.query(sql, (animal_id, vaccination_id), fetch=False)
        print(f"Vaccination {vaccination_id} assigned to animal {animal_id}")
