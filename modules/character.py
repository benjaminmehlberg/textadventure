class Character():

    # Create a character
    def __init__(self, char_name, char_description, weakness = None):
        self.name = char_name
        self.description = char_description
        self.weakness = weakness
        self.conversation = None
        self.call = None

    # Describe this character
    def describe(self):
        print("\n" + self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item, inventory):
        print(self.name + " doesn't want to fight with you")
        return True

    def set_call(self, call):
        self.call = call

    def tell(self):
        if self.call is not None:
            print("[You tell " + self.name + "]: " + self.call)
        else:
            print(self.name + " ignores you.")

    def give(self, present, inventory):
        inv_list = [item.name for item in inventory]
        if present in inv_list and present == self.weakness:
            print(self.name + " really appreciates your gift.")
            return True
        else:
            print(self.name + " refuses to take your gift.")
            return False


class Enemy(Character):

    enemies_to_defeat = 0

    def __init__(self, char_name, char_description, weakness = None):
        super().__init__(char_name, char_description, weakness)
        self.weakness = weakness

        Enemy.enemies_to_defeat += 1


    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item, inventory):
        inv_list = [item.name for item in inventory]
        if combat_item in inv_list and combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False


class Friend(Character):

    def __init__(self, char_name, char_description, weakness = None):
        super().__init__(char_name, char_description, weakness)
        self.weakness = weakness


    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness