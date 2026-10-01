#!/usr/bin/env python3

import curses
import sys


def main(window: curses.window):
    window.keypad(True)  # Turn on keypad mode
    curses.noecho()  # Turn off key echoing
    curses.curs_set(0)  # Set cursor visibility
    curses.cbreak()  # Turn off buffered input

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)

    window = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    window.attrset(curses.color_pair(1))
    window.box()

    # Create Sprites
    window.addstr((curses.LINES // 4), (curses.COLS // 2), "😈")
    window.addstr((curses.LINES // 2), (curses.COLS // 2), "🤺")

    while 1:  # Loop so the game doesn't exit instantly
        window.refresh()  # Refresh


if __name__ == "__main__":
    try:
        curses.wrapper(main)  # Initialise and return the window to main()
    except KeyboardInterrupt:
        pass
    finally:
        sys.stderr.write('Thanks for fighting in PLDnD!\nSee you again soon!\n')
