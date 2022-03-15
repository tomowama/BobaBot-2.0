import GameState
import SearchAndEvaluate


'''
Board = GameState.BOARD
max = -2*SearchAndEvaluate.MATE
min = 2*SearchAndEvaluate.MATE
for i in range(35):
	move = GameState.genMoves(Board, i%2==0)[0]
	takenSquare = Board[move[1]]
	startSquare = Board[move[0]]
	Board = GameState.makeMove(Board, move)
	#Board = GameState.undoMove(Board, move, takenSquare)
	eval = SearchAndEvaluate.Evaluate(Board)
	print(Board)
	
engine = SearchAndEvaluate.Search(Board, 2, True, max, min)	
Board = GameState.makeMove(Board, engine[1])
print(Board)
'''


def gameLoop(depth):
	max = -2*SearchAndEvaluate.MATE
	min = 2*SearchAndEvaluate.MATE
	Board = GameState.BOARD
	gameOver = False
	move = 0
	while not gameOver:
		engine = SearchAndEvaluate.Search(Board, depth, True, max, min)
		print(f"evaluation is {engine[0]} and the move is {GameState.readableMoves([engine[1]])}")
		Board = GameState.makeMove(Board, engine[1])
		print(Board)
		eval = SearchAndEvaluate.Evaluate(Board)
		if eval < -10000:
			print(f"Game over")
			break
		elif eval > 10000:
			print(f"Game over")
			break
		engine = SearchAndEvaluate.Search(Board, depth, False, max, min)
		print(f"evaluation is {engine[0]} and the move is {GameState.readableMoves([engine[1]])}")
		Board = GameState.makeMove(Board, engine[1])
		print(Board)		
		eval = SearchAndEvaluate.Evaluate(Board)
		if eval < -10000:
			print(f"Game over")
			break
		elif eval > 10000:
			print(f"Game over")
			break
		
		move +=1
	
	
gameLoop(3)


