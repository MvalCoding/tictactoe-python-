import random

#create game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
playerone = "X"
winner = None
game_running = True

def printboard(board):
    print(" -------------")
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" -------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" -------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")
    print(" -------------")



#take player input
def playerinput(board):
    index = 0
    while index == 0:
        try:
            playerin = int(input("Enter a number (1-9): "))
            if playerin >= 1 and playerin <= 9 and board[playerin-1] == "-":
                board[playerin-1] = playerone
                printboard(board)
                index += 1
            elif board[playerin-1] != "-":
                print("Position not available.")
                index = 0
            else:
                print("Invalid input!")
                index = 0
                playerin = int(input("Enter a number (1-9): "))
        except:
            print("Invalid input!")




#check for win or tie
def checkhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

def checkrows(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkdiagnal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

def checktie(board):
    global game_running
    if ("-" not in board and checkrows(board) == False and
        checkdiagnal(board) == False and checkhorizontal(board) == False):
        printboard(board)
        print("IT'S A TIE!")
        game_running = False

def checkwin():
    global game_running
    if checkrows(board) or checkdiagnal(board) or checkhorizontal(board):
        printboard(board)
        game_running = False

#switch player
def switchplayer():
    global playerone
    if playerone == "X":
        playerone = "O"
    else:
        playerone = "X"

#computer
def computer(board):
    while playerone == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchplayer()



#check for win or tie again
while game_running:
    printboard(board)
    playerinput(board)
    checktie(board)
    checkwin()
    switchplayer()
    computer(board)
    checkwin()
    checktie(board)

if winner == "X":
    print("YOU WIN!")
elif winner == "O":
    print("YOU LOSE :(")