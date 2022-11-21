import textAdventureItemClass as itemClass

def devPotion(stats):
    stats['location'] = 'devRoom001'
    return stats

itemDict = {
    'devLetter' : itemClass.Message(
        #item nname
        'a letter from the developers',
        #item description
        'a letter which you are not ment to read',
        #command IDs
        [301],
        #message
        'hello'
    ),

    'prisonLetter' : itemClass.Message(
        'prison letter',
        'a letter found in the desk drawer in your prison cell',
        [301],
        'hello'
    ),

    'devPotion' : itemClass.functionRunnerItem(
        #item name
        'a magic potion from the devs',
        #item desription
        'a potion which you are not ment to drink',
        #command IDs
        [300],
        #function
        devPotion
    )

    #'prisonBedPillow' : itemClass.Item(
    #    'prison letter'
    #)
}