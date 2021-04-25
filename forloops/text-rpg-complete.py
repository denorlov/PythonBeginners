name = None
health = 5
currentRoom = 'Зал'
inventory = []

rooms = {
    'Зал': {
        'description': "Все здесь, конечно, странно обставленно. Паутина, старое скрипучее кресло-качалка. Еще здесь много-много пыли. И как это путник, тебя сюда занесло?",
        'юг': 'Кухня',
        'запад': 'Столовая',
        'item': 'ключ'
    },

    'Кухня': {
        'description': "На кухне на плите стоит пара кастрюл. И в одной из кастрюль что-то жарится! Вонь стоит ужасная. Кто, интересно, может есть такую тухлятину?!",
        'север': 'Зал',
        'item': 'monster'
    },

    'Столовая': {
        'description': "В центре комнаты расположен огромный стол, на столе расставлены огромные, если не сказать гигансткие приборы. И еще кто-то собирался ужинать при свечах. На столе, на всех предметах мебели расставлены канделябры и свечи в канделябрах горят.",
        'восток': 'Зал',
        'юг': 'Сад',
        'item': 'яд'
    },

    'Сад': {
        'description': "В саду тихо, лишь слега шумит листва на ветру. И еще  немного жутко.",
        'север': 'Столовая'
    }
}

# ask the player their name
if name is None:
    name = input("Как тебя зовут, странник? ")

    print('''
Ваша задача попасть в Сад имея на руках Ключ и банку Яда.
Да, забыл сказать. Не попадайся монстрам! 
И еще. Каждый раз, когда ты перемещаешься в другую комнату, 
ты устаешь и твое здоровье уменьшается на 1.

Команды:
  идти [направление] (направление может быть: север, юг, восток, запад) 
  взять [предмет]''')

while True:
    print('---------------------------')
    print(name + ' находится в ' + currentRoom)
    print("Здоровье: " + str(health) + ". В рюкзаке: " + str(inventory))
    if "description" in rooms[currentRoom]:
        print(rooms[currentRoom]['description'])
    if "item" in rooms[currentRoom] and not 'monster' in rooms[currentRoom]['item']:
        print('Кажется, здесь есть ' + rooms[currentRoom]['item'])

    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('Ты повстречался с монстром... Конец игры!')
        break

    if health == 0:
        print('У тебя совсем не осталось сил... Ты умер!')
        break

    if currentRoom == 'Сад' and 'Ключ' in inventory and 'Яд' in inventory:
        print('Тебе удалось выбраться из этого жуткого дома... Ты победил!')
        break

    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

    if move[0] == 'идти':
        if move[1] in rooms[currentRoom]:
            health = health - 1
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('В направлении ' + move[1] + ' пройти нельзя!')

    if move[0] == 'взять':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' у нас в кармане!')
            del rooms[currentRoom]['item']
        else:
            print('Что такое ' + move[1] + '? Что-то не понимаю, что ты от меня хочешь')