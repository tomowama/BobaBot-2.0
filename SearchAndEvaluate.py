import GameState



blackPieces = ['P','N','B','R','Q','K']
MATE= 1000000
blackValues = {
	'P': -100,
	'N': -300,
	'B': -325,
	'R': -521,
	'Q': -915,
	'K': -MATE
}




def Evaluate(Board):
	sum = 0
	for i in range(25,118): # this is the whole legal moves of the board
		if Board[i] == '.' or Board[i] == ' ':
			pass
		elif Board[i] in blackPieces: # the piece is black
			sum += blackValues[Board[i]]
		elif Board[i].upper() in blackPieces: # the piece is white
			sum += -1 * blackValues[Board[i].upper()]			
	
	return sum







def Search(Board, depth, color, bestEval, whiteOrBlack):

	moves = GameState.genMoves(Board, color)
	
	if depth == 0:
		return [Evaluate(Board)]
	
	i = 0
	added = False
	while i< len(moves):
		move = moves[i]
		takenSquare = Board[move[1]]
		startSquare = Board[move[0]]
		Board = GameState.makeMove(Board, move)
		eval = Search(Board, depth-1, not color, bestEval, whiteOrBlack)[0]
		Board = GameState.undoMove(Board, move, takenSquare, startSquare)
		
		if (eval > bestEval[0]) and whiteOrBlack:
			bestEval = [eval, move]
		elif (eval < bestEval[0]) and not whiteOrBlack:
			bestEval = [eval, move]
		#elif eval == bestEval[0]:
			#bestEval.append(move)
		i+=1
	return bestEval
	
	