import map, player
playing = True


def exitGame():
    global playing
    playing = False

while playing:
    print(f"\n-------------------------\nYou are at '{map.mapDict[player.stats['location']].getName()}'\n-------------------------")
    player.action()
    if player.exit:
        exitGame()