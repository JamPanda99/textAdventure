import map, player, saveDataManager
playing = True

#load data
player.stats = saveDataManager.load()

def exitGame():
    saveDataManager.save(player.stats)
    global playing
    playing = False

while playing:
    print(f"\n-------------------------\nYou are at '{map.mapDict[player.stats['location']].getName()}'\n-------------------------")
    player.action()
    if player.exit:
        exitGame()