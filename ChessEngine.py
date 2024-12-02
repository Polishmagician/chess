class GameState():
    def __init__(self):

        #First character is color of the piece, second character is type of the piece
        # "--" represents an empty space with no piece
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]]
        self.whiteToMove = True
        self.movelog = []
class piece():
    def __init__(self,color,position):
        self.color = color
        self.moved = False
        self.position = position
class pawn(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        pawn.piece = "p"
        pawn.firstrank = True
class rook(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        rook.piece = "R"
        rook.castle = True
class knight(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        knight.piece = "K"
class bishop(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        bishop.piece = "B"
class queen(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        queen.piece = "Q"
class king(piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        king.piece = "K"
        king.castle = True
