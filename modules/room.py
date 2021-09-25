class Room():

    number_of_rooms = 0


    @staticmethod
    def static_method():
        print("nothing")


    @classmethod
    def class_method(cls):
        print(cls)


    def __init__(self, room_name, room_description = None):
        self.name = room_name
        self.description = room_description
        self.linked_rooms = {}
        self.items = []
        self.character = None

        Room.number_of_rooms = Room.number_of_rooms + 1


    def set_description(self, room_description):
        self.description = room_description


    def get_description(self):
        if self.description is not None:
            return self.description


    def describe(self):
        print(self.description)


    def set_name(self, room_name):
        self.name = room_name


    def get_name(self):
        return self.name


    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name + " linked rooms :" + repr(self.linked_rooms))


    def get_details(self):
        print("\nYou are in the " + self.name + ". " + self.description + ".")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room + " is " + direction)

        if self.items:
            print("\nYou see following items -> ")
            for item in self.items:
                print(item.get_name() + " - " + item.get_description())
        else:
            print("There are no items of interest in this room.")

        inhabitant = self.get_character()
        if inhabitant is not None:
            inhabitant.describe()


    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self


    def add_item(self, item):
        self.items.append(item)


    def take_item(self):
        if self.items is not None:
            return self.items.pop()


    def set_character(self, character):
        self.character = character


    def get_character(self):
        return self.character
