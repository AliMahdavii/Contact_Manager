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
    print("\n----------CONTACT----------\n")

    if len(contacts) == 0:
        print("No contacts found!\n")
        return

    for contact in contacts:
        print("Name: ", contact["name"])
        print("Phone: ", contact["phone"])
        print("Email: ", contact["email"])
        print("--------------------")


def search_contact():
    pass


def edit_contact():
    pass


def delete_contact():
    pass


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
