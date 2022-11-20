import map, items
location = 'prisonCell001'
inventory = []
exit = False

actions = {
    #move to location normal
    'move to '  :   1,
    'go to '    :   1,
    'travel to ':   1,
    #move to special locations type1 (e.g. doors, drawers, boxes...)
    'open '     :   2,
    #take item
    'take '     :   3,
    #use item normal
    'use '      :   4,
    #use special item type1 (e.g. book, letter...)
    'read '     :   5,


    #exits game
    'exit'      :   999
}

def action():
    successAction = False
    while successAction == False:
        actionType, actionSyntax = getActionType(input('> '))

        match (actionType):
            case 1 | 2:
                if move(actionType, actionSyntax):
                    successAction = True
            
            case 3:
                if takeItem(actionType, actionSyntax):
                    successAction = True

            case 4:
                if interactItem(actionType, actionSyntax):
                    successAction = True

            case 999:
                global exit
                exit = True
                successAction = True

def getActionType(actionCommand):
    global actions
    for i in actions:
        if i in actionCommand:
            return actions[i], actionCommand.split(i)[1]
    return -1, 'null'

def move(actionType, destination):
    global location
    tmp = {}
    for i in map.mapDict[location].getDestinationIDs():
        tmp.update({map.mapDict[i].getName() : i})

    if destination not in tmp:
        return False
    
    location = tmp[destination]
    return True

def takeItem(actionType, itemId):
    global location
    if (itemId in inventory) or (itemId not in map.mapDict[location].getItems()):# or (items[itemID]['requirements'][0] != 'none'):
        return False
    
    inventory.update(itemId)
    return True

def interactItem(actionType, itemName):
    if itemName in inventory and items[inventory[itemName]]['type'] == 'message':
        print(items[inventory[itemName]]['message'])
        return True
    return False