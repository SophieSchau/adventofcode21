def readfile(file):
    with open(file) as f:
        lines = [x for x in f.readlines()]
    return lines


def main():
    input = readfile('input-4.txt')    
    draw = input[0]
    draw = draw.strip().split(',')
    
    boards = [0]* int((len(input)-1)/6)
    for ii in range(len(boards)):
        boards[ii] = input[(ii*6)+2:(ii*6)+7] 
        boards[ii] = [ x.strip().split() for x in boards[ii]]

    BINGO = False
    for num in draw:
        for board in boards:
            for row in range(len(board)):
                board[row] = ['X' if x==num else x for x in board[row]]
                if board[row] == ['X'] *  5:
                    BINGO  = True
                    print('BINGO (row)!')
            if BINGO:
                unmarked = [x if x != 'X' else '0' for x in sum(board,[])]
                score = sum([int(x) for x in unmarked])
                print(f"the score was: {score}")
                print(f"the winning number was: {num}")
                print(f"multiplication: {score  * int(num)}")
                break
            for col in range(len(board)):
                testcol = [x[col]  for x in board]
                if testcol == ['X'] *  5:
                    BINGO  = True
                    print('BINGO (column)!')
            if BINGO:
                unmarked = [x if x != 'X' else '0' for x in sum(board,[])]
                score = sum([int(x) for x in unmarked])
                print(f"the score was: {score}")
                print(f"the winning number was: {num}")
                print(f"multiplication: {score  * int(num)}")
                break
        if BINGO:
            break

    print("")
############# RESET BOARDS FOR PART 2:
    boards = [0]* int((len(input)-1)/6)
    for ii in range(len(boards)):
        boards[ii] = input[(ii*6)+2:(ii*6)+7] 
        boards[ii] = [ x.strip().split() for x in boards[ii]]

    BINGO = [False] * len(boards)
    for num in draw:
        for board_n in range(len(boards)):
            board = boards[board_n]
            for row in range(len(board)):
                board[row] = ['X' if x==num else x for x in board[row]]
                if board[row] == ['X'] *  5:
                    BINGO[board_n]  = True
            for col in range(len(board)):
                testcol = [x[col]  for x in board]
                if testcol == ['X'] *  5:
                    BINGO[board_n]  = True
            if all(BINGO):
                unmarked = [x if x != 'X' else '0' for x in sum(board,[])]
                score = sum([int(x) for x in unmarked])
                print(f"the score was: {score}")
                print(f"the winning number was: {num}")
                print(f"multiplication: {score  * int(num)}")
                break
        if all(BINGO):
            break    
                

    


if __name__ == '__main__':
    main()