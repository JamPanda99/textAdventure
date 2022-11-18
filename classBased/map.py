import textAdventureLocationClass as locClass

mapDict = {
    'dev room' : locClass.Location(
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

    'prison cell' : locClass.Location(
        'prison cell',
        [
            'prisonDoor001',
            'prison desk',
            'prisonBed001',
            'prisonDesk001',
            'prisonBox001',
            'prisonCarpet001'
        ],
        [
            'none'
        ],
        {
            'null' : True
        }
    ),

    'prison desk' : locClass.Location(
        'prison desk',
        [
            'prison cell',
            'prison desk drawer'
        ],
        [
            'none'
        ],
        {
            'null' : True
        }
    ),

    'prison desk drawer' : locClass.Location(
        'desk drawer',
        [
            'prison desk'
        ],
        [
            'letter'
        ],
        {
            'null' : True
        }
    )
}