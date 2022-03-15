####### THIS IS THE BOARD AND BASIC RULES AND LOGIC OF THE GAME/ GAMESTATE ################

## BOARD IS A STRING WITH PADDING, black is the capatilized letters

BOARD = (
  "           \n" # 0 -11
  "           \n" # 12-23
  "  RNBQKBNR \n" # 24-35
  "  PPPPPPPP \n" # 36-47
  "  ........ \n" # 48-59
  "  ........ \n" # 60-71
  "  ........ \n" # 72-83
  "  ........ \n" # 84-95
  "  pppppppp \n" # 96-107
  "  rnbqkbnr \n" # 108-119
  "           \n"#  
  "           \n" # 
)
# Directions  used for moving later.
N, E, S, W = -12, 1, 12, -1
#print(BOARD)
captures = ['R','N','B','Q','K','P']

rows = [range(110,118),range(98,106),range(86,94),range(74,82), range(62,70), range(50,58), range(38,46),range(26,34)]

columns = [range(26,120, 12), range(27,121,12), range(28,122,12), range(29,123,12), range(30,124,12), range(31,125,12), range(32,126,12), range(33,127,12)]


col = {
	0: 'a',
	1: 'b',
	2: 'c',
	3: 'd',
	4: 'e',
	5: 'f',
	6: 'g',
	7: 'h'
}



def moveInLine(board, pos, northSouth, eastWest, r):
	legalMoves = []
	for i in range(1, r):
		if board[pos + (i*N*northSouth) + (i*E*eastWest)] in captures:
			legalMoves.append([pos, pos + (i*N*northSouth) + (i*E*eastWest)])
			break
		elif board[pos + (i*N*northSouth) + (i*E*eastWest)] == ".":
			legalMoves.append([pos, pos + (i*N*northSouth) + (i*E*eastWest)])
		else:
			break
	return legalMoves
	
def genMoves(Board, color):
	legalMoves = []
	tempBoard = Board[:]
	forward = -12
	pawnStartRow = range(98,106)

	if not color: # we are black
		forward = 12
		pawnStartRow = range(38,46)
		for i in range(26,118):
			if tempBoard[i] == ' ' or tempBoard[i] == '.':
				#print('if')
				pass
			elif tempBoard[i] in captures: #our peice is black so make white
				#print('elif')
				tempBoard = tempBoard[:i] + tempBoard[i].lower() + tempBoard[i+1:]
			elif tempBoard[i].upper() in captures:
				#print('else')
				#print(f"our element is {tempBoard[i]}")
				tempBoard = tempBoard[:i] + tempBoard[i].upper() + tempBoard[i+1:]
			else:
				pass
	#print(f"our temp board is {tempBoard}")
	for i in range(26,118):
		if tempBoard[i] == '.' or tempBoard[i] == ' ':
			pass
		elif tempBoard[i] == 'p':
			if tempBoard[i + forward] == '.' and tempBoard[i + 2*forward] == '.' and i in pawnStartRow:
				legalMoves.append([i,i+forward])
				legalMoves.append([i,i+2*forward])
			elif tempBoard[i + forward] == '.':
				legalMoves.append([i,i+forward])
			if tempBoard[i + forward + E] in captures:
				legalMoves.append([i,i+forward + E])
			if tempBoard[i+forward + W] in captures:
				legalMoves.append([i,i+forward+W])
		elif tempBoard[i] == 'q':
			qmoves = [moveInLine(tempBoard, i, 1,0, 8),
			moveInLine(tempBoard, i, -1, 0, 8),
			moveInLine(tempBoard, i, 0, 1, 8),
			moveInLine(tempBoard, i, 0, -1, 8),
			moveInLine(tempBoard, i, 1, 1, 8),
			moveInLine(tempBoard, i, -1, 1, 8),
			moveInLine(tempBoard, i, 1, -1, 8),
			moveInLine(tempBoard, i, -1, -1, 8)]
			for moves in qmoves:
				for move in moves:
					legalMoves.append(move)
		elif tempBoard[i] == 'b':
			bmoves = [
			moveInLine(tempBoard, i, 1, 1, 8),
			moveInLine(tempBoard, i, -1, 1, 8),
			moveInLine(tempBoard, i, 1, -1, 8),
			moveInLine(tempBoard, i, -1, -1, 8)
			]
			for moves in bmoves:
				for move in moves:
					legalMoves.append(move)
		elif tempBoard[i] == 'r':
			rmoves = [
			moveInLine(tempBoard, i, 1, 0, 8),
			moveInLine(tempBoard, i, -1, 0, 8),
			moveInLine(tempBoard, i, 0, 1, 8),
			moveInLine(tempBoard, i, 0, -1, 8)
			]
			for moves in rmoves:
				for move in moves:
					legalMoves.append(move)
		elif tempBoard[i] == 'k':
			kmoves = [moveInLine(tempBoard, i, 1,0, 2),
			moveInLine(tempBoard, i, -1, 0, 2),
			moveInLine(tempBoard, i, 0, 1, 2),
			moveInLine(tempBoard, i, 0, -1, 2),
			moveInLine(tempBoard, i, 1, 1, 2),
			moveInLine(tempBoard, i, -1, 1, 2),
			moveInLine(tempBoard, i, 1, -1, 2),
			moveInLine(tempBoard, i, -1, -1, 2)]
			for moves in kmoves:
				for move in moves:
					legalMoves.append(move)
		elif tempBoard[i] == 'n':
			for n in [2*N,2*S,2*E,2*W]:
				if n in [2*N,2*S]:
					for x in [E,W]:
						if tempBoard[i + n + x] in captures or tempBoard[i + n + x] == '.':
							legalMoves.append([i,i+n+x])
				else:
					for x in [N,S]:
						if tempBoard[i + n + x] in captures or tempBoard[i + n + x] == '.':
							legalMoves.append([i,i+n+x])
	return legalMoves
	
	
def makeMove(Board, move):
	blackpromoteRow = range(110,118)
	whitepromoteRow = range(26,34)
	piece = Board[move[0]]
	if piece == 'p' and move[1] in whitepromoteRow:
			Board = Board[:move[0]] + '.' + Board[move[0]+1:]
			Board = Board[:move[1]] + 'q' + Board[move[1]+1:]
			return Board
	elif piece	== 'P' and move[1] in blackpromoteRow:
			Board = Board[:move[0]] + '.' + Board[move[0]+1:]
			Board = Board[:move[1]] + 'Q' + Board[move[1]+1:]
			return Board
	Board = Board[:move[0]] + '.' + Board[move[0]+1:]
	Board = Board[:move[1]] + piece + Board[move[1]+1:]
	
	return Board

def undoMove(Board, move, takenSquare, startSquare):
	Board = Board[:move[1]] + takenSquare + Board[move[1] +1:]
	Board = Board[:move[0]] + startSquare + Board[move[0] +1:]
	return Board
	
	
def readableMoves(moves):
	readableMoves = []
	startRow = 0
	endRow = 0
	startCol = ''
	endCol = ''
	for move in moves:
		for i in range(0,8):
			if move[0] in rows[i]:
				startRow = i+1
			if move[1] in rows[i]:
				endRow = i+1
		for i in range(0,8):
			if move[0] in columns[i]:
				startCol = col[i]
			if move[1] in columns[i]:
				endCol = col[i]
		readableMoves.append([startCol + str(startRow), endCol + str(endRow)])
	
	return readableMoves
	
	
	
	
'''
for i in range(20):
	move = genMoves(BOARD, i%2==0)[0]
	takenSquare = BOARD[move[1]]
	BOARD = makeMove(BOARD, move)
	BOARD = undoMove(BOARD, move, takenSquare)
	
	print(BOARD)
'''