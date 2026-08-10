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
    addContact()

elif option == "2":
    showContacts()

elif option == "3":
    searchContact()

elif option == "4":
    editContact()

elif option == "5":
    deleteContact()

elif option == "6":
    exitFromProgram()
