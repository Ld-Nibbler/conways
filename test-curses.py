import curses, os, time
WIDTH = 60
HEIGHT = 20

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
os.system('cls' if os.name == 'nt' else 'clear')
print('Cursor moving:')
print('a - left, w - up, d - right, x - down')
print('s - select/delete point')
print('Space - to start')
print('Esc - to finish drawing and start the game')
key = -1
crx = 2
cry = 2
points = []

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
    