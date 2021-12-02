#! /usr/local/bin/python3

filepath = 'input.txt'
file = open(filepath, 'r').read().strip().split('\n')

# format:
# 2-9 c: ccccccccc

def get_vars(line, is_index = False):
    instruction, content = line.split(': ')
    letter_range, letter = instruction.split(' ')
    x, y = map(int, letter_range.split('-'))

    if (is_index):
        return [x-1, y-1, letter, content]

    return [x, y, letter, content]

def part1():
    valid_count = 0

    for line in file:
        x, y, letter, content = get_vars(line)
        count = content.count(letter)

        if count >= x and count <= y:
            valid_count += 1
    print(f'Part 1: {valid_count}')
    

def part2():
    valid_count = 0
    
    for line in file:
        x, y, letter, content = get_vars(line, True)
        print(line, x, y)

        # the letter should occur exactly 1 time between position x and position y
        # if it is 0 times or 2+ times it's invalid

        str = content[x:y]

        if(str.count(letter) == 1):
            # print(x, y, letter, content, '-----', str.count(letter))
            valid_count += 1
        else:
            print('invalid?', x, y, letter, content)

    print(f'Part 2: {valid_count}')

part1()
part2()