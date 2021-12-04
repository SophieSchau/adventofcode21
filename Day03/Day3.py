def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines

def main():
    lines = readfile('input-3.txt')
    n_columns = len(lines[0])-1
    n_lines = len(lines)
    tmp = [0] * n_columns
    for col in range(n_columns):
        for lin in range(n_lines):
            tmp[col] = tmp[col]+int(lines[lin][col])
    gamma_rate = [1 if x > n_lines/2 else 0 for x in tmp]
    gamma_rate = [str(gr) for gr in gamma_rate] 
    gamma_rate = "". join(gamma_rate)
    gamma_rate = int(gamma_rate, base=2)

    epsilon_rate = [1 if x < n_lines/2 else 0 for x in tmp]
    epsilon_rate = [str(gr) for gr in epsilon_rate] 
    epsilon_rate = "". join(epsilon_rate)
    epsilon_rate = int(epsilon_rate, base=2)

    power = gamma_rate * epsilon_rate

    print("gamma rate: " + str(gamma_rate))
    print("epsilon rate: " + str(epsilon_rate))
    print("power: " + str(power))

##########
    ox = lines

    n_columns = len(ox[0])-1
    tmp = [0] * n_columns
    for col in range(n_columns):
        for lin in range(n_lines):
            tmp[col] = tmp[col]+int(ox[lin][col])
        if tmp[col] >= n_lines/2.0:
            ox = [ox[l] for l in range(len(ox)) if ox[l][col] == '1']
        else:
            ox = [ox[l] for l in range(len(ox)) if ox[l][col] == '0']
        n_lines = len(ox)
        if n_lines == 1:
            break

    ox = [str(x) for x in ox] 
    ox = "". join(ox)
    ox = int(ox, base=2)

    co2 = lines

    n_columns = len(co2[0])-1
    tmp = [0] * n_columns
    for col in range(n_columns):
        for lin in range(n_lines):
            tmp[col] = tmp[col]+int(co2[lin][col])
        if tmp[col] < n_lines/2.0:
            co2 = [co2[l] for l in range(len(co2)) if co2[l][col] == '1']
        else:
            co2 = [co2[l] for l in range(len(co2)) if co2[l][col] == '0']
        n_lines = len(co2)
        if n_lines == 1:
            break

    co2 = [str(x) for x in co2] 
    co2 = "". join(co2)
    co2 = int(co2, base=2)

    life_support = ox * co2

    print("oxygen generator rating: " + str(ox))
    print("CO2 scrubber rating: " + str(co2))
    print("life support rating: " + str(life_support))









if __name__ == '__main__':
    main()