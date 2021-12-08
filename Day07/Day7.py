# 1. Read input file
# 2a. Find number of times the neighboring value is increasing -> print
# 2b. Sum up depths in sliding window, repeat 2a on new list -> print

def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines

def fuel_consumption(crabs,pos):
    consumption = 0
    for crab in crabs:
        dist = crab - pos
        if dist <= 0:
            consumption = consumption - dist
        else:
            consumption = consumption + dist
    return consumption

def dist2fuel(dist):
    fuel = 0
    if dist <=0:
        dist = -dist
    for x in range(dist):
        fuel = fuel + (dist-x)
    return fuel

def fuel_consumption_nonlin(crabs,pos):
    consumption = 0
    for crab in crabs:
        dist = crab - pos
        consumption = consumption + dist2fuel(dist)
    return consumption


def main():
    input = readfile('input-7.txt')
    input  = input[0].split(',')
    input = [int(x.strip()) for x in input]
    input.sort()
    
    fc = input[-1]*len(input)
    for pos in range(input[0], input[-1]+1):
        tmp = fuel_consumption(input,pos)
        if tmp < fc:
            fc = tmp
    
    print('mimimum fuel consumption (in linear case): ' +str(fc))
    
    ########
    fc = input[-1]*len(input)**2
    for pos in range(input[0], input[-1]+1):
        tmp = fuel_consumption_nonlin(input,pos)
        if tmp < fc:
            fc = tmp
    print('mimimum fuel consumption (in non-linear case): ' +str(fc))
    
    



if __name__ == '__main__':
    main()