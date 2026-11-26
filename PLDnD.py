#!/usr/bin/env python3

import curses
import sys
import pages.page_manager as page_manager


def main(window: curses.window):

    page_manager.set_default_page()

    game_active = True
    current_page = page_manager.Page.START

    while game_active:
        if current_page == page_manager.Page.BREAK:
            game_active = False
        current_page = page_manager.PageManager.manage(window, current_page)

if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    finally:
        sys.stderr.write('Thanks for playing PLDnD!\nSee you again soon!\n')
