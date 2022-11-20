import textAdventureLocationClass as locClass

mapDict = {
    #location ID : class instance
    'devRoom001' : locClass.Location(
        #roomName
        'dev room',
        #desinations
        [],
        #items
        [],
        #reqirements to enter
        {
            'beADev' : False
        }
    ),

    'prisonCell001' : locClass.Location(
        'prison cell',
        [
            #'prisonDoor001',
            'prisonDesk001',
            'prisonBed001',
            #'prisonBox001',
            #'prisonCarpet001'
        ],
        [
            'none'
        ],
        {
            'null' : True
        }
    ),

    'prisonDesk001' : locClass.Location(
        'prison desk',
        [
            'prisonCell001',
            'prisonDeskDrawer001'
        ],
        [
            'none'
        ],
        {
            'null' : True
        }
    ),

    'prisonDeskDrawer001' : locClass.Location(
        'desk drawer',
        [
            'prisonDesk001'
        ],
        [
            'letter'
        ],
        {
            'null' : True
        }
    ),

    'prisonBed001' : locClass.Location(
        'prison bed',
        [
            'prisonCell001'
        ],
        [
            'none'
        ],
        {
            'null' : True
        }
    ),
}