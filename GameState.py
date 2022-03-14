####### THIS IS THE BOARD AND BASIC RULES AND LOGIC OF THE GAME/ GAMESTATE ################

## BOARD IS A STRING WITH PADDING, white is the capatilized letters 

BOARD = (".........\n" #0-9
         ".........\n" #10-19
         ".RNBQKBNR\n" #20-29
         ".PPPPPPPP\n" #30-39
         ".........\n" #40-49
         ".........\n" #50-59
         ".pppppppp\n" #60-69
         ".rnbqkbnr\n" #70-70
         ".........\n" #80-89
         ".........\n" #90-99
        )
# Directions  used for moving later. 
N, E, S, W = 10, 1, -10, -1 



