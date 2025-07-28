import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(name, phone):
    contacts = load_contacts()
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Added contact: {name}")

def delete_contact(name):
    contacts = load_contacts()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Deleted {name}")
    else:
        print("Not found")

def edit_contact(name, new_phone):
    contacts = load_contacts()
    if name in contacts:
        contacts[name] = new_phone
        save_contacts(contacts)
        print(f"Updated {name}")
    else:
        print("Contact not found")

def search_contact(name):
    contacts = load_contacts()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Not found")

def export_contacts():
    with open("contacts.txt", "w") as f:
        contacts = load_contacts()
        for name, phone in contacts.items():
            f.write(f"{name}: {phone}\n")
    print("Exported to contacts.txt")

# CLI Handler
import sys
if len(sys.argv) < 2:
    print("Usage: python contact_book.py [add|edit|delete|search|export] <args>")
    exit()

command = sys.argv[1]

if command == "add":
    add_contact(sys.argv[2], sys.argv[3])
elif command == "edit":
    edit_contact(sys.argv[2], sys.argv[3])
elif command == "delete":
    delete_contact(sys.argv[2])
elif command == "search":
    search_contact(sys.argv[2])
elif command == "export":
    export_contacts()
