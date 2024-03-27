





#"Import os" for ease of use of code with the interactions of the directories


import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#function to show grid in the screen
def printGrid(grid):
    for row in grid:
        print(" | ".join(row))
        print("-" * 9)

#function to show the winner it returns true if the "player g" has won and false otherwise but the function has conditions to be met in separated functions 
def winner(grid, g):
    return winner_line(grid, g) or winner_column(grid, g) or winner_diagonal(grid, g)

#if player symbol is a entire line 
def winner_line(grid, g):
    for i in range(3):
        if all(grid[i][j] == g for j in range(3)):
            return True
    return False


#if player symbol is a entire column 
def winner_column(grid, g):
    for i in range(3):
        if all(grid[j][i] == g for j in range(3)):
            return True
    return False

#if player symbol is a entire diagonal
#these codition can be met with each other except for winner_diagonal and winner_column 
def winner_diagonal(grid, g):
    if all(grid[i][i] == g for i in range(3)) or all(grid[i][2 - i] == g for i in range(3)):
        return True
    return False

#this functions is called for the grid not to be shown 2 times ... the clearscreen is not working
def no2Grids(grid):
    return all(grid[i][j] != " " for i in range(3) for j in range(3))




#function for placing the symbol of player g in row x, column y of the grid
def play(grid, x, y, g):
    if grid[x][y] == " ":
        grid[x][y] = g
        return True
    return False

#functions for saving the scores of the players in a existing file named "player_scores.txt, player_names.txt" and if the player already already exists in the file it will update their scores
def update_scores(player_scores, winners, loser):
    if winners not in player_scores:
        player_scores[winners] = 0
    if loser not in player_scores:
        player_scores[loser] = 0
    
    if winners == loser:
        player_scores[winners] += 1
    else:
        player_scores[winners] += 2
        player_scores[loser] += 0

def save_scores(player_scores, filename):
    with open(filename, "w") as file:
        for player, score in player_scores.items():
            file.write(f"{player}:{score}\n")

def load_scores(filename):
    player_scores = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                player, score = line.strip().split(":")
                player_scores[player] = int(score)
    return player_scores

def save_player_names(player_names, filename):
    with open(filename, "w") as file:
        for player, name in player_names.items():
            file.write(f"{player}:{name}\n")

def load_player_names(filename):
    player_names = {}
    if os.path.exists(filename):
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                player, name = line.strip().split(":")
                player_names[player] = name
    return player_names

#the main part of the game 
def main_game():
   
    player_scores_file = "player_scores.txt"
    player_names_file = "player_names.txt"

    player_scores = load_scores(player_scores_file)
    player_names = load_player_names(player_names_file)

    player1 = input("Enter name of Player 1: ")
    if player1 in player_names:
        player1_name = player_names[player1]
    else:
        player1_name = input(f"Enter display name for {player1}: ")
        player_names[player1] = player1_name

    player2 = input("Enter name of Player 2: ")
    if player2 in player_names:
        player2_name = player_names[player2]
    else:
        player2_name = input(f"Enter display name for {player2}: ")
        player_names[player2] = player2_name
        
    #structure of the grid a 3x3
    grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    players = {player1_name: 'X', player2_name: 'O'}
    player_index = 0

    while True:
        printGrid(grid)

        current_player = list(players.keys())[player_index]
        player_symbol = players[current_player]
        print(f"{current_player} ({player_symbol}), it's your turn.")
        
        while True:
            try:
                #the index of the palyer starts at zero(0) so the player gets to use the numbers 0, 1 and 2 only on the keyboard when the grid appears
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid position. Try again.")
                elif not play(grid, row, col, player_symbol):
                    print("Cell already taken. Try again.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if winner(grid,player_symbol):
            printGrid(grid)
            print(f"{current_player} ({player_symbol}) wins!")
            update_scores(player_scores, current_player, list(players.keys())[player_index])
            save_scores(player_scores, player_scores_file)
            break
        
        #here this part of the code the no2Grids serves for the ingame grid not to appear two times 
        elif no2Grids(grid):
                 printGrid(grid)
                 print("It's a draw!")
                 update_scores(player_scores, player1_name, player2_name)
                 save_scores(player_scores, player_scores_file)
                 break

        player_index = 1 - player_index
        
  
    save_player_names(player_names, player_names_file)
        
if __name__ == "__main__":
    main_game()
    

# GRAZIE MAESTRO LUCIANO