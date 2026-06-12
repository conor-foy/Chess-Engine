
class Moves:

    def __init__(self, startPosition, NewPosition, Board):

        self.startRow = startPosition[0]
        self.startCol = startPosition[1]
        self.newRow = NewPosition[0]
        self.newCol = NewPosition[1]
        self.movedPiece = Board[self.startRow][self.startCol]
        self.capturedPiece = Board[self.newRow][self.newCol]

    # makes output readable and not memory addresses
    def __str__(self):
        
        return f"{self.movedPiece}: ({self.startRow},{self.startCol}) -> ({self.newRow},{self.newCol})"
    
    # for lists
    def __repr__(self):

        return self.__str__()

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

        self.whiteKingPosition = (7, 4)
        self.blackKingPosition = (0, 4)


    def makeMove(self, move):

        if move.movedPiece == "wK":

            self.whiteKingPosition = (move.newRow, move.newCol)

        elif move.movedPiece == "bK":

            self.blackKingPosition = (move.newRow, move.newCol)
        
        self.Board[move.startRow][move.startCol] = "__"
        self.Board[move.newRow][move.newCol] = move.movedPiece

        self.moveLog.append(move)
        self.whiteMove = not self.whiteMove # swap move colour


    def undoMove(self):

        lastMove = self.moveLog.pop()

        if lastMove.movedPiece == "wK":

            self.whiteKingPosition = (lastMove.startRow, lastMove.startCol)
            
        elif lastMove.movedPiece == "bK":
                
            self.blackKingPosition = (lastMove.startRow, lastMove.startCol)

        self.Board[lastMove.newRow][lastMove.newCol] = lastMove.capturedPiece
        self.Board[lastMove.startRow][lastMove.startCol] = lastMove.movedPiece

        self.whiteMove = not self.whiteMove


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
        colour = self.Board[row][col][0]

        for rowOffSet, colOffset in offsetCombos:

            if 0 <= row + rowOffSet <= 7 and 0 <= col + colOffset <= 7:

                position = self.Board[row + rowOffSet][col + colOffset]

                if position == "__" or position[0] != colour:

                    moves.append( Moves((row, col), (row + rowOffSet, col + colOffset), self.Board) )


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

                elif position != "__" and position[0] != colour:

                    moves.append(Moves( (startRow, startCol), (row + rowChange, col + colChange), self.Board))
                    break
                
                else:

                    break

                row += rowChange
                col += colChange


    def validQueenMoves(self, row, col, moves):
        
        self.validRookMoves(row, col, moves)
        self.validBishopMoves(row, col, moves)


    def validKingMoves(self, row, col, moves):

        offsetCombos = [(-1,0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
        colour = self.Board[row][col][0]

        for rowChange, colChange in offsetCombos:

            if 0 <= row + rowChange <= 7 and 0 <= col + colChange <= 7:

                position = self.Board[row + rowChange][col + colChange]

                if position == "__" or position[0] != colour:

                    moves.append(Moves( (row, col), (row + rowChange, col + colChange), self.Board))


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

                    elif pieceType == "R":
                        self.validRookMoves(row, col, moves)

                    elif pieceType == "N":
                        self.validKnightMoves(row, col, moves)

                    elif pieceType == "B":
                        self.validBishopMoves(row, col, moves)

                    elif pieceType == "Q":
                        self.validQueenMoves(row, col, moves)
                        
                    elif pieceType == "K":
                        self.validKingMoves(row, col, moves)

        return moves


    def attackedSquare(self, row, col):

        # change colour
        self.whiteMove = not self.whiteMove

        enemyMoves = self.validMoves()

        self.whiteMove = not self.whiteMove
        
        for move in enemyMoves:

            if (move.newRow, move.newCol) == (row, col):
                
                return True
            
        return False


    def inCheck(self, white):

        if white:

            return self.attackedSquare(self.whiteKingPosition[0], self.whiteKingPosition[1])
        
        else:

            return self.attackedSquare(self.blackKingPosition[0], self.blackKingPosition[1])
        

    def safeMoves(self):
        
        moves = self.validMoves()
        colourTurn = self.whiteMove
        safeMovesList = []

        for move in moves:

            self.makeMove(move) # try move
            
            # swap turn back before checking
            self.whiteMove = not self.whiteMove

            if not self.inCheck(colourTurn):

                # move does not lead to us being in check
                safeMovesList.append(move)

            self.whiteMove = not self.whiteMove

            # only checking for current state of the board so undo
            self.undoMove()
        
        # all safe moves
        return safeMovesList


    def isCheckMate(self):

        if self.inCheck(self.whiteMove) and len(self.safeMoves()) == 0:

            return True
        
        return False


    def isStaleMate(self):

        if not self.inCheck(self.whiteMove) and len(self.safeMoves()) == 0:

            return True
        
        return False
        
if __name__ == "__main__":

    gameState = GameState()
    