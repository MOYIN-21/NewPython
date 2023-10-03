import pickle

from my_class.phone_book.phoneBook import phonebook

my_new_contact = phonebook()


def create_contact_in():
    first_name = input("Enter First Name")
    last_name = input("Enter last Name")
    phone_number = input("Enter Phone Number")
    email_address = input("Enter Email Address")

    my_new_contact.create_contact(first_name, last_name, phone_number, email_address)
    print("Contact created successfully")
    go_to_main_menu()


def view_contact_in():
    first_name = input("Enter First Name")
    last_name = input("Enter First Name")
    print("Hi, here is your entry")
    print(my_new_contact.view_contact(first_name + " " + last_name))
    go_to_main_menu()


def edit_contact():
    initial_first_name = input("Enter Initial First Name")
    initial_last_name = input("Enter Initial last Name")
    first_name = input("Enter First Name")
    last_name = input("Enter First Name")
    phone_number = input("Enter Phone Number")
    email_address = input("Enter Email Address")
    my_new_contact.edit_contact(initial_first_name + " " + initial_last_name, first_name,
                                last_name, phone_number, email_address)
    print("Contact Updated")

    go_to_main_menu()


def count_contact():
    numberOfContacts = my_new_contact.count_contact()
    print("You have", numberOfContacts, "numbers of Contacts in your phonebook")
    go_to_main_menu()


def delete_contact_in():
    first_name = input("Enter First Name")
    last_name = input("Enter First Name")
    my_new_contact.delete_contact(first_name + " " + last_name)
    print("Contact deleted successfully")
    go_to_main_menu()


def view_all_contact_in_phonebook():
    my_new_contact.view_all_contact()
    go_to_main_menu()


def exit_application():
    save_file()


def save_file():
    print("Thank you for using our application ")
    with open("contacts.pkl", 'wb') as phonebook_file:
        pickle.dump(my_new_contact, phonebook_file)
        phonebook_file.close()


def go_to_main_menu():
    mainMenu = int(input("""
                    ===================================
                    So good to be here, How are you today?
                    1 -> Create Contact
                    2 -> View Contact
                    3 -> Edit Contact
                    4 -> Count Contact
                    5 -> Delete Contact
                    6 -> View All Contact
                    7 -> Exit"
                     ===================================
                    """))

    match mainMenu:
        case 1:
            create_contact_in()

        case 2:
            view_contact_in()

        case 3:
            edit_contact()

        case 4:
            count_contact()

        case 5:
            delete_contact_in()

        case 6:
            view_all_contact_in_phonebook()

        case 7:
            exit_application()

        case other:
            go_to_main_menu()


if __name__ == '__main__':
    try:
        with open("contacts.pkl", 'rb') as phonebook_file:
            my_new_contact = pickle.load(phonebook_file)
    except:
        print("Reloading...")

    go_to_main_menu()