"""
Dungeon setup file
"""
import time
from modules import Room, Character, Enemy, Friend, Item, RPGInfo

def init():

    o_rooms = {}
    d_rooms = {
    "Kitchen": 
        {
            "description": "A dank and dirty room buzzing with flies"
        ,
            "links": {"Dining Hall": "south"}
        },
    "Ballroom":
        {
            "description": "A vast room with a shiny wooden floor; huge candlesticks guard the entrance"    
        ,
            "links": {"Dining Hall": "east"}
        }
        ,
    "Dining Hall":
        {
            "description": "A large room with ornate golden decorations on each wall"
        ,
            "links": {"Kitchen": "north", "Ballroom": "west"}
        }
    }
    for key in d_rooms.keys():
        o_rooms[key] = Room(key)
        o_rooms[key].set_description(d_rooms[key]["description"])
        [o_rooms[key].link_room(room, d_rooms[key]["links"][room]) for room in d_rooms.keys() if room in d_rooms[key]["links"].keys()]
    """    
    # Rooms setup
    kitchen = Room("Kitchen")
    ballroom = Room("Ballroom")
    dining_hall = Room("Dining Hall")

    kitchen.set_description("A dank and dirty room buzzing with flies")
    ballroom.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")
    dining_hall.set_description("A large room with ornate golden decorations on each wall")

    kitchen.link_room(dining_hall, "south")
    ballroom.link_room(dining_hall, "east")
    dining_hall.link_room(kitchen, "north")
    dining_hall.link_room(ballroom, "west")
    
    # Items setup
    cheese = Item("Cheese")
    candle = Item("Candleabre")
    sword = Item("Sword Of Vengeance")
    ring = Item("Ring Of Ultimate Power")

    cheese.set_description("Glibberish; Smells like old socks")
    candle.set_description("A massive device with six candles")
    sword.set_description("A mighty blade of dark metal")
    ring.set_description("A heavy ring with a blue glowing jewel")

    kitchen.add_item(cheese)
    kitchen.add_item(candle)
    dining_hall.add_item(ring)
    ballroom.add_item(sword)

    # Enemy setup
    dave = Enemy("Dave", "A smelly zombie")
    dave.set_conversation("Brrlgrh... rgrhl... brains...")
    dave.set_weakness("Cheese")

    sarah = Friend("Sarah", "The farmers' lost daughter")
    sarah.set_conversation("Please, can you help me escape? It's so dark in this place.")
    sarah.set_weakness("Candleabre")

    ballroom.set_character(sarah)
    dining_hall.set_character(dave)
    """
    # Game setup
    my_game = RPGInfo("Mini Dungeon")
    my_game.welcome()
    RPGInfo.info()

    RPGInfo.author = "Skeletor"
    RPGInfo.credits()

    return o_rooms["Kitchen"]
