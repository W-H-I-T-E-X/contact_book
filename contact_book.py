# Contact Book Application

# List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("Contact added successfully!")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

# Function to search for a contact by name or phone number
def search_contact():
    search_term = input("Enter Name or Phone Number to search: ")
    found_contacts = [contact for contact in contacts if search_term in contact['name'] or search_term in contact['phone']]
    
    if found_contacts:
        for contact in found_contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No contacts found with that search term.")

# Function to update a contact
def update_contact():
    search_term = input("Enter Name or Phone Number to update: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            print("Contact found. Enter new details (leave blank to keep current):")
            new_name = input(f"New Name (current: {contact['name']}): ") or contact['name']
            new_phone = input(f"New Phone (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"New Email (current: {contact['email']}): ") or contact['email']
            new_address = input(f"New Address (current: {contact['address']}): ") or contact['address']
            contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
            print("Contact updated successfully!")
            return
    print("Contact not found.")

# Function to delete a contact
def delete_contact():
    search_term = input("Enter Name or Phone Number to delete: ")
    for contact in contacts:
        if search_term in contact['name'] or search_term in contact['phone']:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return
    print("Contact not found.")

# Function to display the main menu
def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting the Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the application
if __name__ == "__main__":
    main_menu()
