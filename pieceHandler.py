class pawn():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "pawn"
        self.typeShort = "p"
        self.material = 1
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}
        
class knight():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "knight"
        self.typeShort = "h"
        self.material = 3
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}
        
class bishop():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "bishop"
        self.typeShort = "b"
        self.material = 3
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}

        
class rook():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "rook"
        self.typeShort = "r"
        self.material = 5
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}
        
class queen():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "queen"
        self.typeShort = "q"
        self.material = 9
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}
 
class king():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "pawn"
        self.typeShort = "k"
        self.material = 999
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort, "material": self.material}
