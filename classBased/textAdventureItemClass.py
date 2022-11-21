class Item:
    def __init__(self, newName, newDesc, newCommandIDs):
        self.name = newName
        self.description = newDesc
        self.commandIDs = newCommandIDs
    
    def getName(self):
        return self.name

    def getCommandIDs(self):
        return self.commandIDs

class Message(Item):
    def __init__(self, newName, newDesc, newCommandIDs, newMessage):
        Item.__init__(self, newName, newDesc, newCommandIDs)
        self.message = newMessage
    
    def outputMessage(self):
        print(self.message)

class functionRunnerItem(Item):
    def __init__(self, newName, newDesc, newCommandIDs, newFunc):
        Item.__init__(self, newName, newDesc, newCommandIDs)
        self.function = newFunc

    def activateItem(self, stats):
        self.function(stats)