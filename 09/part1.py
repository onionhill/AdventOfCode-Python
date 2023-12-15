with open('input.txt') as file :
    lines = file.readlines()

part_1 = 0
part_2 = 0

def get_next_value(h):
    if all(n == 0 for n in h) : return 0
    else:
        diff = [h[i +1]- h[i] for i in range(len(h) -1 ) ]
        return h[-1] + get_next_value(diff)
                                                        
def get_prev_value(h) :
    if all(n == 0 for n in h) : return 0
    else:
        diff = [h[i +1]- h[i] for i in range(len(h) -1 ) ] 
        return h[0] - get_prev_value(diff)

for line in lines : 
    history = [int(x) for x in line.split() ]
    part_1 += get_next_value(history)
    part_2 += get_prev_value(history)



print('part 1', part_1)
print('part 2', part_2)