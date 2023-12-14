from functools import reduce

with open('./input.txt', 'r') as file:
    lines = file.readlines()

time_line = lines[0].split()[1:]
distance_line = lines[1].split()[1:]

time = [int(t) for t in time_line]
distance = [int(d) for d in distance_line]

race = list(zip(time, distance) )
def part1(race) :
    race_winners = []
    for x in range(len(race) ) :
        t, d = race[x]
        winner_times = []
        for charge_time in range(1, t) :
            if (t - charge_time) * charge_time > d :
                winner_times.append((d - charge_time) * charge_time)
        race_winners.append(len(winner_times))
    return race_winners

def part2() :
    race = [(59796575, 597123410321328)]
    race_winners = []
    for x in range(len(race) ) :
        t, d = race[x]
        winner_times = []
        for charge_time in range(1, t) :
            if (t - charge_time) * charge_time > d :
                winner_times.append((d - charge_time) * charge_time)
        race_winners.append(len(winner_times))
    return race_winners

race_winners = part1(race)
race_winners2 = part2()
print('part 1', reduce(lambda x,y: x*y, race_winners))
print('part 2', race_winners2)



