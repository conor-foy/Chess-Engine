
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

        position = self.Board[row][col]
        colour = self.Board[row][col][0]

        # en passant logic later
        # if piece on left or right is pawn and that pawn made 
        # a two move then home pawn can move diagonally behind it and other pawn deleted

        # white moves
        if colour == "w":
            # possible two space move for white
            if row == 6 :

                if self.Board[row - 2][col] == "__" and self.Board[row - 1][col] == "__":

                    moves.append( Moves((row, col), (row - 2, col), self.Board) )

            if self.Board[row - 1][col] == "__":

                moves.append( Moves((row, col), (row - 1, col), self.Board) )

            if col == 0 and self.Board[row - 1][col + 1][0] == "b":

                moves.append( Moves((row, col), (row - 1, col + 1), self.Board) )

            if col == 7 and self.Board[row - 1][col - 1][0] == "b":

                moves.append( Moves((row, col), (row - 1, col - 1), self.Board) )

            if col in range(1, 7):

                if self.Board[row - 1][col - 1][0] == "b":

                    moves.append( Moves((row, col), (row - 1, col - 1), self.Board) )
                
                if self.Board[row - 1][col + 1][0] == "b":

                    moves.append( Moves((row, col), (row - 1, col + 1), self.Board) )

        # black moves
        if colour == "b":
            # possible two space move for black
            if row == 1 :

                if self.Board[row + 2][col] == "__" and self.Board[row + 1][col] == "__":

                    moves.append( Moves((row, col), (row + 2, col), self.Board) )

            if self.Board[row + 1][col] == "__":

                moves.append( Moves((row, col), (row + 1, col), self.Board) )

            if col == 0 and self.Board[row + 1][col + 1][0] == "w":

                moves.append( Moves((row, col), (row + 1, col + 1), self.Board) )

            if col == 7 and self.Board[row + 1][col - 1][0] == "w":

                moves.append( Moves((row, col), (row + 1, col - 1), self.Board) )

            if col in range(1, 7):

                if self.Board[row + 1][col - 1][0] == "w":

                    moves.append( Moves((row, col), (row + 1, col - 1), self.Board) )
                
                if self.Board[row + 1][col + 1][0] == "w":

                    moves.append( Moves((row, col), (row + 1, col + 1), self.Board) )



    def validRookMoves(self, row, col, moves):

        colour = self.Board[row][col][0]
        
        # row case up
        for i in range(row + 1, 8):

            position = self.Board[i][col]

            if position == "__":
                
                moves.append( Moves((row, col), (i, col), self.Board) )

            elif position[0] != colour:

                moves.append( Moves((row, col), (i, col), self.Board) )
                break

            # same colour
            else:

                break

        
        # row case down
        for i in range(row - 1, -1, -1):

            position = self.Board[i][col]

            if position == "__":
                
                moves.append( Moves((row, col), (i, col), self.Board) )

            elif position[0] != colour:

                moves.append( Moves((row, col), (i, col), self.Board) )
                break

            # same colour
            else:

                break

        # col case right
        for j in range(col + 1, 8):

            position = self.Board[row][j]

            if position == "__":
                
                moves.append( Moves((row, col), (row, j), self.Board) )

            elif position[0] != colour:

                moves.append( Moves((row, col), (row, j), self.Board) )
                break

            # same colour
            else:

                break

        # col case left
        for j in range(col - 1, -1, -1):

            position = self.Board[row][j]

            if position == "__":
                
                moves.append( Moves((row, col), (row, j), self.Board) )

            elif position[0] != colour:

                moves.append( Moves((row, col), (row, j), self.Board) )
                break

            # same colour
            else:

                break
        

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
        
        diagonals = [(1, -1), (1, 1), (-1, -1), (-1, 1)]
        startRow = row
        startCol = col
        colour = self.Board[row][col][0]

        for rowChange, colChange in diagonals:

            row = startRow
            col = startCol

            while 0 <= row + rowChange <= 7 and 0 <= col + colChange <= 7:

                position = self.Board[row + rowChange][col + colChange]

                if position == "__":

                    moves.append(Moves( (startRow, startCol), (row + rowChange, col + colChange), self.Board))

                if position != "__" and position[0] != colour:

                    moves.append(Moves( (startRow, startCol), (row + rowChange, col + colChange), self.Board))
                    break
                
                if position[0] == colour:

                    break

                row += rowChange
                col += colChange



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

    gameState = GameState()
    gameState.printBoard()
    
    moves = []
    