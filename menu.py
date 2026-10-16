import curses
import characters
import random

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
            "Welcome to PLDnD!!!",
            ]

    for i, line in enumerate(castle):
        start_menu.addstr(i + 1, pos_mid - int(len(line)/2) , line)

    player_count = 2
    enemy_count = 2
    for num in range(player_count):
        characters.create_character(characters.RoleType.PLAYER.value, random.randint(1,2))
    for num in range(enemy_count):
        characters.create_character(characters.RoleType.ENEMY.value, random.randint(1,2))

    start_menu.noutrefresh()

def set_char_stat(window: curses.window):

    window.clear()

    char_table_contents = [
        ["Name", "Role", "Type", "HP", "AC", "ATK", "DMG", "Initative"],
        [""]
    ]

    character_list = characters.get_initative_list()

    for character in character_list:
        character_stat = [
            f"{character.name}",
            f"{character.role}",
            f"{character.role_type}",
            f"{character.hp}",
            f"{character.ac}",
            f"+{character.at_mod}",
            f"{character.dmg}",
            f"{character.initiative}"
        ]
        char_table_contents.append(character_stat)

    pos_mid = int(curses.COLS / 2)
    col_width = 12
    table_width = len(char_table_contents[0]) * col_width + 2
    char_table = window.derwin(len(char_table_contents)+2, table_width , 9, pos_mid - int(table_width/2))
    char_table.box()

    for i, line in enumerate(char_table_contents):
        for j, content in enumerate(line):
            char_table.addstr(i + 1, 2 + j * col_width, content)

    char_table.noutrefresh()
