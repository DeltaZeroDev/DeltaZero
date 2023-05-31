class pawn():
    def __init__(self, x, y, color) -> None:
        self.x = x
        self.y = y
        self.type = "pawn"
        self.typeShort = "p"
        self.color = color
        self.moved = False

    def __dict__(self) -> dict:
        return {"x": self.x, "y": self.y, "type": self.type, "color": self.color, "moved": self.moved, "typeShort": self.typeShort}