import random

def soduku(grid):

    for i in range(9):
        # To check row in grid
        if len(set(grid[i])) != 9:
            return False
        # To check columns in grid
        if len(set([row[i] for row in grid])) != 9:
            return False
    # To check 3x3
    for i in range(0,9,3):
        for j in range(0,9,3):
            box = grid[i][j:j+3]+grid[i+1][j:j+3]+grid[i+2][j:j+3]
            if len(set(box)) != 9:
                return False
        
    return True

# Creating function to check the above function performs in correct manner
def gridS():
    grid = []
    n = 0
    for i in range(9):
        row =[]
        for j in range(9):
            row.append(n)
            n+=1
        grid.append(row)
    return grid

sodukuGrid = gridS()

print(soduku(sodukuGrid))