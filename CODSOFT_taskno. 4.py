

contacts = {}


def display_menu():
    print("\n<<<--- Contact Book --->>>")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("<<------------------------>>")


def add_contact():
    name = input("Enter the contact name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address,
        
    }
    print(f"\nContact for {name} has been added successfully!")


def view_contact_list():
    if not contacts:
        print("\n No contacts available.")
    else:
        print("\nContact List:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")


def search_contact():
    query = input("Enter the name or phone number to search: ")
    
    for name, details in contacts.items():
        if query.lower() == name.lower() or query == details['phone']:
            print(f"\nContact found: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            return
    
    print("\nContact not found.")


def update_contact():
    name = input("Enter the name of the contact you want to update: ")
    
    if name in contacts:
        print(f"\nUpdating contact for {name}. Leave blank to keep current value.")
        phone = input(f"Current phone ({contacts[name]['phone']}): ")
        email = input(f"Current email ({contacts[name]['email']}): ")
        address = input(f"Current address ({contacts[name]['address']}): ")
        
        contacts[name]['phone'] = phone if phone else contacts[name]['phone']
        contacts[name]['email'] = email if email else contacts[name]['email']
        contacts[name]['address'] = address if address else contacts[name]['address']
        
        print(f"\nContact for {name} has been updated successfully!")
    else:
        print(f"\nContact for {name} not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    
    if name in contacts:
        del contacts[name]
        print(f"\nContact for {name} has been deleted.")
    else:
        print(f"\nContact for {name} not found.")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact_list()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("\nExiting the system.")
            break
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
