map = {
    'prisonCell001' : {
        'routes' : {
            'to the prison door' : 'prisonDoor001',
            'to the desk' : 'prisonDesk001',
            'to the bed' : 'prisonBed001',
            'to thebox' : 'prisonBox001',
            'onto the carpet' : 'prisonCarpet001'
        },

        'items' : {
            'null' : 'null'
        },

        'message' : 'You look around at the room.'
    },

    'prisonDesk001' : {
        'routes' : {
           'away from desk' : 'prisonCell001',
           'drawer' : 'prisonDeskDrawer001'
        },

        'items' : {
            'null' : 'null'
        },

        'message' : 'There is a drawer'
    },

    'prisonDeskDrawer001' : {
        'routes' : {
           'close drawer' : 'prisonDesk001'
        },

        'items' : {
            'letter' : 'letter001'
        },

        'message' : 'There is a letter in the draw'
    }
}

items = {
    'letter001' : {
        'name' : 'note from captors',
        'requirements' : ['none'],
        'type' : 'message',
        'message' : 'You read the letter.. It was a summer day'
    },

    'letterDEV' : {
        'name' : 'letter from devs',
        'requirements' : ['none'],
        'type' : 'message',
        'message' : 'Your not meant to find this'
    }
}

#           move -------   get item   use item------
actions = ['move', 'open', 'take', 'use', 'read']

location = 'prisonCell001'
inventory = {}

def outputRoutesItems(dictionary):
    for i in dictionary:
        print(f' - {i}')


def action():
    sucsessAction = False
    while sucsessAction == False:
        tmpInput = input('\n> ')

        match (splitInput := tmpInput.split(' ', 1))[0]:
            case 'move':
                #print(splitInput)
                if move(splitInput[1]):
                    sucsessAction = True
                
            case 'open':
                if move(splitInput[1]):
                    sucsessAction = True
            
            case 'take':
                if takeItem(splitInput[1]):
                    sucsessAction = True

            case 'read':
                #print(splitInput)
                if interactItem(splitInput[1]):
                    sucsessAction = True

def move(destination):
    global location
    if destination not in map[location]['routes']:
        return False
    
    location = map[location]['routes'][destination]
    print(map[location]['message'])
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

while True:
    #print(map[location]['message'])
    #print(f'location is {location}')

    print('\nYou move to..')
    outputRoutesItems(map[location]['routes'])

    action()