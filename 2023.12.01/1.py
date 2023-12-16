import chess


class Turn:
    def __init__(self, piece: chess.Piece, start_square: chess.Square, 
                end_square: chess.Square):
        self.piece = piece
        self.start_square = start_square
        self.end_square = end_square


class Game:
    def __init__(self, chessboard: chess.Chessboard):
        self.chessboard = chessboard
        self.history = []

    def make_move(self, piece: chess.Piece, start_square: chess.Square, 
                end_square: chess.Square):
        piece.move(end_square)
        self.history.append(Turn(piece, start_square, end_square))

    def print_history(self):
        for i, turn in enumerate(self.history, start=1):
            print(f"{i}. {turn.piece} moved from {turn.start_square}\
                to {turn.end_square}")

    def undo_move(self, steps: int):
        for _ in range(steps):
            last_turn = self.history.pop()
            last_turn.piece.move(last_turn.start_square)




