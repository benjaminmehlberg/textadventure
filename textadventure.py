#!/usr/bin/env python3
"""
A simple text adventure. Main program
"""
import sys
import dungeon
from modules import Room, Character, Enemy, Friend, Item, RPGInfo


def show_inventory(inventory):

    print("\n" + "<-- Your inventory -->".center(30))
    if inventory == []:
        print("<Empty>".center(30))
    else:
        [print(item.name.center(30)) for item in inventory]
    print("<-------------------->".center(30))
    print("\n")


# Initialize rooms, items, characters
current_room = dungeon.init()
inventory = ()
print(f"There are {Room.number_of_rooms} rooms to explore")

# Main loop
while True:
    print(current_room.name, current_room.linked_rooms)
    current_room.get_details()
    show_inventory(inventory)

    command = input("north/south/west/east/talk/fight/take/give\n> ")

    # Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if current_room.character is not None:
            current_room.character.talk()
    elif command == "fight":
        print("What will you fight with?")
        fight_with = input().title()
        result = current_room.character.fight(fight_with, inventory)
        if result == True:
            Enemy.enemies_to_defeat -= 1
            current_room.character = None
            if Enemy.enemies_to_defeat <= 0:
                print("You won the game!")
                break
        else:
            print("Better luck next time.")
            break
    elif command == "take":
        inventory.append(current_room.take_item())
        # show_inventory(inventory)
    elif command == "give":
        if current_room.character is None:
            print("No one's here except you!")
            continue
        elif isinstance(current_room.character, (Friend, Character)):
            print("What do you want to give?")
            present = input().title()
            result = current_room.character.give(present, inventory)
            if result == True:
                current_room.character = None
            else:
                desc = current_room.character.name + " hates you now."
                current_room.character = Enemy(
                    current_room.character.name, desc, current_room.character.weakness
                )
        else:
            print(current_room.character, " doesn't want a present from you.")
    else:
        choice = input("Do you really want to exit (y/n)> ").lower()
        if choice != "y":
            continue
        else:
            sys.exit(0)
