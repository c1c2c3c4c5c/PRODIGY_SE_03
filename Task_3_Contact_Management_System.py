class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name} | Phone Number: {self.phone_number} | Email: {self.email}"

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_email(self, email):
        self.email = email


class ContactManagementSystem:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self):
        name = input("Enter the name of the person: ")
        phone_number = input("Enter the phone number of the person: ")
        email = input("Enter the email ID of the person: ")

        contact = Contact(name, phone_number, email)
        self.contacts.append(contact)
        print("New contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self):
        name = input("Enter the name of the contact to edit: ")
        found = False
        
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_phone_number = input("Enter the new phone number: ")
                new_email = input("Enter the new email ID: ")
                contact.set_phone_number(new_phone_number)
                contact.set_email(new_email)
                print("Contact details updated successfully.")
                found = True
                break
        
        if not found:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        found = False
        
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully!")
                found = True
                break
        
        if not found:
            print("Contact not found.")

    def run(self):
        while True:
            print("\nWelcome to Contact Management System Menu:")
            print("1. Add a new contact")
            print("2. View contacts")
            print("3. Edit a contact")
            print("4. Delete a contact")
            print("5. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                self.add_contact()
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                self.edit_contact()
            elif choice == '4':
                self.delete_contact()
            elif choice == '5':
                print("Exiting the Contact Management System...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()
