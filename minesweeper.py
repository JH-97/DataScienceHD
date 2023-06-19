# A program that calculated the number of adjacent 'mines' in a 2D list

# import modules
import random

# Function calculates number of mines adjacent to position in grid 
# given by arguement
def adjacent(row, col):
    count = 0
    for row_modifier in range(3):
        for col_modifier in range(3):
            current_row = row + (row_modifier -1)
            current_col = col + (col_modifier - 1)
            if current_col >= 0 and current_row >=0 and current_row <= num_of_rows-1 and current_col <= num_of_columns-1:
                if grid[current_row][current_col] == "#":
                    count += 1
    return count
    
# Create 2D list of user selected size
while True:
    try:
        num_of_rows = int(input("Enter the number of rows: "))
        num_of_columns = int(input("Enter the num of cols: "))
        if num_of_columns > 0 and num_of_rows > 0:
            grid = [[None] * num_of_columns for _ in range(num_of_rows)]
            break
        else:
            print("You must have at least 1 row and column. Try again.")
            continue
    except:
        print("You must enter whole positive integers e.g. try typing '2' instead of 'two'.")    

# Randomly populate grid with mines
grid_char = ["#", "-"]
for row in range(num_of_rows):
    for col in range(num_of_columns):
        grid[row][col] = random.choice(grid_char)

# check adjectent space loop
for row in range(num_of_rows):
    for col in range(num_of_columns):
        if grid[row][col] == "-":
            grid[row][col] = adjacent(row, col)


# Output final minesweeper grid in a more readable format
for row in grid:
    print(*row, sep='| ')
    
