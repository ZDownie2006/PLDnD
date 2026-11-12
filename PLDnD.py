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
                menu.start()
                current_page = PageManager.turn_page(window, current_page)
            case Page.MENU:
                menu.set_char_stat()
                current_page = PageManager.turn_page(window, current_page)
            case Page.COMBAT:
                combat_front.fight_vis(window)
                return Page.BREAK
        return current_page

    def turn_page(window, current_page):
        match current_page:
            case Page.START:
                return Page.MENU
            case Page.MENU:
                return Page.COMBAT
        return current_page


def set_default_display():
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)


def main(window: curses.window):

    set_default_display()

    game_active = True
    current_page = Page.START

    while game_active:
        if current_page == Page.BREAK:
            game_active = False
        current_page = PageManager.manage(window, current_page)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stderr.write('Thanks for playing PLDnD!\nSee you again soon!\n')
