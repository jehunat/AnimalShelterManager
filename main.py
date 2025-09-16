from services import *


def menu():
    print("\n--- Animal Shelter Management ---")
    while True:
        # while true az ordog muve., ezt csak akkor lehet hasznalni, ha az ordog a lelkedet akarja. while user_response !=0
        # keruld ezeket a printeket, ifeket, probald meg valahogy ugy megoldani, hogyha kivalasztja az user, az adott menut, akkor egy funkcio meghivodik es az keri be a tovabbi inputokat
        # csoportosisd funkcio szerint, (add, list, assign) valami ilyesmi:
        # errorhandling szep, de mi van az osszes tobbi mezo error handlingjevel?

# MAIN_MENU = {
#     "Add": {
#        1: ("New kennel", add_kennel),
#        2: ("New animal", add_animal),
#        3: ("New vaccination", add_vaccination),
    #  },
        # keress ra a function reference execution -ra pythonban.
        # for fun. adj hozza jogosultsag kezelest. 
        print("1. Add new kennel")
        print("2. Add new animal")
        print("3. Add new vaccination")
        print("4. Assign vaccination to animal")
        print("5. List all animals")
        print("6. List all kennels")
        print("7. Show unvaccinated animals")
        print("0. Exit")

        user_response = int(input("Please select!"))

        if user_response == 1:
            name = input("Kennel name: ")
            capacity = int(input("Capacity: "))
            add_kennel(name, capacity)
        elif user_response == 2:
            name = input("Animal name: ")
            species = input("Species: ")
            breed = input("Breed: ")
            birth_date = input("Birth date (YYYY-MM-DD): ")
            kennel_id = input("Kennel ID (or leave empty): ") or None
            add_animal(name, species, breed, birth_date, kennel_id)
        elif user_response == 3:
            name = input("Vaccination name: ")
            validity = int(input("Validity in months: "))
            add_vaccination(name, validity)
        elif user_response == 4:
            animal_id = int(input("Animal ID: "))
            vaccination_id = int(input("Vaccination ID: "))
            assign_vaccination(animal_id, vaccination_id)
        elif user_response == 5:
            list_animals()
        elif user_response == 6:
            list_kennels()
        elif user_response == 7:
            list_unvaccinated_animals()
        elif user_response == 0:
            print("Goodbye")
            exit()
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    menu()
