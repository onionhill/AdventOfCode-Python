import re

## trying to use a regex to get the number
pattern = r'\d{1,2} green|\d{1,2} red|\d{1,2} blue'

class BagGame:
    def __init__(self,red,green,blue,file) -> None:
        self.RED_MAX = red
        self.GREEN_MAX = green
        self.BLUE_MAX = blue
        self.FILE = file
    
    def read_data(self):
        with open(self.FILE, 'r') as data:
            return data.readlines()
        
    def process_data(self):
        return list(map(lambda x: re.findall(pattern, x), self.read_data()))

    def find_pow_value(self):
        total = 0
        for game in self.process_data():
            name_and_color = [(int(round.split()[0]), round.split()[1]) for round in game]
            print(name_and_color)
            max_values = {
                'red': 0,
                'blue': 0,
                'green': 0
            }
            for draw in name_and_color:
                max_values[draw[1]] = max(max_values[draw[1]], draw[0])
            total += max_values['blue'] * max_values['green'] * max_values['red']
        return total

bag_game = BagGame(red=12, green=13, blue=14, file='games.txt')
print(bag_game.find_pow_value() )