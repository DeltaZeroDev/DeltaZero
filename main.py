import boardHandler as bh

def printBoard(board : bh.main):
    board = board.getBoard()
    for i in range(8):
        for j in range(8):
            if board[i][j] == None:
                print(" ", end="")
            else:
                if board[i][j]["color"] == "white":
                    print(board[i][j]["type"].upper(), end=" ")
                else:
                    print(board[i][j]["type"], end=" ")
        print()

if __name__ == "__main__":
    board = bh.main()
    printBoard(board)