import json

try:
    with open("contacts.json", "r") as file:
        contacts = json.load(file)

except FileNotFoundError:
    contacts = []

program_running = True


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)


def validate_name(name):

    name = name.strip()

    if len(name) == 0:
        print("Name cannot be empty!")
        return False

    if len(name) < 2:
        print("Name must be at least 2 characters!")
        return False

    if len(name) > 30:
        print("Name cannot be longer than 30 characters!")
        return False

    return True


def validate_phone(phone):
    phone = phone.strip()

    if len(phone) == 0:
        print("Phone cannot be empty!")
        return False

    if not phone.isdigit():
        print("Phone must contain only numbers!")
        return False

    if len(phone) != 11:
        print("Phone number must be 11 digits!")
        return False

    if not phone.startswith("09"):
        print("Phone number must start with 09")
        return False

    return True


def validate_email(email):
    email = email.strip()

    if len(email) == 0:
        print("Email cannot be empty!")
        return False

    if email.count("@") != 1:
        print("Invalid email!")
        return False

    username, domain = email.split("@")

    if len(username) == 0:
        print("Invalid email!")
        return False

    if "." not in domain:
        print("Invalid email!")
        return False

    if domain.startswith(".") or domain.endswith("."):
        print("Invalid email!")
        return False

    return True


def phone_exists(phone):
    for contact in contacts:
        if contact["phone"] == phone:
            return True

    return False


def name_exists(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return True

    return False


def add_contact():

    print("\n----------ADD CONTACT----------\n")

    while True:
        name = input("Name: ")

        if not validate_name(name):
            continue

        if name_exists(name):
            print("This name already exists!")
            continue

        break

    while True:
        phone = input("Phone: ")

        if not validate_phone(phone):
            continue

        if phone_exists(phone):
            print("This number already exists!")
            continue

        break

    while True:
        email = input("Email: ")

        if validate_email(email):
            break

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts()

    print("\nContact added successfully!\n")


def show_contacts():
    print("\n----------CONTACTS----------\n")

    if len(contacts) == 0:
        print("No contacts found!\n")
        return

    for contact in contacts:
        print("Name: ", contact["name"])
        print("Phone: ", contact["phone"])
        print("Email: ", contact["email"])
        print("--------------------")


def search_contact():
    print("\n----------SEARCH CONTACT----------\n")

    search = input("Search: ")

    found = False

    for contact in contacts:

        if search.lower() in contact["name"].lower():
            print("\nName: ", contact["name"])
            print("Phone: ", contact["phone"])
            print("Email: ", contact["email"])
            print("--------------------")
            found = True
    if not found:
        print("\nContact not found!\n")


def edit_contact():
    print("\n----------EDIT CONTACT----------\n")

    search = input("Enter contact name: ")

    found = False

    for contact in contacts:
        if search.lower() == contact["name"].lower():
            print("\n1. Name")
            print("2. Phone")
            print("3. Email")

            while True:
                option = input("\nWhat do you want to edit? ")

                if option in ["1", "2", "3"]:
                    break

                print("\nInvalid option!\nPlease choose 1, 2 or 3.\n")

            if option == "1":
                while True:
                    new_name = input("\nEnter your new name: ")

                    if validate_name(new_name):
                        contact["name"] = new_name
                        break

            elif option == "2":
                while True:
                    new_phone = input("\nEnter your new phone: ")

                    if validate_phone(new_phone):
                        contact["phone"] = new_phone
                        break

            elif option == "3":
                while True:
                    new_email = input("\nEnter your new email: ")

                    if validate_email(new_email):
                        contact["email"] = new_email
                        break

            save_contacts()

            print("\nContact updated successfully!")

            found = True
            break

    if not found:
        print("\nContact not found!\n")


def delete_contact():
    print("\n----------DELETE CONTACT----------\n")

    search = input("Enter contact name: ")

    found = False

    for contact in contacts:
        if search.lower() == contact["name"].lower():
            print("\nName: ", contact["name"])
            print("Phone: ", contact["phone"])
            print("Email: ", contact["email"])

            while True:
                confirm = input(
                    "\nAre you sure you want to delete this contact? (y/n): ").lower()

                if confirm in ["y", "n"]:
                    break

                print("\nInvalid option!\nPlease enter y or n.\n")

            if confirm == "y":
                contacts.remove(contact)
                save_contacts()

                print("\nContact deleted successfully!\n")

            else:
                print("\nDeletion cancelled.\n")

            found = True
            break

    if not found:
        print("\nContact not found!")


def exit_from_program():
    return False


while (program_running):
    y = "=" * 30

    print(y, "\n", "      CONTACT MANAGER", "\n", y)

    print("\n",
          "1. Add Contact\n",
          "2. Show Contacts\n",
          "3. Search Contact\n",
          "4. Edit Contact\n",
          "5. Delete Contact\n",
          "6. Exit\n"
          )

    option = input("Choose an option: ")

    if option == "1":
        add_contact()

    elif option == "2":
        show_contacts()

    elif option == "3":
        search_contact()

    elif option == "4":
        edit_contact()

    elif option == "5":
        delete_contact()

    elif option == "6":
        program_running = exit_from_program()

    else:
        print("\nInvalide option!\nPlease choose a number between 1 and 6.\n")
