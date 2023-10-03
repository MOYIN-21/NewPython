class contact:
    def __init__(self, contact_name, phone_number, email_address):
        self.contact_name = contact_name
        self.phone_number = phone_number
        self.email_address = email_address

    def set_contact_name(self, name):
        self.contact_name = name

    def get_contact_name(self):
        return self.contact_name

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number

    def set_email_address(self, email_address):
        self.email_address = email_address

    def get_email_address(self):
        return self.email_address

    def __str__(self):
        return f"""
       Contact Name: {self.contact_name}
       Contact Phone Number: {self.phone_number}
       Contact Email-Address: {self.email_address}
       """