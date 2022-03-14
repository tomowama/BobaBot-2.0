####### THIS IS THE BOARD AND BASIC RULES AND LOGIC OF THE GAME/ GAMESTATE ################

## BOARD IS A STRING WITH PADDING, white is the capatilized letters 

BOARD = (
  "           \n" # 0 -11 
  "           \n" # 12-23
  "  RNBQKBNR \n" # 24-35
  "  PPPPPPPP \n" # 36-47
  "  ........ \n" # 48-59
  "  ........ \n" # 60-71
  "  pppppppp \n" # 72-83
  "  rnbqkbnr \n" # 84 - 95
  "           \n"#  96 - 107
  "           \n" # 108-119
)
# Directions  used for moving later. 
N, E, S, W = -12, 1, 12, 1
#print(BOARD)
captures = ['R','N','B','Q','K','P']


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
  pawnStartRow = range(74,82)
  if not color:
    forward = 12
    pawnStartRow = range(38,46)
    for i in range(25,94):
      
      if tempBoard[i] in captures: #our peice is black so make white
        tempBoard = tempBoard[:i] + tempBoard[i].lower() + tempBoard[i+1:]
      elif tempBoard[i].upper() in captures: #white make black
        tempBoard = tempBoard[:i] + tempBoard[i].upper() + tempBoard[i+1:]
  #print(tempBoard)
  for i in range(25,94):
    if tempBoard[i] == 'p':
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
        if n in [2*E,2*W]:
          for x in [N,S]:
            if tempBoard[i + n + x] in captures or tempBoard[i + n + x] == '.':
              legalMoves.append([i,i+n+x])
  return legalMoves


def makeMove(Board, move):
  piece = Board[move[0]]
  Board = Board[:move[0]] + '.' + Board[move[0]+1:]
  Board = Board[:move[1]] + piece + Board[move[1]+1:]
  return Board

  





for i in range(20):
  BOARD = makeMove(BOARD, genMoves(BOARD, i%2==0)[0])
  print(BOARD)
    
    

