import boardHandler as bh
import pieceHandler as ph

def knightmove(knight : ph.knight):

    knightx = int(input("x coords of where trying to move"))
    knighty = int(input("y coord of where trying to move"))

    if knightx == knight.x + 2 and knighty == knight.y + 1:
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
    elif knightx > 7 or knighty > 7:
        print("illegal move")
    
    else:
        print("illegal move")
