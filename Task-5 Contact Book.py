# Task 5: Contact Book
contacts = {}

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        # Save all details in a dictionary under the person's name
        contacts[name] = {"phone": phone, "email": email, "address": address}
        print(name, "has been added to your contacts.")
        
    elif choice == '2':
        print("\n--- All Contacts ---")
        if len(contacts) == 0:
            print("Your contact book is empty.")
        else:
            for name, details in contacts.items():
                print("Name:", name, "| Phone:", details["phone"])
                
    elif choice == '3':
        search = input("Enter name or phone number to search: ")
        found = False
        for name, details in contacts.items():
            if search.lower() in name.lower() or search == details["phone"]:
                print("\nFound Contact:")
                print("Name:", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("Address:", details["address"])
                found = True
        if not found:
            print("No contact found.")
            
    elif choice == '4':
        name = input("Enter the exact name of the contact to update: ")
        if name in contacts:
            print("Leave the space blank and press Enter if you don't want to change a specific detail.")
            
            new_phone = input("Enter new phone: ")
            if new_phone != "":
                contacts[name]["phone"] = new_phone
                
            new_email = input("Enter new email: ")
            if new_email != "":
                contacts[name]["email"] = new_email
                
            new_address = input("Enter new address: ")
            if new_address != "":
                contacts[name]["address"] = new_address
                
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
            
    elif choice == '5':
        name = input("Enter the exact name of the contact to delete: ")
        if name in contacts:
            del contacts[name]
            print(name, "has been deleted.")
        else:
            print("Contact not found.")
            
    elif choice == '6':
        print("Exiting Contact Book.")
        break
        
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")