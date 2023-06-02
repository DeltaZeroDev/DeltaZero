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
         bishop.x = bishopx
         bishop.y = bishopy

    else:
        print("illegal move")
    return bishop

def pawnmove(pawn : ph.pawn, pawny : int, pawnx : int, board):
    pseudoLegals = []
    pseudoLegals.append([pawn.y + 1,pawn.x])
    if not board.isOccupied(*pseudoLegals[-1]):
        pseudoLegals.append([pawn.y + 2,pawn.x])
    
    return pawn

        
          

