import map
location = 'prison cell'
inventory = []

#           move -------   get item   use item------
actions = ['move', 'open', 'take', 'use', 'read']

def action():
    sucsessAction = False
    while sucsessAction == False:
        tmpInput = input('> ')

        match (splitInput := tmpInput.split(' ', 1))[0]:
            case 'move':
                print(splitInput)
                if move(splitInput[1]):
                    sucsessAction = True
                
            case 'open':
                if move(splitInput[1]):
                    sucsessAction = True
            
            case 'take':
                if takeItem(splitInput[1]):
                    sucsessAction = True

            case 'read':
                print(splitInput)
                if interactItem(splitInput[1]):
                    sucsessAction = True

def move(destination):
    global location
    if destination not in map.mapDict[location].getDestinations():
        return False
    
    location = destination
    #print(map[location]['message'])
    return True

def takeItem(itemName):
    global location
    if (itemName in inventory) or (itemName not in map[location]['items']):# or (items[itemID]['requirements'][0] != 'none'):
        return False
    
    inventory.update({itemName : map[location]['items'][itemName]})
    return True

def interactItem(itemName):
    if itemName in inventory and items[inventory[itemName]]['type'] == 'message':
        print(items[inventory[itemName]]['message'])
        return True
    return False