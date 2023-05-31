import pieceHandler as ph
import json

class main():
    def __init__(self) -> None:
        self.board = []
        self.placePieces()

    def getBoard(self):
        board = {}
        for peice in self.board:
            peice = peice.__dict__()
            if peice["x"] not in board:
                board[peice["x"]] = {}
            board[peice["x"]][peice["y"]] = peice
        return board
    
    def isOccupied(self,x,y):
        print(x, y)
        sortedBoard = [[0] * 8 for i in range(0,8)]
        for peice in map(lambda j: j.__dict__(),self.board):
            sortedBoard[peice["y"]][peice["x"]] = [peice["typeShort"],peice["color"]]
        return sortedBoard[x][y] != 0
    
    def getPiece(self, x, y):
        for piece in self.board:
            print(piece.x, piece.y, x, y)
            if piece.x == x and piece.y == y:
                return piece
        return None
    
    def setPiece(self, x, y, piece):
        for i in range(len(self.board)):
            if self.board[i].x == x and self.board[i].y == y:
                self.board[i] = piece
                return
        self.board.append(piece)

    def placePieces(self):
        for i in range(8):
            # place pawns
            self.board.append(ph.pawn(i, 1, "white"))
            self.board.append(ph.pawn(i, 6, "black"))
        # knights
        self.board.append(ph.knight(1, 0, "white")) 
        self.board.append(ph.knight(1, 7, "black"))
        self.board.append(ph.knight(6, 0, "white"))
        self.board.append(ph.knight(6, 7, "black"))
        # bishops
        self.board.append(ph.bishop(2, 0, "white"))
        self.board.append(ph.bishop(2, 7, "black"))
        self.board.append(ph.bishop(5, 0, "white"))
        self.board.append(ph.bishop(5, 7, "black"))
        # queens
        self.board.append(ph.queen(4, 0, "white"))
        self.board.append(ph.queen(4, 7, "black"))
        # kings
        self.board.append(ph.king(3, 0, "white"))
        self.board.append(ph.king(3, 7, "black"))
        # rooks
        self.board.append(ph.rook(0, 0, "white"))
        self.board.append(ph.rook(7, 0, "white"))
        self.board.append(ph.rook(0, 7, "black"))
        self.board.append(ph.rook(7, 7, "black"))

if __name__ == "__main__":
    board = main()
    print(json.dumps(board.getBoard(), indent=4))
