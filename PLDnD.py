#!/usr/bin/env python3

import curses
import characters


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
    pos_mid = int(curses.COLS / 2)
    window.addstr(1, pos_mid - 6, " _   |~  _ ")
    window.addstr(2, pos_mid - 6, "[_]--'--[_]")
    window.addstr(3, pos_mid - 6, "|'|  `  |'|")
    window.addstr(4, pos_mid - 6, "| | /^\ | |")
    window.addstr(5, pos_mid - 6, "|_|_|_|_|_|")
    window.addstr(7, pos_mid - 10, "Welcome to PLDnd!!!")

    char_table = window.derwin(6, 72, 9, 2 + 7)
    char_table.box()
    char_table.addstr(1, 2, "Name")
    char_table.addstr(1, 12, "Role")
    char_table.addstr(1, 22, "Type")
    char_table.addstr(1, 32, "HP")
    char_table.addstr(1, 42, "AC")
    char_table.addstr(1, 52, "ATK")
    char_table.addstr(1, 62, "DMG")
    char_table.addstr(3, 2, "{}".format(characters.Fighter.name))
    char_table.addstr(3, 12, "{}".format(characters.Fighter.role))
    char_table.addstr(3, 22, "{}".format(characters.Fighter.role_type))
    char_table.addstr(3, 32, "{}".format(characters.Fighter.hp))
    char_table.addstr(3, 42, "{}".format(characters.Fighter.ac))
    char_table.addstr(3, 52, "{}".format(characters.Fighter.attack))
    char_table.addstr(3, 62, "{}".format(characters.Fighter.dmg))
    char_table.addstr(4, 2, "{}".format(characters.Goblin.name))
    char_table.addstr(4, 12, "{}".format(characters.Goblin.role))
    char_table.addstr(4, 22, "{}".format(characters.Goblin.role_type))
    char_table.addstr(4, 32, "{}".format(characters.Goblin.hp))
    char_table.addstr(4, 42, "{}".format(characters.Goblin.ac))
    char_table.addstr(4, 52, "{}".format(characters.Goblin.attack))
    char_table.addstr(4, 62, "{}".format(characters.Goblin.dmg))

    while 1:  # Loop so the game doesn't exit instantly
        window.refresh()  # Refresh


if __name__ == '__main__':
    curses.wrapper(main)  # Initialise and return the window to main()
