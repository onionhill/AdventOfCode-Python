def find_value(line: str, direction: str) -> list[tuple[int, int]]:
    mappings = {
        '1': 1, 'one': 1,
        '2': 2, 'two': 2,
        '3': 3, 'three': 3,
        '4': 4, 'four': 4,
        '5': 5, 'five': 5,
        '6': 6, 'six': 6,
        '7': 7, 'seven': 7,
        '8': 8, 'eight': 8,
        '9': 9, 'nine': 9,
    }
    if(direction == 'start'):
        return [(line.find(digit), value) for digit, value in mappings.items() if line.find(digit) != -1]
    else:
        return [(line.rfind(digit), value) for digit, value in mappings.items() if line.rfind(digit) != -1]



with open('t.txt', 'r') as f:
    input_data = f.read().splitlines()
    
values = [int(
    str(min(find_value(line, 'start'))[1] ) + 
    str(max(find_value(line, 'end')) [1] )
) for line in input_data]


print(sum(values))