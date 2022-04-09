"""
File: BeeperRow.py
Name: Darren
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()
    
    
if __name__ == '__main__':
    execute_karel_task(main)
