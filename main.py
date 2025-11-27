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

def search_contact(name):
   found =[contact for contact in contacts if contact["name"].lower() == name.lower()]
   if found:
      for contact in found:
          print(f"\nfound: {contact['name']} - {contact['phone']}")
   else:
      print("\nSorry, no contact found with the name you searched.")
search_contact("Alice")
