import pieceHandler as ph

def knightmove(knight : ph.knight, knightx : int, knighty : int):
    if knightx > 7 or knighty > 7:
        print("illegal move")
        return knight
    elif knightx < 0 or knighty < 0:
        print("illegal move")
        return knight
    elif knightx == knight.x + 2 and knighty == knight.y + 1:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x + 2 and knighty == knight.y - 1:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x + 1 and knighty == knight.y + 2:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x - 1 and knighty == knight.y + 2:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x - 2 and knighty == knight.y + 1:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x - 2 and knighty == knight.y - 1:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x - 1 and knighty == knight.y - 2:
        knight.x = knightx
        knight.y = knighty
    elif knightx == knight.x + 1 and knighty == knight.y - 2:
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
    if not board.isOccupied(pawn.x,pawn.y + forward):
        pseudoLegals.append([pawn.x,pawn.y + forward])
        if not board.isOccupied(pawn.x,pawn.y + (forward * 2)) and not pawn.moved:
            pseudoLegals.append([pawn.x,pawn.y + (forward * 2)])
    if board.isOccupied(*takeleft) and board.getPiece(*takeleft).color != pawn.color:
        pseudoLegals.append(takeleft)
    if board.isOccupied(*takeright) and board.getPiece(*takeright).color != pawn.color:
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
        
          

