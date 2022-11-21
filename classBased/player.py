import map, items

stats = {
    'location' : 'prisonCell001',
    'inventory' : {
        'a magic potion from the devs' : 'devPotion'
    }
}

exit = False

actions = {
    #print locations player can travel too
    'look around'       :   0,
    #print inventory of player
    'open inventory'    :   1,
    #move to location normal
    'move to '          :   100,
    'go to '            :   100,
    'travel to '        :   100,
    #move to special locations type1 (e.g. doors, drawers, boxes...)
    'open '             :   101,
    #take item
    'take '             :   200,
    #use functionRunnerItem item
    'use '              :   300,
    #use Message item
    'read '             :   301,


    #exits game
    'exit'              :   999
}

def getActionType(actionCommand):
    global actions
    for i in actions:
        if i in actionCommand:
            return actions[i], actionCommand.split(i)[1]
    return -1, 'null'

def move(actionType, destination):
    global stats
    tmp = {}
    for i in map.mapDict[stats['location']].getDestinationIDs():
        tmp.update({map.mapDict[i].getName() : i})

    if destination not in tmp:
        return False

    stats['location'] = tmp[destination]
    print(f"\nYou move to {destination}")
    return True

def takeItem(actionType, itemName):
    global stats
    if (itemName in stats['inventory']) or (itemName not in map.mapDict[stats['location']].getItems()):# or (items[itemID]['requirements'][0] != 'none'):
        return False
    
    tmp = map.mapDict[stats['location']].getItems()[itemName]
    stats['inventory'].update({items.itemDict[tmp].getName() : tmp})
    return True

def interactItem(actionType, itemName):
    if (itemName not in stats['inventory']) or (actionType not in items.itemDict[stats['inventory'][itemName]].getCommandIDs()):
        return False

    if actionType == 300:
        items.itemDict[stats['inventory'][itemName]].activateItem(stats)

def action():
    successAction = False
    while successAction == False:
        actionType, actionSyntax = getActionType(input('> '))

        match (actionType):
            case 0:
                print()
                tmp = []
                for i in map.mapDict[stats['location']].getDestinationIDs():
                    print(f' - {map.mapDict[i].getName()}')

                successAction = True
            
            case 1:
                print()
                for i in stats['inventory']:
                    print(i)

                successAction = True

            case 100 | 101:
                if move(actionType, actionSyntax):
                    successAction = True
            
            case 200:
                if takeItem(actionType, actionSyntax):
                    successAction = True

            case 300 | 301:
                if interactItem(actionType, actionSyntax):
                    successAction = True

            case 999:
                global exit
                exit = True
                successAction = True

        if not successAction:
            print('Action Failed')