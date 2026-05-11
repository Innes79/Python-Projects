#X = 1
#O = 5
import os
import sys
import time
import random


board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


def clear():
    os.system("cls" if sys.platform=="win32" else "clear")

    
def sumofrow(board):
    for row in board:
        sumrow = sum(row)
        
        if sumrow == 15:
            clear()
            Display(board)
            print("O won")
            print("")
            input("Press Enter to close...")
            sys.exit()
        elif sumrow == 3:
            clear()
            Display(board)
            print("X won")
            print("")
            input("Press Enter to close...")
            sys.exit()


def sumofcolumn(board):
    for i in range(len(board)):
        sumcolumn=0
        for row in board:
            sumcolumn+=row[i]
        if sumcolumn == 15:
            clear()
            Display(board)
            print("O won")
            print("")
            input("Press Enter to close...")
            sys.exit()
        elif sumcolumn == 3:
            clear()
            Display(board)
            print("X won")
            print("")
            input("Press Enter to close...")
            sys.exit()
            
def diagonalsum(board):
    if board[0][0] == 5 and board[1][1] == 5 and board[2][2] == 5:
        clear()
        Display(board)
        print("O won")
        print("")
        input("Press Enter to close...")
        sys.exit()
    elif board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1:
        clear()
        Display(board)
        print("X won")
        print("")
        input("Press Enter to close...")
        sys.exit()

    elif board[0][2] == 5 and board[1][1] == 5 and board[2][0] == 5:
        clear()
        Display(board)
        print("O won")
        print("")
        input("Press Enter to close...")
        sys.exit()
    elif board[0][2] == 1 and board[1][1] == 1 and board[2][0] == 1:
        clear()
        Display(board)
        print("X won")
        print("")
        input("Press Enter to close...")
        sys.exit()
        
def Display(board):
    found_displays = []
    for row in board:
        for cell in row:
            if cell == 5:
                found_displays.append("O")
            elif cell == 1:
                found_displays.append("X")
            elif cell == 0:
                found_displays.append(" ")
         
        print(" ".join(found_displays))
        found_displays.clear()
    print("")
        
def player_turn(turn, board):
    if turn == "Playertwo":
        move = input(f"{turn}, enter your move (row,col): ")
        individual_coords = move.split(',')
        row = int(individual_coords[0])
        col = int(individual_coords[1])
        value = board[row-1][col-1]
        if 1 <= row <= 3 and 1 <= col <= 3:
            print(f"The space at ({row},{col}) is free")
            clear()
            if board[row-1][col-1] == 0:
                board[row-1][col-1] = player2
                sumofcolumn(board)
                sumofrow(board)
                diagonalsum(board)
            else:
                print("this spot on the board is taken choose another")
                player_turn(turn, board)
        else:
            print("invalid option, please enter row and column values between 1 and 3")
            player_turn(turn, board)
    if turn == "Playerone":
        move = input(f"{turn}, enter your move (row,col): ")
        individual_coords = move.split(',')
        row = int(individual_coords[0])
        col = int(individual_coords[1])
        value = board[row-1][col-1]
        if 1 <= row <= 3 and 1 <= col <= 3:
            print(f"The space at ({row},{col}) is: free")
            if board[row-1][col-1] == 0:
                board[row-1][col-1] = player1
                clear()
                sumofcolumn(board)
                sumofrow(board)
                diagonalsum(board)
            else:
                print("this spot on the board is taken choose another")
                player_turn(turn, board)
        else:
            print("invalid option, please enter row and column values between 1 and 3")
            player_turn(turn, board)

def Computer(board):

    while True:
        ComRow = random.randint(1, 3)
        ComCol = random.randint(1, 3)
        
        
        if board[ComRow-1][ComCol-1] == 0:
            board[ComRow-1][ComCol-1] = player2
            sumofrow(board)
            sumofcolumn(board)
            diagonalsum(board)
            break

        
input("This is tic tac toe, press enter to play")
input("The empty spots on the board will apear as just a blank space")
clear()
input("also credit to andrii for helping create the column adddition function")
clear()
gametype = input("Would you like to play (s)olo or (m)ultiplayer: ").lower()
selection = input("would you like to be (X / O): ").lower()
clear()

if selection == "x":
    player1 = 1
    player2 = 5
elif selection == "o":
    player1 = 5
    player2 = 1
    
    
if gametype == "m":
    for i in range(9):
        clear()
        Display(board)
        
        if i % 2 == 0:
            turn = "Playerone"
        else:
            turn = "Playertwo"
        player_turn(turn, board)
    clear()
    Display(board)
    print("Nobody won, its a draw!")

elif gametype == "s":
    turn = "playerone"
    for i in range(9):
        clear()
        Display(board)

        if i % 2 == 0:
            player_turn(turn, board)
        else:
            time.sleep(1)
            Computer(board)
