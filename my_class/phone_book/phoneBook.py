from my_class.phone_book.contact import contact


class phonebook:

    def __init__(self):
        self.contacts = []

    def create_contact(self, first_name, last_name, phone_number, email_address):
        new_contact = contact(first_name + " " + last_name, phone_number, email_address)
        self.contacts.append(new_contact)

    def count_contact(self):
        return len(self.contacts)

    def view_contact(self, name):
        for each in self.contacts:
            if name == each.get_contact_name():
                return each.__str__()

    def edit_contact(self, initial_name, first_name, last_name, phone_number, email_address):
        for each in range(0, len(self.contacts)):
            if initial_name == self.contacts[each].get_contact_name():
                self.contacts[each].set_contact_name(first_name + " " + last_name)
                self.contacts[each].set_phone_number(phone_number)
                self.contacts[each].set_email_address(email_address)
                self.contacts.insert(each, self.contacts[each])

    def delete_contact(self, name):
        for each in self.contacts:
            if name == each.get_contact_name():
                self.contacts.remove(each)

    def view_all_contact(self):
        for each in self.contacts:
            print(each)