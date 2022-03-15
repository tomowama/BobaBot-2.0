import GameState
import SearchAndEvaluate




'''
for i in range(35):
	move = GameState.genMoves(Board, i%2==0)[0]
	takenSquare = Board[move[1]]
	startSquare = Board[move[0]]
	Board = GameState.makeMove(Board, move)
	#Board = GameState.undoMove(Board, move, takenSquare)
	eval = SearchAndEvaluate.Evaluate(Board)
	print(Board)
	print(eval)

engine = SearchAndEvaluate.Search(Board,2,True,[-2*SearchAndEvaluate.MATE], True)
print(engine)
Board = GameState.makeMove(Board,engine[1])
print(Board)

print("now it is blacks turn and we have")

engine = SearchAndEvaluate.Search(Board,2,False,[2*SearchAndEvaluate.MATE], False)
print(engine)

#piece = Board[move[0]]
#Board = Board[:move[0]] + '.' + Board[move[0]+1:]
#Board = Board[:move[1]] + piece + Board[move[1]+1:]
Board = GameState.makeMove(Board,engine[1])
print(Board)

Board = GameState.makeMove(Board, [57,67])
print(Board)
print(SearchAndEvaluate.Evaluate(Board))
'''
'''
print(Board)
print(GameState.readableMoves(GameState.genMoves(Board, False)))
print(Board)

'''


def gameLoop(depth):
	Board = GameState.BOARD
	gameOver = False
	move = 0
	while not gameOver:
		engine = SearchAndEvaluate.Search(Board, depth, True, [-2*SearchAndEvaluate.MATE], True)
		print(f"evaluation is {engine[0]} and the move is {GameState.readableMoves([engine[1]])}")
		Board = GameState.makeMove(Board, engine[1])
		print(Board)
		if engine[0] < -10000:
			print(f"Game over")
			break
		elif engine[0] > 10000:
			print(f"Game over")
			break
		engine = SearchAndEvaluate.Search(Board, depth, False, [2*SearchAndEvaluate.MATE], False)
		print(f"evaluation is {engine[0]} and the move is {GameState.readableMoves([engine[1]])}")
		Board = GameState.makeMove(Board, engine[1])
		print(Board)		
		if engine[0] < -10000:
			print(f"Game over")
			break
		elif engine[0] > 10000:
			print(f"Game over")
			break		
		
		move +=1
	
	
gameLoop(3)


