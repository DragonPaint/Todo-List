import json

users = None
user_list = None


def todo_user():
    print("")

    try:
        with open("users.json", "r") as file:
            users = json.load(file)
    except FileNotFoundError:
        users = {
        }

    user_current = input("What is your user name?")
    if user_current.lower() in users:
        users[user_current.lower()]()
    else:
        todo_new_user(user_current)

    try:
        with open(users[user_current], "r") as file:
            user_list = json.load(file)
    except FileNotFoundError:
        user_list = {
        }
    todo_list(user_list, user_current)


def todo_new_user(user_current):
    correct = input("Is" + user_current + "a new user? If not press: n and then enter.")
    if correct.lower() == "n":
        print("Try again")
        todo_user()
    else:
        user_current_file = user_current + ".json"
        users[user_current] = user_current_file
        with open('users.json', 'w') as outfile:
            json.dump(users, outfile)


def user_list_add(user_list, user_current):
    user_add = input("What do you want to add " + user_current + "? Or type: exit = ")
    if user_add.lower() != "exit":

    else:
        todo_options(user_list, user_current)


def user_list_remove(user_list, user_current):
    user_add = input("What do you want to add " + user_current + "? Or type: exit = ")
    if user_add.lower() != "exit":

    else:
        todo_options(user_list, user_current)


def user_list_modify(user_list, user_current):
    user_add = input("What do you want to add " + user_current + "? Or type: exit = ")
    if user_add.lower() != "exit":

    else:
        todo_options(user_list, user_current)


def user_list_changeuser(user_list, user_current):
    todo_user()


def todo_list(user_list, user_current):
    with open(users[user_current], 'w') as outfile:
        json.dump(user_list, outfile)
    user_list_print = None
    nbr = 0
    for z in user_list:
        nbr += 1
        user_list_print += '%s. %s,\n' % nbr % z
    print("This is " + user_current + "'s current Todo list:")
    print(user_list_print)
    todo_options(user_list, user_current)


user_program_dict = {
    "add": user_list_add,
    "remove": user_list_remove,
    "modify": user_list_modify,
    "changeuser": user_list_changeuser,
}


def todo_options(user_list, user_current):
    user_option = input("Do you want to?: Add, Remove, Modify, Changeuser, Exit").lower()
    if user_option in user_program_dict:
        user_program_dict[user_option](user_list, user_current)
    else:
        print("Ops, something went wrong. I shall send you back")
        todo_options(user_list,user_current)


def launcher():
    print("To Do list, by DragonPainter.")
    todo_user()


launcher()