from random import randint 
         
# Innitializing the board as a 5x5 grid of "O"   
board = [["O"] * 5 for _ in range(5)]       
                    
def print_board(board):         
    """Print the board."""                
    for row in board:     
        print (" ".join(row))       
       
def random_row(board):
    """Returning a random row index.""" 
    return randint(0, len(board[0]) - 1) 
 
def random_col(board):
    """Returning a random column index."""
    return randint(0, len(board[0]) - 1)

# Randomly place the battleship
ship_row = random_row(board)
ship_col = random_col(board)

print (ship_row)
print (ship_col)

# Main game loop
for turn in range(4):
    print ("Turn", turn + 1)
    guess_row = int(input("Guess Row: "))
    guess_col = int(input("Guess Col: "))

    # Checking if the guess is correct
    if guess_row == ship_row and guess_row == ship_col:
        print ("Congratulations! You sank my battleship")
        break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
            print ("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
        if turn == 3:
            print("Game Over!")
        print_board(board)
