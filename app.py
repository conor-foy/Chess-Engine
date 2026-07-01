from flask import Flask, jsonify, request, send_from_directory
from chessLogic import GameState, Moves

gameState =  GameState()
app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("templates", "index.html")

@app.route("/board")

def board():

    return jsonify({
        "board": gameState.Board,
        "whiteMove": gameState.whiteMove
    })

@app.route("/move", methods = ["POST"])

def move():

    data = request.json
    start = tuple(data["start"])
    end = tuple(data["end"])

    legalMoves = gameState.safeMoves()

    currMove = None

    for move in legalMoves:

        if (move.startRow, move.startCol) == start and (move.newRow, move.newCol) == end:

            currMove = move
            break

    if currMove == None:

       return jsonify({"error": "illegal move", "board": gameState.Board, "whiteMove": gameState.whiteMove})
    
    gameState.makeMove(currMove)

    return jsonify({
        "board": gameState.Board,
        "whiteMove": gameState.whiteMove
    })


if __name__ == "__main__":

    app.run(debug = True, threaded = True)