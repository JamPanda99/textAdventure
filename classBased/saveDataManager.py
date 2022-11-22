def load():
    dataFile = open('classBased/player.saveData', 'r')
    data = dataFile.read()
    dataFile.close()

    stats = {
        'location' : '',
        'inventory' : {
        }
    }

    stats['location'] = (tmp := data.split('\n'))[0]
    for i in tmp[1].split('```'):
        stats['inventory'].update({i.split(':')[0]:i.split(':')[1]})

    return stats


def save(stats):
    newData = str(f"{stats['location']}\n")

    for i in stats['inventory']:
        newData = newData + str(f"{i}:{stats['inventory'][i]}```")
    newData = newData[:-3]

    data = open('classBased/player.saveData', 'w')
    data.write(newData)
    data.close()