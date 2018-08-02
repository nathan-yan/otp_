import sys
import os 
import time

USING_TERMIOS = True

try:
    import tty
    import termios
    import select
except:
    import msvcrt
    USING_TERMIOS = False

def getch():
    if USING_TERMIOS:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            mode = termios.tcgetattr(fd)
            mode[tty.LFLAG] = mode[tty.LFLAG] & ~(termios.ECHO | termios.ICANON)
            termios.tcsetattr(fd, termios.TCSAFLUSH, mode)
            try:
                rw, wl, xl = select.select([fd], [], [], 1)
            except select.error:
                return
            if rw:
                return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    else:
        keydown = msvcrt.kbhit()
        if keydown:
            return msvcrt.getch().decode()
        
        time.sleep(1)
