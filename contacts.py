import json

menu = """
What do you want to do?
1 - Print list of contacts
2 - Add new contact
3 - Delete contact
q - Exit from application
"""

contacts = []
with open("contacts.json") as f:
    contacts = json.load(f)


def save_contacts():
    data = json.dumps(contacts, indent=2)
    with open("contacts.json", "w") as f:
        f.write(data)


def print_list():
    print("\nYour contacts:")
    for num, contact in enumerate(contacts, start=1):
        print(f"{num}: {contact['name']} / {contact['email']}")


def add_contact():
    print("\nAdd a new contact:")
    name = input("Enter name: ")
    email = input("Enter email: ")

    contacts.append({"name": name, "email": email})
    save_contacts()

    print("Contact was added successfully")


def delete_contact():
    print_list()
    num_to_delete = int(input("Please enter number to delete: "))
    del contacts[num_to_delete - 1]

    save_contacts()
    print("Contact was successfully removed")


def main():
    print("Welcome to Contacts!")

    while True:
        print(menu)
        op = input("Please select menu option: ")

        if op == "1":
            print_list()
        elif op == "2":
            add_contact()
        elif op == "3":
            delete_contact()
        elif op == "q":
            print("Goodbye!")
            return 0
        else:
            print("Unknown operation")


if __name__ == '__main__':
    main()
