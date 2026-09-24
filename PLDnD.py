#!/usr/bin/env python3

import curses
import characters

def main(window: curses.window):

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
    window.addstr(4, pos_mid - 6, "| | /^\\ | |")
    window.addstr(5, pos_mid - 6, "|_|_|_|_|_|")
    window.addstr(7, pos_mid - 10, "Welcome to PLDnD!!!")

    char_table = window.derwin(6, 72, 9, pos_mid - 36)
    char_table.box()
    char_table.addstr(1, 2, "Name")
    char_table.addstr(1, 12, "Role")
    char_table.addstr(1, 22, "Type")
    char_table.addstr(1, 32, "HP")
    char_table.addstr(1, 42, "AC")
    char_table.addstr(1, 52, "ATK")
    char_table.addstr(1, 62, "DMG")
    char_table.addstr(3, 2, "{}".format(characters.fighter.name))
    char_table.addstr(3, 12, "{}".format(characters.fighter.role))
    char_table.addstr(3, 22, "{}".format(characters.fighter.role_type))
    char_table.addstr(3, 32, "{}".format(characters.fighter.hp))
    char_table.addstr(3, 42, "{}".format(characters.fighter.ac))
    char_table.addstr(3, 52, "+" + "{}".format(characters.fighter.at_mod))
    char_table.addstr(3, 62, "{}".format(characters.fighter.dmg))
    char_table.addstr(4, 2, "{}".format(characters.goblin.name))
    char_table.addstr(4, 12, "{}".format(characters.goblin.role))
    char_table.addstr(4, 22, "{}".format(characters.goblin.role_type))
    char_table.addstr(4, 32, "{}".format(characters.goblin.hp))
    char_table.addstr(4, 42, "{}".format(characters.goblin.ac))
    char_table.addstr(4, 52, "+" + "{}".format(characters.goblin.at_mod))
    char_table.addstr(4, 62, "{}".format(characters.goblin.dmg))

    while 1:  # Loop so the game doesn't exit instantly
        window.refresh()  # Refresh
        c = window.get_wch()
        if c == 'x':
            break

if __name__ == '__main__':
    curses.wrapper(main)  # Initialise and return the window to main()
