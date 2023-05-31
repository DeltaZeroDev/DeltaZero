import boardHandler as bh

def printBoard(board : bh.main):
    board = board.getBoard()
    for y in range(8):
        for x in range(8):
            if x in board and y in board[x]:
                if board[x][y]["color"] == "white":
                    print(board[x][y]["typeShort"].upper(), end=" ")
                else:
                    print(board[x][y]["typeShort"].lower(), end=" ")
            else:
                print(" ", end=" ")
        print()

if __name__ == "__main__":
    board = bh.main()
    printBoard(board)