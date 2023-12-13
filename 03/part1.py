import re


with open('input.txt') as sample :
    data = sample.readlines()

def get_bounderies(line, start,end) :
    lineNumbers = []
    if line > 0 : lineNumbers.append(line-1)
    lineNumbers.append(line)
    if line+1 < len(data) :  lineNumbers.append(line +1)

    if start != 0:
        start = start -1
    if end + 1 != len(data[0] ) :
        end = end + 1
    return {'lines': lineNumbers, 'start': start,'end':end}

def check_matrix_for_special_char(bounderies) :
    for x in bounderies['lines'] :
        if re.search(r'[^.\d]', data[x][bounderies['start']:bounderies['end'] ]):
            return True
    return False

def check_matrix_for_numbers(bounderies, numbers) :
    result = []
    for x in bounderies['lines'] :
        if x in numbers:
            for numb in numbers[x] :
                if numb[1] >= bounderies['start'] and numb[1] <= bounderies['end'] :
                    result.append(numb[0])
                elif numb[2] >= bounderies['start'] and numb[2] <= bounderies['end'] :
                    result.append(numb[0])
    return result

def part1() :
    part1_result = []
    for x in range(len(data ) ) :
        line = data[x].rstrip()
        matches = re.finditer(r'\d+', line)
        for match in matches :
            if not x in numbers_found : numbers_found[x] = []
            numbers_found[x].append( [int(match.group() ),match.start(), match.end()-1] )
            if check_matrix_for_special_char(get_bounderies(x, match.start(), match.end() )):       
                part1_result.append(int(match.group()))   

    print('Part 1', sum(part1_result))

def part2() :
    part2_result = []
    for x in range(len(data ) ) :
        line = data[x].rstrip()
        matches = re.finditer(r'[^.\d]',line )
        for match in matches :
            part2_data = check_matrix_for_numbers(get_bounderies(x, match.start(), match.end()-1 ), numbers_found)
            if len( part2_data) > 1:     
                part2_result.append(part2_data[0] * part2_data[1] )

    print('Part 1', sum(part2_result))

numbers_found = dict()
part1()
part2()