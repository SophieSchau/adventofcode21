from typing import List


def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines

def calculating_generations(fish: List[int], day: int):
    _state = fish

    if day <= 0:
        return _state

    for i in range(0, len(_state)):
        _state[i] -= 1
        if _state[i] == 0:
            _state[i] = 6
            _state + [8]
            
    calculating_generations(_state, day - 1)

def main():
    start_cond = readfile('input-6.txt')
    birthdays = [int(x) for x in start_cond[0].split(',') ]
    ans = calculating_generations(birthdays, 80)
    print(ans)

if __name__ == '__main__':
    main()