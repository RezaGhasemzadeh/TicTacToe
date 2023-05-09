from termcolor import colored
board = list(range(1, 10))
player, computer = "X", "O"
print("Your symbol: <X>\ncomputers symbol: <O>")
winners_pos = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
edge_board = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


def print_board():
    j = 1
    for i in board:
        end = "  "
        if j % 3 == 0:
            end = "\n\n"
        if i == "X":
            print(colored(f"[{i}]", "blue"), end=end)
        elif i == "O":
            print(colored(f"[{i}]", "red"), end=end)
        else :
            print(f"[{i}]", end=end)
        j += 1


def is_winner(brd, plr):
    win = True
    for tup in winners_pos:
        win = True
        for j in tup:
            if brd[j] != plr:
                win = False
                break
        if win:
            break
    return win


def computer_move():
    j = -1
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            j = i
            break
        if j == -1:
            for u in range(1, 10):
                if make_move(board, player, u, True)[1]:
                    j = u
                    break
        if j == -1:
            for tup in edge_board:
                for m in tup:
                    if j == -1 and can_move(board, m):
                        j = m
                        break
    return make_move(board, computer, j)


def can_move(boar, position):
    if position in range(1, 10) and isinstance(boar[position-1], int):
        return True
    return False


def make_move(brd, plr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve-1] = plr
        win = is_winner(board, player)
        if undo:
            brd[mve-1] = mve
        return True, win
    else:
        return False, False


def check_empty_houses():
    return board.count("X") + board.count("O") != 9


while check_empty_houses():
    print_board()
    move = int(input("Choose your position[1-9]: "))
    moved, won = make_move(board, player, move)
    if not moved:
        print("invalid position!, Try again.\n")
        continue
    if won:
        print("You won!")
        break
    if computer_move()[1]:
        print("You lose! computer won.")
        break

print_board()





