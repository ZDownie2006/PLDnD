import curses
import pages.menu as menu
import combat_front
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


def set_default_page():
    curses.noecho()
    curses.curs_set(0)
    curses.cbreak()

    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_WHITE, -1)
