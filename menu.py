import curses
import characters
import random
from display_classes import Display

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

    player_amount_request = "Select Amount of Players (Max 4)"
    start_menu.addstr(i + 5, pos_mid - int(len(player_amount_request)/2), player_amount_request)

    key_press = ""
    player_count = 1
    enemy_count = 2

    start_menu.addstr(i + 7, pos_mid + 3, ">")

    while key_press not in (curses.KEY_ENTER, 10, 13):
        start_menu.addstr(i + 7, pos_mid, str(player_count))
        if player_count > 1 and player_count < 4:
            start_menu.addstr(i + 7, pos_mid - 3, "<")
            start_menu.addstr(i + 7, pos_mid + 3, ">")
        elif player_count == 1:
            start_menu.addstr(i + 7, pos_mid - 3, " ")
        elif player_count == 4:
            start_menu.addstr(i + 7, pos_mid + 3, " ")

        start_menu.refresh()
        key_press = start_menu.getch()

        match (key_press):
            case 68:
                if player_count > 1:
                    player_count -= 1
                    start_menu.addstr(i + 7, pos_mid - 3, "<")
            case 67:
                if player_count < 4:
                    player_count += 1
                    start_menu.addstr(i + 7, pos_mid + 3, ">")

    for _ in range(player_count):
        characters.create_character(characters.RoleType.PLAYER.value, random.randint(1,2))
    for _ in range(enemy_count):
        characters.create_character(characters.RoleType.ENEMY.value, random.randint(1,2))

    next_page_message = "Press Key to View Character Stats"
    start_menu.addstr(i + 10, pos_mid - len(next_page_message)//2, "Press Key to View Character Stats")

    start_menu.noutrefresh()

def set_char_stat():

    character_stat_display = Display(height=curses.LINES, width=curses.COLS)
    character_stat_window = character_stat_display.window

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
    char_table = character_stat_window.derwin(len(char_table_contents)+2, table_width , 9, pos_mid - int(table_width/2))
    char_table.box()

    for i, line in enumerate(char_table_contents):
        for j, content in enumerate(line):
            char_table.addstr(i + 1, 2 + j * col_width, content)

    character_stat_window.refresh()
