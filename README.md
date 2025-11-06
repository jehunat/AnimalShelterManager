# 🐾 Animal Shelter Management System

A web-based application built with **Streamlit** and **PostgreSQL** for managing animal shelters. This system allows shelter staff to easily track animals, kennels, vaccinations, and unvaccinated animals through a user-friendly browser interface.

---

## Features

* **Home Dashboard**: Welcome page with navigation.
* **Animals Management**: Add new animals, view all animals, assign them to kennels.
* **Kennels Management**: Add and view kennels with capacities.
* **Vaccinations Management**: Add new vaccinations and assign them to animals.
* **Unvaccinated Animals**: Quickly see which animals still need vaccinations.

---

## Tech Stack

* **Frontend / UI**: [Streamlit](https://streamlit.io/)
* **Database**: [PostgreSQL](https://www.postgresql.org/)
* **Python Libraries**:

  * `psycopg2` for database connection
  * `pandas` for data handling
  * `streamlit-option-menu` for sidebar navigation
  * `python-dotenv` for local environment configuration

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/jehunat/animal-shelter-manager.git
   cd animal-shelter-manager
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure your database:

   * **Streamlit Cloud**: Add your PostgreSQL credentials in `st.secrets`.
   * **Local**: Create a `.env` file:

     ```env
     DB_HOST=localhost
     DB_NAME=animal_shelter
     DB_USER=postgres
     DB_PASSWORD=yourpassword
     DB_PORT=5432
     ```

---

## Usage

Run the app with Streamlit:

```bash
streamlit run app.py
```

Open the URL provided by Streamlit in your browser (usually `http://localhost:8501`).

---

## Project Structure

```
animal-shelter-manager/
│
├── app.py                 # Main Streamlit app
├── config.py              # DB configuration
├── services/
│   ├── animal_service.py
│   ├── kennel_service.py
│   └── vaccination_service.py
├── services/db.py         # Database class with initialization
├── requirements.txt
└── README.md
```

---

## Database Initialization

The app automatically initializes the required tables if they do not exist:

* `Kennel`
* `Animal`
* `Vaccination`
* `AnimalVaccination`
* `KennelHistory`

---

## Features Explained

### Animals

* Add new animals with optional kennel assignment.
* View all animals in a table with their details and kennel assignment.

### Kennels

* Add new kennels with capacity.
* View list of kennels.

### Vaccinations

* Add new vaccination types.
* Assign vaccinations to animals.

### Unvaccinated Animals

* Shows all animals that have not received any vaccination yet.

---

## Best Practices

* **OOP-based**: Each service and database functionality is encapsulated in classes for easy maintenance and expansion.
* **Error Handling**: Database operations are wrapped in try-except blocks with logging and rollback.
* **SQL Injection Safe**: Parameterized queries using `%s`.
* **Streamlit Ready**: DataFrames are returned directly for easy display in Streamlit tables.

---

## License

MIT License
