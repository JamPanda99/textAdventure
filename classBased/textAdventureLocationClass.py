class Location:
    #Name - string | destinations - list of map indexes | items - list of items indexes | requirements - dictionary of boolians
    def __init__(self, newName, newDestinations, newItems, newRequirements):
        self.name = newName
        self.destinations = newDestinations
        self.items = newItems
        self.requirments = newRequirements

    def getName(self):
        return self.name

    def getDestinationIDs(self):
        return self.destinations
    
    def getItems(self):
        return self.items

    def addDestination(self, newDestinations):
        for i in newDestinations:
            self.destinations.append(i)

    def setRequirementStatus(self, reqName, status):
        if reqName in self.requirments:
            self.requirments[reqName] = status