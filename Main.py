from manager import ContactManager

def show_menu():
    print("\nContact Manager Menu:")
    print("1. Add normal contact")
    print("2. Add campus contact")
    print("3. Show all contacts")
    print("4. Find contact by name")
    print("5. Show contact count")
    print("6. Clear all contacts")
    print("7. Exit")
    return input("Choose an option: ")

def main():
    manager = ContactManager()  # Create instance of manager class
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            location = input("Location: ")
            manager.add_normal_contact(name, phone, location)
            print("Added normal contact.")
        
        elif choice == "2":
            name = input("Name: ")
            phone = input("Phone: ")
            location = input("Location: ")
            department = input("Department: ")
            manager.add_campus_contact(name, phone, location, department)
            print("Added campus contact.")
        
        elif choice == "3":
            contacts = manager.get_all_contacts()
            if not contacts:
                print("No contacts.")
            else:
                print("\nAll Contacts:")
                for contact in contacts:
                    print(contact.get_details())
        
        elif choice == "4":
            search = input("Search name: ")
            results = manager.find_contacts_by_name(search)
            if not results:
                print("No matches.")
            else:
                print("\nFound:")
                for contact in results:
                    print(contact.get_details())
        
        elif choice == "5":
            print(f"Total: {manager.get_contact_count()}")
        
        elif choice == "6":
            manager.clear_all_contacts()
            print("Cleared all.")
        
        elif choice == "7":
            print("Bye!")
            break
        
        else:
            print("Bad choice. Try again.")

if __name__ == "__main__":
    main()