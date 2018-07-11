# Adventure Game Erin_Miller

import random

print("Last night, you went to sleep in your own home.")
print("Now, you wake up in a locked room.")
print("Could there be a key hidden somewhere?")
print("In the room, you can see:")

# The menu Function:


def menu(list, question):
    for item in list:
            print(1 + list.index(item), item)
    return int(input(question))


items = ["backpack", "painting", "vase", "bowl", "door"]


# This is the list of items in the room:


key_location = random.randint(1, 4)

# the key is not found.

key_found = "No"
loop = 1

# Display the menu until the key is found:

while loop == 1:
    choice = menu(items, "What do you want to inspect?")

    print("")

    if choice < 5:
        if choice == key_location:
            print("You found a small key in the", items[choice-1])
            key_found = "Yes"

        else:
            print("You found nothing in the", items[choice-1])

    elif choice == 5:
        if key_found == "Yes":
            loop = 0
            print(" You insert the key in the keyhole and turn it.")
        else:
            print("The door is locked. You need to find the key.")

    else:
        print("Choose a number less than 6.")


print("You open the door to a long corridor.")
print("You creep down the long corridor and tiptoe down the stairs.")
print("The stairs lead to a living room.")
print("You see the following:")


def menu2(list, question):
    for item in list:
            print(1 + list.index(item), item)
    return int(input(question))


items = ["fireplace", "window", "bookcase", "closet", "door"]

key_location = random.randint(1, 4)
key_found = "No"
loop = 1

while loop == 1:
    choice = menu(items, "What do you want to inspect?")
    if choice < 5:
        if choice == key_location:
            print("You found a small key in the", items[choice-1])
            key_found = "Yes"

        else:
            print("You found nothing in the", items[choice-1])

    elif choice == 5:
        if key_found == "Yes":
            loop = 0
            print(" You insert the key in the keyhole and turn it.")
        else:
            print("The door is locked. You need to find the key.")

    else:
        print("Choose a number less than 6.")

print("You exit the house before anyone came home. You breathe a sigh of relief.")
