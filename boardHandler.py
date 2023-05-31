import pieceHandler as ph

class main():
    def __init__(self) -> None:
        self.board = [[None for i in range(8)] for j in range(8)]
        self.placePieces()

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

    def getBoard(self) -> list:
        # convert peice objects to strings
        board = [[None for i in range(8)] for j in range(8)]
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == None:
                    board[i][j] = None
                else:
                    peice = self.board[i][j].__dict__()
                    board[i][j] = {"color": peice["color"], "type": peice["typeShort"]}
        return board
    
    def placePieces(self):
        # place pawns
        for i in range(8):
            self.setPos(1, i, ph.pawn(1, i, "white"))
            self.setPos(6, i, ph.pawn(6, i, "black"))