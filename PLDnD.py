#!/usr/bin/env python3

import curses

def main(window: curses.window):

    stdscr = curses.initscr()

    window.keypad(True)
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    fground = curses.COLOR_WHITE
    bground = -1
    curses.init_pair(1, fground, bground)

    window = curses.newwin(curses.LINES, curses.COLS, 0, 0)
    window.attrset(curses.color_pair(1))
    window.box()
    window.attrset(curses.color_pair(1))
    window.addstr(1,2," _   |~  _ ")
    window.addstr(2,2,"[_]--'--[_]")
    window.addstr(3,2,"|'|  `  |'|")
    window.addstr(4,2,"| | /^\ | |")
    window.addstr(5,2,"|_|_|I|_|_|")
    window.addstr(7, 2, "Welcome to PLDnd!!!")

    char_table = window.derwin(10,10,9,2)
    char_table.box()

    while 1: # Loop so the game doesn't exit instantly
        window.refresh() # Refresh

if __name__ == '__main__':
    curses.wrapper(main) # Initialise and return the window to main()

