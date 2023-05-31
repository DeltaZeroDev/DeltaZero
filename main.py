import boardHandler as bh

def printBoard(board : bh.main):
    for i in range(8):
        for j in range(8):
            print(board.getPos(i, j), end=" ")
        print()

if __name__ == "__main__":
    board = bh.main()
    printBoard(board)