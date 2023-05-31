import boardHandler as bh
import colorama as c

def printBoard(board : bh.main):
    board = board.getBoard()
    for y in range(8):
        for x in range(8):
            if x in board and y in board[x]:
                if board[x][y]["color"] == "white":
                    print(c.Fore.RED + board[x][y]["typeShort"].upper() + c.Style.RESET_ALL, end=" ")
                else:
                    print(c.Fore.BLUE + board[x][y]["typeShort"].lower() + c.Style.RESET_ALL, end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    board = bh.main()
    printBoard(board)