import json


def todo_user():
    print("")
    # Adds an space between text

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {
        }
    # Loads the users file, if it does not exist it makes a new users dictionary

    user_current = input("What is your user name? ")
    # current username

    user_current_encoding_array = [17, 5, 15, 8, 3, 7, 3, 3, 10, 20, 3, 5, 11, 12, 23, 24, 20]
    # It creates an array to encrypt the username so you can't read it out from the users.json file
    if len(user_current_encoding_array) <= len(user_current):
        diff = len(user_current) - len(user_current_encoding_array)
        user_current_encoding_array = (user_current_encoding_array * int(
            diff / len(user_current_encoding_array)) + 2 * user_current_encoding_array)
        # The whole if statement makes sure that the user_current_encoding_array is longer than the username in user_current
    user_current_encoded = todo_encode(user_current, user_current_encoding_array)
    # sends the username along for encryption
    if user_current_encoded not in users:
        # Checks if the encoded username is a new username
        todo_new_user(users, user_current, user_current_encoded)
        # Adds a new user using the encrypted name

    try:
        with open(users[user_current_encoded], "r") as file:
            user_list = json.load(file)
    except FileNotFoundError:
        user_list = {
        }
    # Loads the user to do list file, if it does not exist it makes a new user to do list file dictionary
    todo_list(user_list, user_current, users, user_current_encoded)
    # Starts the to do list


def todo_new_user(users, user_current, user_current_encoded):
    correct = input("Is " + user_current + " a new user? If not press: n and then enter.")
    # Double checks if you wrote the correct username if it is not in the users dictionary
    if correct.lower() == "n":
        print("Try again")
        todo_user()
        # Pressing n and then enter it sends you back to the user "log in" method to correct your username
    else:
        user_current_file = user_current_encoded + ".json"
        # Creates a string to open the proper user.json file
        users[user_current_encoded] = user_current_file
        # Updates the users dictionary
        with open('users.json', 'w') as outfile:
            json.dump(users, outfile)
        # Updates the users.json


def todo_encode(user_current, user_current_encoding_array):
    user_current_encoded = ""
    # clears user_current_encoded
    abc_itteration = 0
    user_current_encoding = ["ijk"]
    # Opens user_current_encoding
    for letters in user_current:
        if 96 <= ord(letters) <= 123:
            ascii_numbers = ord(letters)
            ascii_numbers += user_current_encoding_array[abc_itteration]
            if ascii_numbers >= 123:
                ascii_numbers -= 26
            user_current_encoding.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            ascii_numbers = ord(letters)
            ascii_numbers += user_current_encoding_array[abc_itteration]
            if ascii_numbers >= 91:
                ascii_numbers -= 26
                # Checks if the ascii characters
            user_current_encoding.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95:
            user_current_encoding.append(" ")
            # Underscore = blankspace
        else:
            user_current_encoding.append(letters)
            # Checks if every letter is either normal, capital, underscore or else and inputs the result from the calculation in user_current_encoding
        abc_itteration += 1

    for converter in user_current_encoding:
        user_current_encoded += '%s' % converter

    user_current_encoding.clear()
    return user_current_encoded


def user_list_add(user_list, user_current, users, user_current_encoded):
    user_add_note = input("What do you want to add " + user_current + "? Or type: exit = ")
    keys_list = user_list.keys()
    user_add_number_print = ""
    for key in keys_list:
        user_add_number_print += "%s, " % key
    print("Input an id for your note, it will not be sorted in order.")
    user_add_number = input("Already used id;s include: " + user_add_number_print)
    if user_add_note.lower() != "exit":
        user_list[user_add_number] = user_add_note
        todo_list(user_list, user_current, users, user_current_encoded)
    else:
        todo_options(user_list, user_current, user_current_encoded)


def user_list_remove(user_list, user_current, users, user_current_encoded):
    user_remove = input(user_current + " what id do you want to delete? Or type: exit = ")
    if user_remove.lower() != "exit":
        if user_remove in user_list:
            del user_list[user_remove]
        todo_list(user_list, user_current, users, user_current_encoded)
    else:
        todo_options(user_list, user_current, users, user_current_encoded)


def user_list_modify(user_list, user_current, users, user_current_encoded):
    user_modify = input("Witch id do you want to modify " + user_current + "? Or type: exit = ")
    if user_modify.lower() != "exit":
        if user_modify in user_list:
            user_modify_modification = input("What do you want to replace : " + user_list[user_modify] + " with? ")
            user_list[user_modify] = user_modify_modification
            todo_list(user_list, user_current, users, user_current_encoded)
        else:
            user_list_modify(user_list, user_current, users, user_current_encoded)
    else:
        todo_options(user_list, user_current, users, user_current_encoded)


def user_list_changeuser(user_list, user_current, users, user_current_encoded):
    print(user_current + " Logged out...")
    todo_user()


def todo_list(user_list, user_current, users, user_current_encoded):
    print("")
    # Adds an space between text
    user_list_print = ""
    with open(users[user_current_encoded], 'w') as outfile:
        json.dump(user_list, outfile)

    for z in user_list:
        user_list_print += "%s: %s,\n" % (z, user_list[z])
    print("This is " + user_current + "'s current Todo list:")
    print(user_list_print)
    todo_options(user_list, user_current, users, user_current_encoded)


user_program_dict = {
    "add": user_list_add,
    "remove": user_list_remove,
    "modify": user_list_modify,
    "changeuser": user_list_changeuser,
}


def todo_options(user_list, user_current, users, user_current_encoded):
    user_option = input("Do you want to?: Add, Remove, Modify, Changeuser, Exit ").lower()
    if user_option in user_program_dict:
        user_program_dict[user_option](user_list, user_current, users, user_current_encoded)
    elif user_option == "exit":
        exit()
    else:
        print("Ops, something went wrong. I shall send you back")
        todo_options(user_list, user_current, users, user_current_encoded)


def launcher():
    print("To Do list, by DragonPainter.")
    todo_user()
    # Starts the program and sends you to user selection


launcher()
