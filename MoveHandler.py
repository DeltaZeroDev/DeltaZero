import pieceHandler as ph

def knightmove(knight : ph.knight, knightx : int, knighty : int, board):
    if knightx > 7 or knighty > 7:
        print("illegal move")
        return knight
    elif knightx < 0 or knighty < 0:
        print("illegal move")
        return knight
    elif knightx == knight.x + 2 and knighty == knight.y + 1:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x + 2 and knighty == knight.y - 1:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x + 1 and knighty == knight.y + 2:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x - 1 and knighty == knight.y + 2:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x - 2 and knighty == knight.y + 1:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x - 2 and knighty == knight.y - 1:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x - 1 and knighty == knight.y - 2:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
    elif knightx == knight.x + 1 and knighty == knight.y - 2:
        if board.isOccupied(knightx,knighty) and board.getPeice(knightx,knighty).color != knight.color:
                board.removePiece(knightx,knighty)
                knight.x = knightx
                knight.y = knighty
        elif not board.isOccupied(knightx,knighty):
                knight.x = knightx
                knight.y = knighty
        
        
    else:
        print("illegal move")
    return knight

def bishopmove(bishop : ph.bishop, bishopx : int, bishopy : int, board):
    pseudoLegals = []
    def check():
        if min(pseudoLegals[-1]) < 0 or max(pseudoLegals[-1]) > 7:
            pseudoLegals.pop()
            return False
        if board.isOccupied(*pseudoLegals[-1]):
            if board.getPiece(*pseudoLegals[-1]).color == bishop.color:
                pseudoLegals.pop()
            return True
        return False

    for x in range(1,7):
            pseudoLegals.append([bishop.x + x,bishop.y - x])
            if check():
                break
    for x in range(1,7):
            pseudoLegals.append([bishop.x + x,bishop.y + x])
            if check():
                break
    for x in reversed(range(7,0,-1)):
            pseudoLegals.append([bishop.x - x,bishop.y + x])
            if check():
                break
    for x in reversed(range(7,0,-1)):
            pseudoLegals.append([bishop.x - x,bishop.y - x])
            if check():
                break

    if [bishopx, bishopy] in pseudoLegals:
        if board.isOccupied(bishopx,bishopy):
            board.removePiece(bishopx,bishopy)
        bishop.x = bishopx
        bishop.y = bishopy

    else:
        print("illegal move")
    return bishop

def pawnmove(pawn : ph.pawn, pawnx : int, pawny : int, board):
    pseudoLegals = []
    forward = -1 if pawn.color == "black" else 1
    takeleft = [pawn.x - 1,pawn.y + forward]
    takeright = [pawn.x + 1,pawn.y + forward]
    if takeleft[1] > -1 and takeleft[1] < 8:
            if not board.isOccupied(pawn.x,pawn.y + forward):
                pseudoLegals.append([pawn.x,pawn.y + forward])
                if not board.isOccupied(pawn.x,pawn.y + (forward * 2)) and not pawn.moved:
                    pseudoLegals.append([pawn.x,pawn.y + (forward * 2)])
            if takeleft[1] > -1 and board.isOccupied(*takeleft) and board.getPiece(*takeleft).color != pawn.color:
                pseudoLegals.append(takeleft)
            if takeright[1] < 8 and board.isOccupied(*takeright) and board.getPiece(*takeright).color != pawn.color:
                pseudoLegals.append(takeright)
    if [pawnx,pawny] in pseudoLegals:
        if board.isOccupied(pawnx,pawny):
            board.removePiece(pawnx,pawny)
        pawn.x = pawnx
        pawn.y = pawny
        pawn.moved = True
    else:
         print("illegal move")
    return pawn

def rookmove(rook : ph.rook, rookx : int, rooky : int, board):
    pseudoLegals = []
    for i in range(rook.y+1,8):
        pseudoLegals.append([rook.x,i])
        if board.isOccupied(*pseudoLegals[-1]):
            if board.getPiece(*pseudoLegals[-1]).color == rook.color:
                pseudoLegals.pop()
            break
    for i in range(rook.y - 1,-1,-1):
          pseudoLegals.append([rook.x,i])
          if board.isOccupied(*pseudoLegals[-1]):
                if board.getPiece(*pseudoLegals[-1]).color == rook.color:
                    pseudoLegals.pop()
                break
    for i in range(rook.x+1,8):
        pseudoLegals.append([i,rook.y])
        if board.isOccupied(*pseudoLegals[-1]):
            if board.getPiece(*pseudoLegals[-1]).color == rook.color:
                pseudoLegals.pop()
            break
    for i in range(rook.x - 1,-1,-1):
          pseudoLegals.append([i, rook.y])
          if board.isOccupied(*pseudoLegals[-1]):
                if board.getPiece(*pseudoLegals[-1]).color == rook.color:
                    pseudoLegals.pop()
                break
    if [rookx,rooky] in pseudoLegals:
        if board.isOccupied(rookx,rooky):
            board.removePiece(rookx,rooky)
        rook.x = rookx
        rook.y = rooky
        rook.moved = True
    else:
         print("illegal move")
    return rook





def queenmove(queen : ph.queen, queenx : int, queeny : int, board):
     

   

