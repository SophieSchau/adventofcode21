def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines


def main():
    commands = readfile('input-2.txt')

    x = 0
    depth = 0

    for ii in range(len(commands)):
        command = commands[ii]
        if command[0] == 'f':
            x = x + int(command.split()[1])
        elif command[0] == 'd':
            depth  = depth +  int(command.split()[1])
        elif command[0] == 'u':
            depth  = depth -  int(command.split()[1])
    
    print(f"A) Horizontal  distance: {x}")
    print(f"A) Depth: {depth}")
    print(f"A) Multiply depth and horzontal distance: {x*depth}")


    x = 0
    depth = 0
    aim = 0

    for ii in range(len(commands)):
        command = commands[ii]
        if command[0] == 'f':
            x = x + int(command.split()[1])
            depth = depth + int(command.split()[1])*aim
        elif command[0] == 'd':
            aim  = aim +  int(command.split()[1])
        elif command[0] == 'u':
            aim  = aim -  int(command.split()[1])
    
    print(f"B) Horizontal  distance: {x}")
    print(f"B) Depth: {depth}")
    print(f"B) Multiply depth and horzontal distance: {x*depth}")
            


if __name__ == '__main__':
    main()