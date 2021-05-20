import os
import sys

BANNER = '''
_________                                     __    ___________                 
\_   ___ \  ____   ____   ____   ____   _____/  |_  \_   _____/___  __ _________ 
/    \  \/ /  _ \ /    \ /    \_/ __ \_/ ___\   __\  |    __)/  _ \|  |  \_  __ \ 
\     \___(  <_> )   |  \   |  \  ___/\  \___|  |    |   |  (  <_> )  |  /|  | \/
 \________/\____/|___|__/___|__/\_____>\_____>__|    \___|   \____/|____/ |__|


'''
ROWS = 6
COLUMNS = 7
player_turn = 0
choice = 0
row = 0
game_over = False

# Creates a blank grid for a new game
def new_grid():
    grid = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
    return grid

# Prints each row in the grid's list, but in reverse row order, so the 0 row will be on the bottom
def print_grid(grid):
    for row in range(len(grid)):
        print((" " * 28) + str(grid[-(row + 1)]))
    print("\n")

# Delete previous line in terminal
def delete_line():
    sys.stdout.write('\x1b[1A') # Move cursor up one line
    sys.stdout.write('\x1b[2K') # Delete line

# Ensure the selected column is a valid choice
def is_choice_valid(choice):
    try:
        if choice -1 >= 0 and choice -1 < 8:
            if grid[ROWS - 1][choice -1] == 0:
                if choice in range(1, COLUMNS + 1):
                    return
                else:
                    delete_line()
                    delete_line()
                    choice = int(input((" " * 24) + "*** INVALID COLUMN NUMBER ***\nPlayer " + str(player_turn + 1) + ", please enter a valid column number (1-7):"))
                    is_choice_valid(choice)
            else:
                delete_line()
                delete_line()
                choice = int(input((" " * 24) + f"*** NO MORE OPEN SPACES IN COLUMN {choice} ***\nPlayer " + str(player_turn + 1) + ", please enter a valid column number (1-7):"))
                is_choice_valid(choice)
        else:
            delete_line()
            delete_line()
            choice = int(input((" " * 24) + "*** COLUMN NUMBER TOO LOW ***\nPlayer " + str(player_turn + 1) + ", please enter a valid column number (1-7):"))
            is_choice_valid(choice)
    except:
        delete_line()
        delete_line()
        choice = int(input((" " * 24) + "*** COLUMN NUMBER TOO HIGH ***\nPlayer " + str(player_turn + 1) + ", please enter a valid column number (1-7):"))
        is_choice_valid(choice)

def find_open_row(choice):
    for row in range(ROWS):
        if grid[row][choice -1] == 0:
            return row

def place_piece(row, choice):
    grid[row][choice - 1] = player_turn + 1

def check_win():
    pass

# Refresh grid with new selection
def refresh_grid():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
    print_grid(grid)

# Swap player turn
def swap_players():
    global player_turn
    player_turn = (player_turn + 1) % 2
    
if __name__ == "__main__":
   # Start the game
   grid = new_grid()
   refresh_grid()

   while game_over == False:
      choice = int(input("Player " + str(player_turn + 1) + ", please choose a column (1-7):"))
      is_choice_valid(choice)
      row = find_open_row(choice)
      place_piece(row, choice)
      refresh_grid()
      check_win()
      swap_players()
    
