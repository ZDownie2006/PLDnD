#!/usr/bin/env python3

import curses
import menu
import sys


def main(window: curses.window):

    window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)

    window = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    window.attrset(curses.color_pair(1))
    window.box()

    while 1:  # Loop so the game doesn't exit instantly
        menu.start(window)
        c = window.get_wch()
        if c == 'x':
            break
        elif c == 3:
            break
    sys.stderr.write('Interrupted\n')


if __name__ == '__main__':
    try:
        curses.wrapper(main)  # Initialise and return the window to main()
    except KeyboardInterrupt:
        pass
    finally:
        sys.stderr.write('Thanks for playing PLDnD!\nSee you again soon!\n')
