# Conway's game of life
import random, time, copy, os, curses, sys
WIDTH = 60
HEIGHT = 20
points = [] # User drawing list

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
    try:       
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
            time.sleep(0.2) # Add a 0.2-second pause to reduce flickering.
    except KeyboardInterrupt:
        print('\n Good bye!')
        sys.exit()

def read_key(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    key = stdscr.getch()
    return key

def field_draw(cx, cy):
    os.system('cls' if os.name == 'nt' else 'clear')
    for xs in range(WIDTH+2):
        print('-', end='')
    print()
        # Print currentCells on the screen
    for y in range(HEIGHT):
        print('|', end='')
        for x in range(WIDTH):
            if (x,y) in points:
                print("0",end='')
            elif x == cx and y == cy:
                print("X", end="") # Printing the cursor position
            else:
                print(".", end="") # Printing space
            
            
        print('|') # Printing a new line at the end of the row      
    for xs in range(WIDTH+2):
        print('-', end='')
    print('\n\n')


def userDrawing():
    # pattern = []
    # pattern.append((4,1))
    # pattern.append((5,2))
    # pattern.append((5,3))
    # pattern.append((4,3))
    # pattern.append((3,3))
    # pattern.append((57,1))
    # pattern.append((56,2))
    # pattern.append((56,3))
    # pattern.append((57,3))
    # pattern.append((58,3))    
    
    # return pattern
    key = -1
    crx = 30 # Start drawing x
    cry = 10 # Start drawing y
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Cursor moving:')
    print('a - left, w - up, d - right, x - down')
    print('s - select/delete point')
    print('Space - to start')
    print('Esc - to finish drawing and start the game')

    while key != 27:  
        crx = crx % WIDTH 
        cry = cry % HEIGHT  
        key = curses.wrapper(read_key)    
        if key == 32:
            field_draw(crx,cry)
        elif key == 132 or key == 97:
            crx = (crx - 1) % WIDTH
            field_draw(crx,cry)
        elif key == 134 or key == 119:
            cry = (cry - 1) % HEIGHT
            field_draw(crx,cry)
        elif key == 178 or key == 100:
            crx = (crx + 1) % WIDTH
            field_draw(crx,cry)
        elif key == 135 or key == 120:
            cry = (cry + 1) % HEIGHT
            field_draw(crx,cry)  
        elif key == 139 or key == 115:
            if ((crx, cry)) in points:
                points.remove((crx,cry))
            else:
                points.append((crx,cry))
            field_draw(crx,cry) 
        else:
            time.sleep(0.5) # Add a 0.5-second pause to reduce flickering.
    
        
def userFilling():
    userDrawing()    
    
    nextCells = []
    for x in range(WIDTH):
        column = [] # Create a new column
        for y in range(HEIGHT):        
            if (x,y) in points:
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
    
