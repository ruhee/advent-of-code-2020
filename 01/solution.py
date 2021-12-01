#! /usr/bin/python

filepath = 'input.txt'
file = open(filepath, 'r').read().strip().split('\n')

for x in file:
    for y in file:
        for z in file: 
            if int(x) + int(y) + int(z) == 2020:
                print('sum reached', x, y, z, int(x)*int(y)*int(z))
                break