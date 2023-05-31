import boardHandler as bh
import knightMove as km
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
    while True:
        printBoard(board)
        x, y = input("x: "), input("y: ")
        if board.getBoard()[int(x)][int(y)]["type"] == "knight":
            board.setPiece(int(x), int(y), km.knightmove(board.getPiece(int(x), int(y))))