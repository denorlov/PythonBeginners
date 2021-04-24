# map is here https://projects.raspberrypi.org/en/projects/rpg/7

name = ""
current_room = 'Hall'
health = 10

rooms = {
    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
    },

    'Kitchen': {
        'north': 'Hall',
    },

    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
    },

    'Garden': {
        'north': 'Dining Room'
    }
}

# ask the player their name
if name == "":
    name = input("What is your name Adventurer? ")

print("""Get to the Garden with a key and a potion
You are getting tired, each time you move you loose 1 health point.""")

while True:
    print('---------------------------')
    print(name + ' is in the ' + current_room + ", health is " + str(health))
    print(name + ' could go to ', end="")

    ways = rooms[current_room]
    for w in ways:
        print(w, end=",")
    print()

    direction = ''
    while direction == '':
        direction = input('Enter your direction>')

    if direction in rooms[current_room]:
        health = health - 1
        current_room = rooms[current_room][direction]
    else:
        print('You can\'t go that way!')
