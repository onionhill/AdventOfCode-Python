with open('games.txt', 'r') as f:
    games = f.read().splitlines()

validGames = []
bagItems = {
    'red': 12,
    'green': 13,
    'blue': 14
}

for game in games:
    gameId = game.split(':')[0].split(' ')[1]
    draws = [x.strip(' ') for x in game.split(':')[1].split(';')]

    result = []
    colors = {
        'red': 0,
        'green': 0,
        'blue': 0
    }
    for draw in draws:
        pairs = (item.split() for item in draw.split(','))
        for value, color in pairs:
            result.append((int(value), color))
            if colors[color] < int(value):
                colors[color] = int(value)
    validGames.append(int(colors['red'] * int(colors['green']) * int(colors['blue'] )))

print(sum(validGames))



#  draws = [(color, value) for draw in draws for color, value in [draw.split()]]

   
   

