import textAdventureLocationClass as locClass, textAdventureItemClass as itemClass, map, player
playing = True


def exitGame():
    global playing
    playing = False

while playing:
    print(map.mapDict[player.location].getName())
    player.action()
    if player.exit:
        exitGame()