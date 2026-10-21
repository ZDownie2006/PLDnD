#!/usr/bin/env python3

import curses
import menu
import combat_front
import sys
from enum import Enum


class Page(Enum):
    START = "start"
    MENU = "menu"
    COMBAT = "combat"
    BREAK = "break"


class PageManager:
    def manage(window, current_page):
        match current_page:
            case Page.START:
                menu.start(window)
                current_page = PageManager.turn_page(window, current_page)
            case Page.MENU:
                menu.set_char_stat(window)
                current_page = PageManager.turn_page(window, current_page)
            case Page.COMBAT:
                combat_front.fight_vis(window)
                return Page.BREAK
        return current_page

    def turn_page(window, current_page):
        key_press = window.get_wch()

        if key_press == 'x':
            current_page = Page.BREAK

        match current_page:
            case Page.START:
                return Page.MENU
            case Page.MENU:
                return Page.COMBAT
        return current_page

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

    game_active = True
    current_page = Page.START

    while game_active:
        if current_page == Page.BREAK:
            break
        current_page = PageManager.manage(window, current_page)


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stderr.write('Thanks for playing PLDnD!\nSee you again soon!\n')
