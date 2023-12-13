
with open('input.txt') as sample :
    data = sample.readlines()    

def get_numb_of_winners(winners, numbers) :
    return sum(numb in winners for numb in numbers)

def get_points(winners) :
    if winners < 2 : return winners
    return pow(2, winners-1)

result = []
scratchlist = dict()

def add_to_list(x,numb) :

    scratchlist[x] = scratchlist.get(x,0) + numb

for x in range(len(data) ) :
    add_to_list(x,1)
    line = data[x]
  
    winners = [int (num) for num in line.split(':')[1].split('|')[0].split() if num.isdigit ]
    numbers = [int(num) for num in line.split('|')[1].split() if num.isdigit()]

    result.append(  get_points( get_numb_of_winners(winners, numbers)) )

    for i in range(1, get_numb_of_winners(winners, numbers) + 1) :
        add_to_list(x + i, scratchlist[x])

print("Part 1" , sum(result))
print("Part 2", sum(scratchlist.values() ) )