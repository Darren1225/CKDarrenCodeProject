"""
File: Steeplechase.py
Name: Darren
---------------------------------
Darren:
"""

from karel.stanfordkarel import*


def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()


def jump():
    #karel is going to cross over all the steeple#
    up()
    cross()
    down()


def up():
    #karel is going to climb up the steepls#
    turn_left()# karel is facing North
    while not right_is_clear():
        move()


def turn_right():
    for i in range(3):
        turn_left()


def cross():
    turn_right()
    move()
    turn_right()


def down():
    while front_is_clear():
        move()
    turn_left()




if __name__ == '__main__':
    execute_karel_task(main)
