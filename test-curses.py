import curses, os

def read_key(stdscr):
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    key = stdscr.getch()
    return key
os.system('cls' if os.name == 'nt' else 'clear')
key = -1
while key != 27:    
    key = curses.wrapper(read_key)
    if key == 132:
        print('a')
    elif key == 134:
        print('w')
    elif key == 178:
        print('d')
    elif key == 135:
        print('x')   
    elif key == 139:
        print('s')
    elif key != -1:
        print(key)