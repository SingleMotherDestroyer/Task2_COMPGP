class Contact:
    """Base class for all contacts, demonstrating Encapsulation."""
    def __init__(self, name, phone, location):
        self.__name = name
        self.__phone = phone
        self.__location = location

    def get_name(self):
        return self.__name

    def get_location(self):
        return self.__location

    def get_details(self):
        """Polymorphic method to be overridden by subclasses."""
        return f"Name: {self.__name} | Phone: {self.__phone} | Location: {self.__location}"

class CampusContact(Contact):
    """Subclass for HKMU Staff/Students, demonstrating Inheritance."""
    def __init__(self, name, phone, location, department):
        super().__init__(name, phone, location)
        self.department = department

    def get_details(self):
        """Method Overriding - Polymorphism in action."""
        return f"[Campus] {super().get_details()} | Dept: {self.department}"
