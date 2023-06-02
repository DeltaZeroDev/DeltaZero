import boardHandler as bh
import MoveHandler as mh
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

def moveKnight(x, y, newX, newY, board : bh.main):
    board.setPiece(int(x), int(y), mh.knightmove(board.getPiece(int(x), int(y)), int(newX), int(newY)))
def moveBishop(x, y, newX, newY, board : bh.main):
    board.setPiece(int(x), int(y), mh.bishopmove(board.getPiece(int(x), int(y)), int(newX), int(newY), board))
def movePawn(x, y, newX, newY, board : bh.main):
    board.setPiece(int(x), int(y), mh.pawnmove(board.getPiece(int(x), int(y)), int(newX), int(newY), board))

if __name__ == "__main__":
    board = bh.main()
    while True:
        printBoard(board)

        x, y = input("x: "), input("y: ")
        if board.getBoard()[int(x)][int(y)]["type"] == "knight":
            newX, newY = input("new x: "), input("new y: ")
            moveKnight(x, y, newX, newY, board)

        
        elif board.getBoard()[int(x)][int(y)]["type"] == "bishop":
            newX, newY = input("new x: "), input("new y: ")
            moveBishop(x, y, newX, newY, board)
        
        elif board.getBoard()[int(x)][int(y)]["type"] == "pawn":
            newX, newY = input("new x: "), input("new y: ")
            movePawn(x, y, newX, newY, board)
