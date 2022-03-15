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
		for square in [64,65,76,77]:
			if Board[square] == 'p':
				sum += 250
			elif Board[square] == 'P':
				sum += -250		
	
	return sum







def Search(Board, depth, color, MAX, MIN):

	moves = GameState.genMoves(Board, color)
	#print(f"we are in depth {depth} and our color of the node is {color}")
	#print('')
	if depth == 0:
		return [Evaluate(Board)]
	
	i = 0
	while i< len(moves):
		move = moves[i]
		takenSquare = Board[move[1]]
		startSquare = Board[move[0]]
		Board = GameState.makeMove(Board, move)
		eval = Search(Board, depth-1, not color, MAX, MIN)[0]
		Board = GameState.undoMove(Board, move, takenSquare, startSquare)
		#print(f"we checked move {GameState.readableMoves([move])} which has an evaluation of {eval}")
		
		if color: # we are white
			#print(f"we are at depth {depth}, color {color} checking if {eval} > {MAX}")
			MAX = max(MAX, eval)
			bestEval = [MAX, move]
		elif not color: # we are black
			#print(f"we are at depth {depth}, color {color} checking if {eval} < {MIN}")
			MIN = min(MIN, eval)
			bestEval = [MIN, move]
		#elif eval == bestEval[0]:
			#bestEval.append(move)
		i+=1
	return bestEval
	
	