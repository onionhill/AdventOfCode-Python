
with open('input.txt') as sample :
    data = sample.readlines()    

def get_numb_of_winners(winners, numbers) :
    return sum(numb in winners for numb in numbers)

def get_points(winners) :
    if winners < 2 : return winners
    return pow(2, winners-1)

result = []
for line in data :
    winners = [int (num) for num in line.split(':')[1].split('|')[0].split() if num.isdigit ]
    numbers = [int(num) for num in line.split('|')[1].split() if num.isdigit()]

    result.append(  get_points( get_numb_of_winners(winners, numbers)) )

print("Part 1" , sum(result))