import curses
import characters


def start(window: curses.window):

    pos_mid = int(curses.COLS / 2)
    start_menu = window.derwin(curses.LINES, curses.COLS, 0, 0)

    castle = [
            " _   |~  _ ",
            "[_]--'--[_]",
            "|'|  `  |'|",
            "| | /^\\ | |",
            "|_|_|_|_|_|",
            "",
            "Welcome to PLDnD!!!"
            ]

    for i, line in enumerate(castle):
        start_menu.addstr(i + 1, pos_mid - int(len(line)/2) , line)

    window.refresh()


def set_char_stat(window: curses.window):

    window.clear()

    pos_mid = int(curses.COLS / 2)
    char_table = window.derwin(6, 72, 9, pos_mid - 36)
    char_table.box()

    char_table_contents = [
        ["Name", "Role", "Type", "HP", "AC", "ATK", "DMG"],
        [""],
        [
            f"{characters.fighter.name}",
            f"{characters.fighter.role}",
            f"{characters.fighter.role_type}",
            f"{characters.fighter.hp}",
            f"{characters.fighter.ac}",
            f"+" + f"{characters.fighter.at_mod}",
            f"{characters.fighter.dmg}"
        ],
        [
            f"{characters.goblin.name}",
            f"{characters.goblin.role}",
            f"{characters.goblin.role_type}",
            f"{characters.goblin.hp}",
            f"{characters.goblin.ac}",
            f"+" + f"{characters.goblin.at_mod}",
            f"{characters.goblin.dmg}"
        ],
    ]

    for i, line in enumerate(char_table_contents):
        for j, content in enumerate(line):
            char_table.addstr(i + 1, 2 + j * 10, content)

    window.refresh()
