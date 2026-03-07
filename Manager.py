from Contact import Contact, CampusContact

class ContactManager:

    def __init__(self):
        self.__contacts = []

    def add_contact(self, contact):

        self.__contacts.append(contact)

    def add_normal_contact(self, name, phone, location):
        """
        Create and add normal contact.
        """
        new_contact = Contact(name, phone, location)
        self.add_contact(new_contact)
        return new_contact

    def add_campus_contact(self, name, phone, location, department):
        """
        Create and add campus contact.
        """
        new_contact = CampusContact(name, phone, location, department)
        self.add_contact(new_contact)
        return new_contact

    def get_all_contacts(self):
        """
        Return copy of contacts list.
        """
        return self.__contacts[:]

    def find_contacts_by_name(self, search_text):
        """
        Find contacts by name (case-insensitive).
        """
        results = []
        search_text = search_text.lower()
        for contact in self.__contacts:
            if search_text in contact.get_name().lower():
                results.append(contact)
        return results

    def get_contact_count(self):
        """
        Return number of contacts.
        """
        return len(self.__contacts)

    def clear_all_contacts(self):
        """
        Clear the list.
        """
        self.__contacts = []