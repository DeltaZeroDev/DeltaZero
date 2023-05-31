class chessBoard():
    def __init__(self) -> None:
        self.board = [[0 for i in range(8)] for j in range(8)]

    def getPos(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return None
        else:
            return self.board[x][y]
    
    def setPos(self, x, y, value):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return None
        else:
            self.board[x][y] = value