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
    
    def setPos(self, y, x, value):
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
        # THIS IDIOT DOESN'T KNOW HOW COORDINATES WORK HELP ME PLEASE - Zero
        # (He flipped the x and y corrdinates around and reversed them even after I fixed it) - Zero
        for i in range(8):
            # place pawns
            self.setPos(i, 1, ph.pawn(i, 1, "white"))
            self.setPos(i, 6, ph.pawn(i, 6, "black"))
        # knights
        self.setPos(6, 0, ph.knight(7, 0, "white")) 
        self.setPos(1, 0, ph.knight(2, 0, "white"))
        self.setPos(1, 7, ph.knight(2, 7, "black"))
        self.setPos(6, 7, ph.knight(7, 7, "black"))
        # bishops
        self.setPos(5, 0, ph.bishop(6, 0, "white"))
        self.setPos(2, 0, ph.bishop(6, 0, "white"))
        self.setPos(2, 7, ph.bishop(6, 0, "black"))
        self.setPos(5, 7, ph.bishop(6, 7, "black"))
        # queens
        self.setPos(3, 0, ph.queen(4, 0, "white"))
        self.setPos(3, 7, ph.queen(4, 7, "black"))
        # kings
        self.setPos(4, 0, ph.king(5, 0, "white"))
        self.setPos(4, 7, ph.king(5, 7, "black"))
        # rooks
        self.setPos(0, 0, ph.rook(1, 0, "white"))
        self.setPos(7, 0, ph.rook(7, 0, "white"))
        self.setPos(0, 7, ph.rook(0, 7, "black"))
        self.setPos(7, 7, ph.rook(7, 7, "black"))
