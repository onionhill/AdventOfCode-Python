import re


with open('input.txt') as sample :
    data = sample.readlines()


def check_matrix(lineNumber, start,end) :
    ## Check the line above
    lineNumbers = []
    if lineNumber > 0 : lineNumbers.append(lineNumber-1)
    lineNumbers.append(lineNumber)
    if lineNumber+1 < len(data) :  lineNumbers.append(lineNumber +1)

    if start != 0:
        start = start -1
    
    for x in lineNumbers :
        if re.search(r'[^.\d]', data[x][start:end] ):
            return True

    return False

result = []
for x in range(len(data ) ) :
    line = data[x]
    matches = re.finditer(r'\d+', line)
    numbers_in_line = []
    for match in matches :
        if check_matrix(x, match.start(), match.end() ):        
            result.append(int(match.group()))   

print('Part 1', sum(result))