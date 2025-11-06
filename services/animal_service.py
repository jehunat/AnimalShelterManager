from .db import Database


class AnimalService:
    """The logic of Animal entities"""
    def __init__(self, db: Database):
        self.db = db

    def add_animal(self, name, species, breed, birth_date, kennel_id=None):
        if kennel_id:
            self.db.query(
            """
                INSERT INTO Animal (name, species, breed, birth_date, arrival_date, kennel_id, status)
                VALUES (%s, %s, %s, %s, CURRENT_DATE, %s, 'active')
                """,
                (name, species, breed, birth_date, kennel_id),
            fetch=False)
        else:
            self.db.query(
                """
                    INSERT INTO Animal (name, species, breed, birth_date, arrival_date, status)
                    VALUES (%s, %s, %s, %s, CURRENT_DATE, 'active')
                    """,
                (name, species, breed, birth_date),
                fetch=False
            )
        #print(f"Animal '{name}' added successfully")

    def get_all_animals(self):
        return self.db.query(
            """
            SELECT a.id, a.name, a.species, a.breed, a.birth_date, a.arrival_date, k.name AS kennel
            FROM Animal a
            LEFT JOIN Kennel k ON a.kennel_id = k.id
            ORDER BY a.id
            """
        )
        #for a in animals:
        #    print(f"ID: {a['id']} | Name: {a['name']} | Species: {a['species']} Breed: {a['breed']} | Kennel: {a['kennel_name']}")

    def get_unvaccinated_animals(self):
        return self.db.query("""
                    SELECT a.id, a.name, a.species, a.breed, a.birth_date, a.arrival_date, k.name AS kennel
                    FROM Animal a
                    LEFT JOIN Kennel k ON a.kennel_id = k.id
                    ORDER BY a.id
                """)
