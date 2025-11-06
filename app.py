import streamlit as st
from streamlit_option_menu import option_menu
from services.animal_service import AnimalService
from services.db import Database


class App:
    def __init__(self):
        self.db = Database()
        self.db.init_db()
        self.animal_service = AnimalService(self.db)
        self.selected_page = None
        st.set_page_config(
            page_title="🐾 Animal Shelter Management",
            page_icon="🐶",
            layout="wide"
        )
        self.render_sidebar()

    def render_sidebar(self):
        with st.sidebar:
            self.selected_page = option_menu(
                menu_title="🐾 Animal Shelter",
                options=[
                    "🏠 Home",
                    "🐶 Animals",
                    "🏡 Kennels",
                    "💉 Vaccinations",
                    "📊 Unvaccinated"
                ],
                icons=["house", "dog", "home", "capsule", "bar-chart"],
                menu_icon="paw",
                default_index=0
            )

    def render_page(self):
        if self.selected_page == "🏠 Home":
            st.title("🏠 Animal Shelter Management System")
            st.write("Welcome to the Animal Shelter administration system!")
        elif self.selected_page == "🐶 Animals":
            self.page_animals()
        elif self.selected_page == "🏡 Kennels":
            self.page_kennels()
        elif self.selected_page == "💉 Vaccinations":
            self.page_vaccinations()
        elif self.selected_page == "📊 Unvaccinated":
            self.page_unvaccinated()

    def page_home(self):
        st.title("🏠 Animal Shelter Management System")
        st.write("Üdvözöl az állatmenhely adminisztrációs rendszere!")
        st.info("Használd a bal oldali menüt az adatok kezeléséhez.")

    def page_animals(self):
        st.title("🐶 Animals")

        with st.expander("➕ Add new animal"):
            with st.form("add_animal_form", clear_on_submit=True):
                name = st.text_input("Name")
                species = st.text_input("Species")
                breed = st.text_input("Breed")
                birth_date = st.date_input("Birth date")
                kennel_id = st.number_input("Kennel ID (optional)", min_value=0, step=1)
                submitted = st.form_submit_button("Add Animal")

                if submitted:
                    if kennel_id > 0:
                        self.db.query(
                            """
                            INSERT INTO Animal (name, species, breed, birth_date, kennel_id)
                            VALUES (%s, %s, %s, %s, %s)
                            """,
                            (name, species, breed, birth_date, kennel_id),
                            fetch=False
                        )
                    else:
                        self.db.query(
                            """
                            INSERT INTO Animal (name, species, breed, birth_date)
                            VALUES (%s, %s, %s, %s)
                            """,
                            (name, species, breed, birth_date),
                            fetch=False
                        )
                    st.success(f"Animal '{name}' added successfully!")

        df = self.db.query("""
            SELECT a.id, a.name, a.species, a.breed, a.birth_date, a.arrival_date, k.name AS kennel
            FROM Animal a
            LEFT JOIN Kennel k ON a.kennel_id = k.id
            ORDER BY a.id
        """)
        st.dataframe(df, use_container_width=True)

    def page_kennels(self):
        st.title("🏡 Kennels")

        with st.expander("➕ Add new kennel"):
            with st.form("add_kennel_form", clear_on_submit=True):
                name = st.text_input("Kennel name")
                capacity = st.number_input("Capacity", min_value=1, step=1)
                submitted = st.form_submit_button("Add Kennel")

                if submitted:
                    self.db.query(
                        "INSERT INTO Kennel (name, capacity) VALUES (%s, %s)",
                        (name, capacity),
                        fetch=False
                    )
                    st.success(f"Kennel '{name}' added successfully!")

        df = self.db.query("SELECT * FROM Kennel ORDER BY id")
        st.dataframe(df, use_container_width=True)

    def page_vaccinations(self):
        st.title("💉 Vaccinations")

        with st.expander("➕ Add new vaccination"):
            with st.form("add_vaccination_form", clear_on_submit=True):
                name = st.text_input("Vaccination name")
                validity = st.number_input("Validity (months)", min_value=1, step=1)
                submitted = st.form_submit_button("Add Vaccination")

                if submitted:
                    self.db.query(
                        "INSERT INTO Vaccination (name, validity_month) VALUES (%s, %s)",
                        (name, validity),
                        fetch=False
                    )
                    st.success(f"Vaccination '{name}' added successfully!")

        df = self.db.query("SELECT * FROM Vaccination ORDER BY id")
        st.dataframe(df, use_container_width=True)

    def page_unvaccinated(self):
        st.title("📊 Unvaccinated Animals")
        df = self.db.query("""
            SELECT a.id, a.name, a.species
            FROM Animal a
            WHERE NOT EXISTS (
                SELECT 1 FROM AnimalVaccination av WHERE av.animal_id = a.id
            )
            ORDER BY a.id
        """)
        if df.empty:
            st.success("🎉 Every animals are vaccinated!")
        else:
            st.warning("The following animals are not vaccinated:")
            st.dataframe(df, use_container_width=True)

if __name__ == "__main__":
    app = App()
    app.render_page()