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
    abc_iteration = 0
    # A value that increses every time the for loop iterates to make user_current_encoding_array change value
    user_current_encoding = ["ijk"]
    # Opens user_current_encoding
    for letters in user_current:
        # letters becomes every letter in users_current one at a time every iteration of the for loop
        if 96 <= ord(letters) <= 123:
            # Checks if the ascii value is between 96 and 123 = a -> z
            ascii_numbers = ord(letters)
            # Makes ascii_numbers = the ascii value of the letter in letters
            ascii_numbers += user_current_encoding_array[abc_iteration]
            # Adds the current value of the user_current_encoding_array
            if ascii_numbers >= 123:
                ascii_numbers -= 26
                # Checks if the ascii values are higher than the highest value of 123 = z and then removes 26
            user_current_encoding.append(chr(int(ascii_numbers)))
        elif 64 <= ord(letters) <= 91:
            # Checks if the ascii value is between 64 and 91 = A -> Z
            ascii_numbers = ord(letters)
            # Makes ascii_numbers = the ascii value of the letter in letters
            ascii_numbers += user_current_encoding_array[abc_iteration]
            # Adds the current value of the user_current_encoding_array
            if ascii_numbers >= 91:
                ascii_numbers -= 26
                # Checks if the ascii values are higher than the highest value of 91 = Z and then removes 26
            user_current_encoding.append(chr(int(ascii_numbers)))
        elif ord(letters) == 95:
            user_current_encoding.append(" ")
            # Underscore = blank space and adds it to user_current_encoding
        else:
            user_current_encoding.append(letters)
            # Checks if every letter is either normal, capital, underscore or else and inputs the result from the calculation in user_current_encoding
        abc_iteration += 1
        # Iterates abc_iteration by adding +1 for each for loop

    for converter in user_current_encoding:
        user_current_encoded += '%s' % converter
    # Adds everything to user current_encoded so it is stored as a single string
    user_current_encoding.clear()
    return user_current_encoded


def user_list_add(user_list, user_current, users, user_current_encoded):
    user_add_note = input("Type out what you want to add " + user_current + " or type: exit = ")
    # Asks the user to input the note
    keys_list = user_list.keys()
    user_add_id_print = ""
    # Clears number_print
    for key in keys_list:
        user_add_id_print += "%s, " % key
    # Makes a nice list of all the id's in the users user_list
    print("Input an id for your note, it will not be sorted in order.")
    user_add_id = input("Already used id;s include: " + user_add_id_print)
    # Asks the user for an id and prints the already used id's
    if user_add_note.lower() != "exit":
        user_list[user_add_id] = user_add_note
        # Adds the note to user_list using the id
        todo_list(user_list, user_current, users, user_current_encoded)
        # Goes back to todo_list
    else:
        todo_options(user_list, user_current, user_current_encoded)
        # Goes back to todo_options if you choose to exit


def user_list_remove(user_list, user_current, users, user_current_encoded):
    user_remove = input(user_current + " what id do you want to delete or type: exit = ")
    if user_remove.lower() != "exit":
        if user_remove in user_list:
            del user_list[user_remove]
        todo_list(user_list, user_current, users, user_current_encoded)
        # Goes back to todo_list
    else:
        todo_options(user_list, user_current, users, user_current_encoded)
        # Goes back to todo_options if you choose to exit


def user_list_modify(user_list, user_current, users, user_current_encoded):
    user_modify = input("Witch id do you want to modify " + user_current + " or type: exit = ")
    if user_modify.lower() != "exit":
        if user_modify in user_list:
            user_modify_modification = input("What do you want to replace : " + user_list[user_modify] + " with? ")
            user_list[user_modify] = user_modify_modification
            todo_list(user_list, user_current, users, user_current_encoded)
            # Goes back to todo_list
        else:
            user_list_modify(user_list, user_current, users, user_current_encoded)
            # Restarts modify because the input id did not exist
    else:
        todo_options(user_list, user_current, users, user_current_encoded)
        # Goes back to todo_options if you choose to exit


def user_list_changeuser(user_list, user_current, users, user_current_encoded):
    print(user_current + " Logged out...")
    todo_user()


def todo_list(user_list, user_current, users, user_current_encoded):
    print("")
    # Adds an space between text
    user_list_print = ""
    with open(users[user_current_encoded], 'w') as outfile:
        json.dump(user_list, outfile)
    # Saves the current user list every time todo_list is launched to decrease the size of user_add/remove/modify
    for z in user_list:
        user_list_print += "%s: %s,\n" % (z, user_list[z])
    # Makes the user_list_print a list that adds the Id and the associating user_list note
    print("This is " + user_current + "'s current Todo list:")
    print(user_list_print)
    # Prints the user_list
    todo_options(user_list, user_current, users, user_current_encoded)
    # Launches the options menu


user_program_dict = {
    "add": user_list_add,
    "remove": user_list_remove,
    "modify": user_list_modify,
    "changeuser": user_list_changeuser,
}


def todo_options(user_list, user_current, users, user_current_encoded):
    user_option = input("Do you want to?: Add, Remove, Modify, Changeuser, Exit ").lower()
    # .lower() makes all the input characters lower case to make sure it works with lower and upper case characters
    if user_option in user_program_dict:
        # Checks if the user input was the same as any item in the user program dictionary
        user_program_dict[user_option](user_list, user_current, users, user_current_encoded)
        # Starts the program that was selected
    elif user_option == "exit":
        exit()
        # turns the program off
    else:
        print("Ops, something went wrong. I shall send you back")
        todo_options(user_list, user_current, users, user_current_encoded)
        # if the input does not match any option then it relaunches the method todo_options


def launcher():
    print("To Do list, by DragonPainter.")
    todo_user()
    # Starts the program and sends you to user selection


launcher()
