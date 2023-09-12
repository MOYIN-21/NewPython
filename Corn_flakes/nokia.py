def main_menu():
    print("""Menu
          1. Phonebook
          2. Messages
          3. Chat
          4. Call register
          5. Tones
          6. Settings
          7. Call divert
          8. Games
          9. Calculator
          10. Reminder
          11. Clock
          12. Profiles
          13. SIM services""")

    user = input("Enter a number: ")
    if user == "1":
        phonebook()
    elif user == "2":
        message()
    elif user == "3":
        chat()
    elif user == "4":
        call_register()
    elif user == "5":
        tones()
    elif user == "6":
        settings()
    elif user == "7":
        call_divert()
    elif user == "8":
        games()
    elif user == "9":
        calculator()
    elif user == "10":
        remainder()
    elif user == "11":
        clock()
    elif user == "12":
        profile()
    else:
        return main_menu()


def phonebook():
    print("""Phonebook
          1. Search
          2. Service Nos.1
          3. Add name
          4. Erase
          5. Edit
          6. Assign tone
          7. Send b’card
          8. Options
          9. Speed
          10. Voice tags
          11. Back""")
    user = input("Enter a number: ")
    if user == "1":
        search()
    if user == "2":
        service_nos()
    if user == "3":
        add_name()
    if user == "4":
        erase()
    if user == "5":
        edit()
    if user == "6":
        assign_tone()
    if user == "7":
        Send_b_card()
    if user == "8":
        options()
    if user == "9":
        speed_dials()
    if user == "10":
        voice_tags()
    if user == "11":
        main_menu()
    else:
        main_menu()


def search():
    print("No contact available yet")
    user = input("Enter 0 to phonebook or 1 to go back to main_menu: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        main_menu()


def service_nos():
    print("service center")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()


def add_name():
    print("Empty")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()


def erase():
    print("phone_book is Empty")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()


def edit():
    print("Empty")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()


def assign_tone():
    print("Empty")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()

def Send_b_card():
    print(":(")
    user = input("Enter 1 to main_menu and 0 to phonebook: ")
    if user == "0":
        phonebook()
    if user == "1":
        main_menu()
    else:
        print("invalid input")
        phonebook()


def options():
    print("""1. Type of view        
          2. Memory status""")
    user = input("Enter any number: ")
    if user == "1":
        type_of_view()
    if user == "2":
        memory_status()
    else:
        main_menu()


def type_of_view():
    print("Empty")
    user = input("Enter 0 to : ")
    if user == 0:
        main_menu()
    else:
        main_menu()


def memory_status():
    print("no status recorded yet")
    user = input("Enter any number: ")
    if user == 0:
        main_menu()
    else:
        main_menu()


def speed_dials():
    print("speed dial")
    user = input("Enter any number: ")
    if user == "1":
        phonebook()
    else:
        phonebook()


def voice_tags():
    print("voice tag")
    user = input("Enter o to phonebook or 1 to main menu: ")
    if user == "1":
        phonebook()
    else:
        main_menu()


def message():
    print("""1. Write messages
          2. Inbox
          3. Outbox
          4. Picture messages
          5. Templates
          6. Smileys
          7. Message settings
          8. Info service
          9. Voice mailbox
          10. Service command editor
          11. Back""")
    user = int(input("Enter a number: "))
    if user == 1:
        write_message()
    elif user == 2:
        inbox()
    elif user == 3:
        outbox()
    elif user == 4:
        picture_message()
    elif user == 5:
        templates()
    elif user == 6:
        smileys()
    elif user == 7:
        message_settings()
    elif user == 8:
        info_service()
    elif user == 9:
        voice_mailbox()
    elif user == 10:
        service_command_editor()
    elif user == 11:
        message()
    else:
        print("invalid input")
        main_menu()


def write_message():
    print("Type and send message to contacts")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def inbox():
    print("no new message")
    user = input("Enter 0 to message: ")
    if user == "0":
        message()
    else:
        print("Invalid input")
        main_menu()


def outbox():
    print("outbox")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        main_menu()


def picture_message():
    print(":(")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def templates():
    print("template")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def smileys():
    print(":),(:")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def message_settings():
    print("""1. Set
          \n2. Common""")
    user = input("Enter no a number: ")
    if user == "1":
        print("""1. message centered number"
              2. message sent as"
              3. message validating""")
        user = input("Enter a number: ")
        if user == 1:
            print("message center")
        if user == 2:
            print("Your message is successfully sent")
            message()
    if user == "2":
        print(""" 1. Delivery report, 
                  2. reply via same centre
                  3. Character support""")
        user = int(input("Enter a number: "))
        if user == 1:
            delivery_report()
        if user == 2:
            reply_via_same_centre()
        if user == 3:
            character_support()
        else:
            print("invalid input")
            message()


def delivery_report():
    print("message delivered")
    user = input("Enter 0 to message")
    if user == "0":
        message()
    else:
        main_menu()


def reply_via_same_centre():
    print("No reply")
    user = input("Enter o to return to outbox: ")
    if user == "o":
        message()
    else:
        main_menu()


def character_support():
    print("your message support character")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        main_menu()


def info_service():
    print("YAY!!!,successfully sent message")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def voice_mailbox():
    print("welcome to voice_mailbox")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def service_command_editor():
    print("command editor")
    user = input("Enter 0 to go back: ")
    if user == "0":
        message()
    else:
        print("invalid input")
        main_menu()


def chat():
    print("chat")
    user = input("Enter 1 to go back: ")
    if user == "1":
        phonebook()
    else:
        main_menu()


def call_register():
    print("""1. Missed calls
            2. Received calls 
            3. Dialled numbers 
            4. Erase recent call lists
            5. Show call duration
            6. Show call cost
            7. Call cost settings 
            8. Prepaid credit""")
    user = input("Enter a number: ")
    if user == "1":
        print("43 Missed calls")
    if user == "2":
        print("Received call")
    if user == "3":
        print("Dialled number")
    if user == "4":
        print("Erase recent call lists")
    if user == "5":
        show_call_duration()
    if user == "6":
        show_call_cost()
    if user == "7":
        call_cost_settings()
    if user == "8":
        print("prepaid credit")
    else:
        print("enter 1 to main menu/0 to message")
        if user == 1:
            call_register()
        if user == 0:
            phonebook()


def erase_recent_call_list():
    print("call list")
    call_register()


def show_call_duration():
    print("""1. Last call duration
            2. All calls’ duration
            3. Received calls’ duration
            4. Dialled calls’ duration
            5. Clear timers""")
    user = input("Enter a number: ")
    if user == "1":
        print("last call duration")
    if user == "2":
        print("all call duration")
    if user == "3":
        print("Empty")
    if user == "4":
        print("Empty")
    if user == "5":
        print("Empty")
    else:
        call_register()


def show_call_cost():
    print("""1. Last call cost
         2. All calls’ cost
         3. Clear counters""")
    user = input("Enter a number and 0 to call register: ")
    if user == "0":
        call_register()
    if user == "1":
        print("Last call cost")
    if user == "2":
        print("All calls cost")
    if user == "3":
        print("Clear counter")
    else:
        main_menu()


def call_cost_settings():
    print("""1. Call cost limit
            2. Show costs in""")
    user = input("Enter a number and 0 to call register: ")
    if user == "1":
        print("call cost")
    if user == "2":
        print("Empty")
    if user == "0":
        call_register()
    else:
        main_menu()


def tones():
    print("""1. Ringing tone 
    2. Ringing volume 
    3. Incoming call alert
    4. Composer
    5. Message alert tone 
    6. Keypad tones
    7. Warning and game tones
    8. Vibrating alert
    9. Screen saver""")
    user = input("Enter a number and 10 to phonebook: ")
    if user == "1":
        print("Ringing tone")
    if user == "2":
        print("Ringing volume")
    if user == "3":
        print("incoming call alert")
    if user == "4":
        print("Composer")
    if user == "5":
        print("Message alart tone")
    if user == "6":
        print("Keypad tones")
    if user == "7":
        print("Warning and game tones")
    if user == "8":
        print("Vibrating alert")
    if user == "9":
        print("Screen Saver")
    if user == "10":
        phonebook()
    else:
        user = int(input("Enter 0 to main-menu and 1 phonebook: "))
        if user == 1:
            phonebook()
        if user == 0:
            main_menu()


def settings():
    print("""1.Call settings
    2.Phone settings
    3.Security settings
    4.Restore factory settings""")
    user = input("Enter a number and 0 to main menu: ")
    if user == "1":
        print("""1. Automatic redial
                2. Speed dialling
                3. Call waiting options
                4. Own number sending
                5. Phone line in use
                6. Automatic answer""")
        if user == "1":
            print("Automatic radial")
        if user == "2":
            print("Speed dialling")
        if user == "3":
            print("Call waiting option")
        if user == "4":
            print("Own number sending")
        if user == "5":
            print("Phone line in use")
        if user == "6":
            print("Automatic answer")
        if user == "0":
            main_menu()
        else:
            main_menu()
    elif user == "2":
        print("""1. Language
         2. Cell info display
         3. Welcome note
         4. Network selection
         5. Lights2
         6. Confirm SIM service actions""")
        user = input("Enter any number and 0 to settings: ")
        if user == "1":
            print("Yoruba, English, Hausa, Chinese")
        if user == "2":
            print("Cell info display")
        if user == "3":
            print("Welcome note")
        if user == "4":
            print("Network selection")
        if user == "5":
            print("Empty")
        if user == "6":
            print("Confirm SIM service actions")
        if user == "0":
            settings()
        else:
            phonebook()
    elif user == "3":
        print("""1. PIN code request
                 2. Call barring service
                 3. Fixed dialling
                 4. Closed user group
                 5. Phone security
                 6. Change access codes""")
        user = input("Enter a number and 0 to settings: ")
        if user == "0":
            settings()
        if user == "1":
            print("Empty")
        if user == "2":
            print("Fixed dialling")
        if user == "3":
            print("Fixed dialling")
        if user == "4":
            print("Closed user group")
        if user == "5":
            print("Change access codes")
        else:
            main_menu()


def call_divert():
    print("""1. Call cost limit
            2. Show costs in""")
    user = input("Enter a number: ")
    if user == "1":
        phonebook()
    else:
        settings()


def games():
    print(":(, not available yet")
    main_menu()


def calculator():
    print(":(, not available")
    phonebook()


def remainder():
    phonebook()


def clock():
    print("""1. Alarm clock
     2. Clock settings
     3. Date setting
     4. Stopwatch
     5. Countdown timer
     6. Auto update of date and time""")


def profile():
    print("Empty")
    user_input = int(input("Enter number 0 to main menu: "))
    if user_input == "0":
        phonebook()
    else:
        main_menu()


def services():
    print("EMPTY!!!")
    user_input = int(input("Enter number 0 to main menu or 1 to phonebook: "))
    if user_input == 0:
        main_menu()
    else:
        phonebook()

services()

main_menu()