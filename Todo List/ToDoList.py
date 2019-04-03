import json

users = {}
user_list = None


def todo_user():
    print("")

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {
        }

    user_current = input("What is your user name? ")
    if user_current not in users:
        todo_new_user(users, user_current)

    try:
        with open(users[user_current], "r") as file:
            user_list = json.load(file)
    except FileNotFoundError:
        user_list = {
        }
    todo_list(user_list, user_current, users)


def todo_new_user(users, user_current):
    correct = input("Is " + user_current + " a new user? If not press: n and then enter.")
    if correct.lower() == "n":
        print("Try again")
        todo_user()
    else:
        user_current_file = user_current + ".json"
        users[user_current] = user_current_file
        with open('users.json', 'w') as outfile:
            json.dump(users, outfile)
        ##user_list = {}
        ##with open(users[user_current], 'w') as outfile:
        ##    json.dump(user_list, outfile)


def user_list_add(user_list, user_current, users):
    user_add_note = input("What do you want to add " + user_current + "? Or type: exit = ")
    keys_list = user_list.keys()
    user_add_number_print = ""
    for key in keys_list:
        user_add_number_print += "%s, " % key
    user_add_number = input("Input an id for your note, it will not be sorted in order. \nAlready used id;s include: " + user_add_number_print)
    if user_add_note.lower() != "exit":
        user_list[user_add_number] = user_add_note
        todo_list(user_list, user_current, users)
    else:
        todo_options(user_list, user_current)


def user_list_remove(user_list, user_current, users):
    user_remove = input(user_current +" what id do you want to delete? Or type: exit = ")
    if user_remove.lower() != "exit":
        if user_remove in user_list:
            del user_list[user_remove]
        todo_list(user_list, user_current, users)
    else:
        todo_options(user_list, user_current, users)


def user_list_modify(user_list, user_current, users):
    user_modify = input("Witch id do you want to modify " + user_current + "? Or type: exit = ")
    if user_modify.lower() != "exit":
        if user_modify in user_list:
            user_modify_modification = input("What do you want to replace : " + user_list[user_modify] + " with? ")
            user_list[user_modify] = user_modify_modification
            todo_list(user_list, user_current, users)
        else:
            user_list_modify(user_list, user_current, users)
    else:
        todo_options(user_list, user_current, users)


def user_list_changeuser(user_list, user_current, users):
    print(user_current + " Logged out...")
    todo_user()


def todo_list(user_list, user_current, users):
    user_list_print = ""
    with open(users[user_current], 'w') as outfile:
        json.dump(user_list, outfile)

    for z in user_list:
        user_list_print += "%s: %s,\n" % (z, user_list[z])
    print("This is " + user_current + "'s current Todo list:")
    print(user_list_print)
    todo_options(user_list, user_current, users)


user_program_dict = {
    "add": user_list_add,
    "remove": user_list_remove,
    "modify": user_list_modify,
    "changeuser": user_list_changeuser,
}


def todo_options(user_list, user_current, users):
    user_option = input("Do you want to?: Add, Remove, Modify, Changeuser, Exit ").lower()
    if user_option in user_program_dict:
        user_program_dict[user_option](user_list, user_current,users)
    elif user_option == "exit":
        exit()
    else:
        print("Ops, something went wrong. I shall send you back")
        todo_options(user_list, user_current, users)


def launcher():
    print("To Do list, by DragonPainter.")
    todo_user()


launcher()