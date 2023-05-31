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

    return knight