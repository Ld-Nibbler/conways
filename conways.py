# Conway's game of life
import random, time, copy, os, keyboard
WIDTH = 60
HEIGHT = 20

# Function for random cells filling
def randFilling():
    # Create a list of list for the cells
    nextCells = []
    for x in range(WIDTH):
        column = [] # Create a new column
        for y in range(HEIGHT):
            if random.randint(0,1) == 0:
                column.append("֍") # Add a living cell
            else:
                column.append(" ") # Add a dead cell
        nextCells.append(column) # nextCells is a list of column lists
    return nextCells


def mainLoop(nextCells):        
    # Mine program loop
    while True:
        # print("\n\n\n\n\n")
        os.system('cls' if os.name == 'nt' else 'clear')
        currentCells = copy.deepcopy(nextCells)
        for xs in range(WIDTH+2):
            print('-', end='')
        print()
        # Print currentCells on the screen
        for y in range(HEIGHT):
            print('|', end='')
            for x in range(WIDTH):
                print(currentCells[x][y], end="") # Printing # or a space
            print('|') # Printing a new line at the end of the row

        # Calculate the next step's cells, based on the current step's cells:
        for x in range(WIDTH):
            for y in range(HEIGHT):
                #Get neighboring coordinates
                # % WIDTH ensures leftCoord always between 0 and WIDTH - 1
                leftCoord  = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                aboveCoord = (y - 1) % HEIGHT
                belowCoord = (y + 1) % HEIGHT
                # Count number of living neighbors:
                numNeighbors = 0
                if currentCells[leftCoord][aboveCoord] == '֍':
                    numNeighbors += 1 # Top-left neighbor is alive.
                if currentCells[x][aboveCoord] == '֍':
                    numNeighbors += 1 # Top neighbor is alive.
                if currentCells[rightCoord][aboveCoord] == '֍':
                    numNeighbors += 1 # Top-right neighbor is alive.
                if currentCells[leftCoord][y] == '֍':
                    numNeighbors += 1 # Left neighbor is alive.
                if currentCells[rightCoord][y] == '֍':
                    numNeighbors += 1 # Right neighbor is alive.
                if currentCells[leftCoord][belowCoord] == '֍':
                    numNeighbors += 1 # Bottom-left neighbor is alive.
                if currentCells[x][belowCoord] == '֍':
                    numNeighbors += 1 # Bottom neighbor is alive.
                if currentCells[rightCoord][belowCoord] == '֍':
                    numNeighbors += 1 # Bottom-right neighbor is alive.
                # Set cell based on Conway's Game of Life rules:
                if currentCells[x][y] == '֍' and (numNeighbors == 2 or numNeighbors == 3):
                    # Living cells with 2 or 3 neighbors stay alive:
                    nextCells[x][y] = '֍'
                elif currentCells[x][y] == ' ' and numNeighbors == 3:
                    # Dead cells with 3 neighbors become alive:
                    nextCells[x][y] = '֍'
                else:
                    # Everything else dies or stays dead:
                    nextCells[x][y] = ' '
        for xs in range(WIDTH+2):
            print('-', end='')
        print('\n\n')
        time.sleep(1) # Add a 1-second pause to reduce flickering.


def userDrawing():
    pattern = []
    pattern.append((20,10))
    pattern.append((21,11))
    pattern.append((21,12))
    pattern.append((20,12))
    pattern.append((19,12))

    keyboard.hook(print_pressed_keys)
    keyboard.wait()
    
    
    #return pattern

def userFilling():    
    # figure = userDrawing()
    userDrawing()
    nextCells = []
    for x in range(WIDTH):
        column = [] # Create a new column
        for y in range(HEIGHT):        
            if (x,y) in figure:
                column.append("֍") # Add a living cell
                # print('X',end='')
            else:
                column.append(" ") # Add a dead cell
                # print('.',end='')
        nextCells.append(column)
        # print()
    return nextCells


setConditions = ''
while setConditions != 'R' or setConditions != 'U':
    print('How do you wish to set start conditions? (R - randomly, U - user settings):',end='')
    setConditions = input()
    if setConditions == 'R':
        cells = randFilling()
        mainLoop(cells) 
    elif setConditions == 'U':
        cells = userFilling()
        mainLoop(cells)
    
