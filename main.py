contacts = []

def add_contact(name, phone):
    contacts.append({"name": name, "phone": phone})
    print(f"Contact {name} added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found")
    else:
        print("\nContact List:")
        for i, contact in enumerate(contacts, 1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

# Adding contacts
add_contact("Alice", "1234567890")
add_contact("Bob", "9876543210")

# Viewing contacts
view_contacts() 