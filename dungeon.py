"""
Dungeon setup file
"""
from modules import Room, Enemy, Friend, Item, RPGInfo

def init():

    room_objects = {}
    room_data = {
        "Kitchen": {
            "description": "A dank and dirty room buzzing with flies"
            ,
            "links": {"Dining Hall": "south"}
        },
        "Ballroom": {
            "description": ("A vast room with a shiny wooden floor; huge "
            "candlesticks guard the entrance")
            ,
            "links": {"Dining Hall": "east"}
        },
        "Dining Hall": {
            "description": ("A large room with ornate golden decorations "
            "on each wall")
            ,
            "links": {"Kitchen": "north", "Ballroom": "west"}
        }
    }
    # For every room, generate a Room object and apply data from room_data
    # dictionary
    for key in room_data.keys():
        room_objects[key] = Room(key)
        room_objects[key].set_description(room_data[key]["description"])
        # For every room, check for links with other rooms and apply
        for room in room_data.keys():
            if room in room_data[key]["links"].keys():
                room_objects[key].link_room(room, room_data[key]["links"][room])

    # Items setup
    cheese = Item("Cheese")
    candle = Item("Candleabre")
    sword = Item("Sword Of Vengeance")
    ring = Item("Ring Of Ultimate Power")

    cheese.set_description("Glibberish; Smells like old socks")
    candle.set_description("A massive device with six candles")
    sword.set_description("A mighty blade of dark metal")
    ring.set_description("A heavy ring with a blue glowing jewel")

    room_objects["Kitchen"].add_item(cheese)
    room_objects["Kitchen"].add_item(candle)
    room_objects["Dining Hall"].add_item(ring)
    room_objects["Ballroom"].add_item(sword)

    # Enemy/NPC setup
    dave = Enemy("Dave", "A smelly zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("Cheese")

    sarah = Friend("Sarah", "The farmers' lost daughter")
    sarah.set_conversation("Please, can you help me escape? It's so dark in "
                           "this place.")
    sarah.set_weakness("Candleabre")

    room_objects["Ballroom"].set_character(sarah)
    room_objects["Dining Hall"].set_character(dave)
    
    # Game setup
    my_game = RPGInfo("Mini Dungeon")
    my_game.welcome()
    RPGInfo.info()

    RPGInfo.author = "BM"
    RPGInfo.credits()

    return room_objects["Kitchen"]
