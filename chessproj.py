
class Moves:

    def __init__(self, startPosition, NewPosition, Board):

        self.startRow = startPosition[0]
        self.startCol = startPosition[1]
        self.newRow = NewPosition[0]
        self.newCol = NewPosition[1]
        self.movedPiece = Board[self.startRow][self.startCol]
        self.capturedPiece = Board[self.newRow][self.newCol]
        

class GameState:

    def __init__(self):

        self.Board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["__","__","__","__","__","__","__","__"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"],
        ]
        self.whiteMove = True
        self.moveLog = []

    def printBoard(self):

        print("_______________________")

        for row in self.Board:

            print(" ".join(row))

        print("_______________________")

    def validPawnMoves(self, row, col, moves):

        if col == 1 or col == 8:
            pass


    def validRookMoves(self, row, col, moves):
        pass

    def validKnightMoves(self, row, col, moves):

        offsetCombos = [(-2,-1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

        for rowOffSet, colOffset in offsetCombos:

            currRow = row + rowOffSet
            currCol = col + colOffset

            if 0 <= currRow <= 7 and 0 <= currCol <= 7:

                availableMove = self.Board[currRow][currCol]

                if availableMove[0] != self.Board[row][col][0]:

                    moves.append( Moves((row, col), (currRow, currCol), self.Board) )

    def validBishopMoves(self, row, col, moves):
        pass

    def validQueenMoves(self, row, col, moves):
        pass

    def validKingMoves(self, row, col, moves):
        pass

    def validMoves(self):

        moves = []

        for row in range(0, 8):

            for col in range(0, 8):

                piece = self.Board[row][col]

                if piece == "__":

                    continue

                if (piece[0] == "w") == self.whiteMove: # Check whether piece is black or white

                    pieceType = piece[1]

                    if pieceType == "P":
                        self.validPawnMoves(row, col, moves)

                    if pieceType == "R":
                        self.validRookMoves(row, col, moves)

                    if pieceType == "N":
                        self.validKnightMoves(row, col, moves)

                    if pieceType == "B":
                        self.validBishopMoves(row, col, moves)

                    if pieceType == "Q":
                        self.validQueenMoves(row, col, moves)
                        
                    if pieceType == "K":
                        self.validKingMoves(row, col, moves)

        return moves



if __name__ == "__main__":

    game_state = GameState()
    game_state.printBoard()