board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win = 1
draw = -1
running = 0
game = running
player = 1


def draw_board():
    print(board[0], "|", board[1], "|", board[2])
    print("__", "__", "__")
    print(board[3], "|", board[4], "|", board[5])
    print("__", "__", "__")
    print(board[6], "|", board[7], "|", board[8])
    print("__", "__", "__")


def check_position(x):
    if board[x] == " ":
        return True
    else:
        return False


def check_win():
    global game
    if board[0] == board[1] and board[1] == board[2] and board[0] != " ":
        game = win
    elif board[3] == board[4] and board[4] == board[5] and board[3] != " ":
        game = win
    elif board[6] == board[7] and board[7] == board[8] and board[6] != " ":
        game = win
    elif board[0] == board[3] and board[3] == board[6] and board[0] != " ":
        game = win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != " ":
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != " ":
        game = win
    elif board[0] == board[4] and board[4] == board[8] and board[0] != " ":
        game = win
    elif board[0] == board[4] and board[4] == board[6] and board[2] != " ":
        game = win
    elif board[0] != " " and board[1] != " " and board[2] != " " and board[3] != " " and board[4] != " " and board[
        5] != " " and board[6] != " " and board[7] != " " and board[8] != " ":
        game = draw
    else:
        game = running


print("Tic - Tac - Toe Game")
print("Player[1] = x ...... player[2]=0-->")
print()
while game == running:
    draw_board()
    if player % 2 != 0:
        print("Player[1] chance-")
        mark = 'X'
    else:
        print("player[2] chance-")
        mark = '0'
    choice = int(input("Enter b/w 1 to 9:"))
    if check_position(choice - 1):
        board[choice - 1] = mark
    player += 1
    check_win()

draw_board()
if game == draw:
    print("game draw")
else:
    if player % 2 == 0:
        print("player 2 won")
    else:
        print("player 1 won")
