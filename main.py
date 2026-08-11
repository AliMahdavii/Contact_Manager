contacts = []
program_running = True


def add_contact():

    print("\n----------ADD CONTACT----------\n")

    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)

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

            option = input("\nWhat do you want to edit? ")

            if option == "1":
                contact["name"] = input("\nEnter your new name: ")

            elif option == "2":
                contact["phone"] = input("\nEnter your new phone: ")

            elif option == "3":
                contact["email"] = input("\nEnter your new email: ")

            print("\nContact updated successfully!")

            found = True

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

            confirm = input(
                "\nAre you sure you want to delete this contact? (y/n): ")

            if confirm.lower() == "y":
                contacts.remove(contact)

                print("\nContact deleted successfully!\n")

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
