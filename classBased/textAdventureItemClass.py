class Item:
    def __init__(self, newName):
        self.name = newName

class Message(Item):
    def __init__(self, newName, newMessage):
        Item.__init__(self, newName)
        self.message = newMessage
    
    def outputMessage(self):
        print(self.message)