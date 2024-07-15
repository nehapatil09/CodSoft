class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
        
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"
    
class ContactBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully")
        
    def view_contacts(self):
        for contact in self.contacts:
            print(contact)
            
    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                print(contact)
                
    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")
        
    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact delected successfully.")
                return
        print("Contact not found")
            
            
def main():
    contact_book = ContactBook()
    
    while True:
        print("\n Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter Phone: ")
            email = input("Enter Email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            
        elif choice == '2':
            contact_book.view_contacts()
            
        elif choice == '3':
            search_term = input("Enter name or phone to search: ")
            contact_book.search_contact(search_term)
            
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
            
        elif choice == '5':
            name = input("Enter the name of the contact to delet: ")
            contact_book.delete_contact(name)
            
        elif choice == '6':
            print("Exiting Contact Book.")
            break
        
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()