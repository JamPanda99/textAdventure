class Location:
    #Name - string | destinations - list of Location() instances | items - list of Item() instances | requirements - dictionary of boolians
    def __init__(self, newName, newDestinations, newRequirements):
        self.name = newName
        self.destinations = newDestinations
        self.requirments = newRequirements

    def addDestination(self, newDestination):
        self.destinations.append(newDestination)

    def setRequirement(self, reqName, status):
        if reqName in self.requirments:
            self.requirments[reqName] = status


class Item:
    def __init__(self, newName):
        self.name = newName

class Message(Item):
    def __init__(self, newName, newMessage):
        Item.__init__(self, newName)
        self.message = newMessage
    
    def outputMessage(self):
        print(self.message)

map = []

map.append(Location(
    'prison cell',
    [],
    {
        'null' : True
    }
))


print(map[0].requirments)
map[0].setRequirement('null', False)
print(map[0].requirments)

print('----')

devLetter = Message(
    'letter',
    'hello'
)

devLetter.outputMessage()
print(devLetter.name)  