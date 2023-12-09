with open('t.txt', 'r') as f:

    lines = f.readlines()

    sum = 0


    for line in lines:
        first = 0
        last = 0
        for s in line:
            if(s.isdigit()):
                if(first == 0):
                    first = s
                last = s
        sum += int(str(first) + str(last))
    print(sum)

