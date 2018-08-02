import sys
import os 

USING_TERMIOS = True

try:
    import tty
    import termios
except:
    import msvcrt
    USING_TERMIOS = False

def getch():
    if USING_TERMIOS:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_setting)

        return ch
    else:
        keydown = msvcrt.kbhit()
        if keydown:
            return msvcrt.getch().decode()
