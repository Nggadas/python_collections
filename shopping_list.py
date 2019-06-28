import os

shopping_list = []
message = ""


def welcome_message():
    return "*" * 10 + " Welcome to the Shopping List " + "*" * 10


def show_help():
    return """Enter any item to add to the list
Type 'HELP' to see this instruction again 
Type 'DONE' when You're finished
To remove an item from the list, type 'DEL: ' and the item you want to remove."""


def add_item(text):
    shopping_list.append(text.capitalize())


def clear_screen():
    # run "cls" if on windows or "clear" if on mac or linux
    os.system("cls" if os.name == "nt" else "clear")


def show_list():
    if shopping_list:
        clear_screen()
        print(welcome_message())
        print(show_help())
        print("-" * 40)
        print("You have {} item(s) in the shopping list:".format(len(shopping_list)))
        for item in shopping_list:
            print("* " + item)


def remove(item):
    item_to_delete = item.split(": ")
    item_to_delete = item_to_delete[1].capitalize()
    if item_to_delete in shopping_list:
        shopping_list.remove(item_to_delete)


print(welcome_message())
print(show_help())

while True:
    show_list()

    if message:
        print(message)
        message = ""

    new_item = input("> ")

    if new_item.lower() == "done":
        print("Thank you for using the Shopping List App!")
        break
    elif new_item.lower() == "help":
        message = show_help()
    elif "del: " in new_item.lower():
        remove(new_item)
        clear_screen()
        print(show_help())
    elif new_item.lower() != "":
        if new_item.capitalize() in shopping_list:
            message = "You've already added '{}' to the shopping list.".format(new_item.capitalize())
        else:
            add_item(new_item)
    else:
        continue



























