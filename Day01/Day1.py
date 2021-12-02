# 1. Read input file
# 2a. Find number of times the neighboring value is increasing -> print
# 2b. Sum up depths in sliding window, repeat 2a on new list -> print

def readintfile(file):
    with open(file) as f:
        lines = [int(x) for x in f.readlines()]
    return lines

def sliding_window(list, win_len):
    newlist = []
    for i in range(len(list)-win_len+1):
        newlist.append(sum(list[i:(i+win_len)]))
    return newlist

def main():
    depths = readintfile('input.txt')
    depth_increasing_idx = [x for x in range(len(depths)-1) if depths[x] < depths[x+1]]
    n_depth_increasing = len(depth_increasing_idx)
    print(f"The depth increased {n_depth_increasing} times")


    depths_sl = sliding_window(depths,3)
    depth_increasing_idx = [x for x in range(len(depths_sl)-1) if depths_sl[x] < depths_sl[x+1]]
    n_depth_increasing = len(depth_increasing_idx)
    print(f"The depth increased {n_depth_increasing} times (sliding window)")

if __name__ == '__main__':
    main()