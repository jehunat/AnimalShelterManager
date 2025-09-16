from services import *


def menu():
    print("\n--- Animal Shelter Management ---")
    while True:
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