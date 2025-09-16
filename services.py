from db import connect

# csinalhatnal valami meno valtozas kezeles kovetest is.
def add_kennel(name, capacity):
    conn = connect()
    cur = conn.cursor()
    cur.execute(f"INSERT INTO Kennel (name, capacity) VALUES ('{name}', {capacity})")
    conn.commit()
    cur.close()
    conn.close()
    # return es ne printelj
    print(f"Kennel '{name}' added successfully")


def add_animal(name, species, breed, birth_date, kennel_id=None):
    # hol van az, amikor orokbe lett fogadva?
    # old meg, hogy ne ismetlodjon minden funkciobna a csatlakozas es lecsatlakozas
    # contextmanager
    conn = connect()
    cur = conn.cursor()

    if kennel_id:
        # %s szep hasznald ezt mindenhol.
        cur.execute("""
                    INSERT INTO Animal (name, species, breed, birth_date, arrival_date, kennel_id, status)
                    VALUES (%s, %s, %s, %s, CURRENT_DATE, %s, 'active')
                """, (name, species, breed, birth_date, kennel_id))
    else:
        cur.execute("""
                    INSERT INTO Animal (name, species, breed, birth_date, arrival_date, status)
                    VALUES (%s, %s, %s, %s, CURRENT_DATE, 'active')
                """, (name, species, breed, birth_date))

    conn.commit()
    cur.close()
    conn.close()
    print(f"Animal '{name}' added successfully")


def add_vaccination(name, validity_month):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO Vaccination (name, validity_month) VALUES (%s, %s)", (name, validity_month))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Vaccination '{name}' added successfully!")


def assign_vaccination(animal_id, vaccination_id):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
            INSERT INTO AnimalVaccination (animal_id, vaccination_id, date)
            VALUES (%s, %s, CURRENT_DATE)
        """, (animal_id, vaccination_id))
    conn.commit()
    cur.close()
    conn.close()
    print(f"Vaccination {vaccination_id} assigned to animal {animal_id}")


def list_animals():
    # miert vaan ketszer a name?
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
    SELECT a.id, a.name, a.name, a.species, a.breed, a.birth_date, a.arrival_date, a.status, k.name AS kennel_name
    FROM Animal a
    LEFT JOIN Kennel k ON a.kennel_id = k.id
    """)
    animals = cur.fetchall()
    cur.close()
    conn.close()

    for a in animals:
        print(f"ID: {a['id']} | Name: {a['name']} | Species: {a['species']} Breed: {a['breed']} | Kennel: {a['kennel_name']}")


def list_kennels():
    #mova animal? mi van akkor ha atkerul egy masik kernelbe?
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Kennel")
    kennels = cur.fetchall()
    cur.close()
    conn.close()
    for kennel in kennels:
        print(f"ID: {kennel['id']} | Name: {kennel['name']} | Capacity: {kennel['capacity']}")


def list_unvaccinated_animals():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
            SELECT a.id, a.name, a.species
            FROM Animal a
            WHERE NOT EXISTS (
                SELECT 1 FROM AnimalVaccination av WHERE av.animal_id = a.id
            )
        """)
    animals = cur.fetchall()
    cur.close()
    conn.close()

    print("\nUnvaccinated animals:")
    for a in animals:
        print(f"ID: {a['id']} | Name: {a['name']} | Species: {a['species']}")
