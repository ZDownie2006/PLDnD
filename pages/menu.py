import curses
import characters
import random

PAD_BUFFER = 100

def select_player_count(start_menu_pad, i):

    pos_mid = int(curses.COLS / 2)
    key_press = ""
    player_count = 1
    enemy_count = 2

    start_menu_pad.addstr(i + 7, pos_mid + 3, ">")

    while key_press not in (curses.KEY_ENTER, 10, 13):
        start_menu_pad.addstr(i + 7, pos_mid, str(player_count))
        if player_count > 1 and player_count < 4:
            start_menu_pad.addstr(i + 7, pos_mid - 3, "<")
            start_menu_pad.addstr(i + 7, pos_mid + 3, ">")
        elif player_count == 1:
            start_menu_pad.addstr(i + 7, pos_mid - 3, " ")
        elif player_count == 4:
            start_menu_pad.addstr(i + 7, pos_mid + 3, " ")

        start_menu_pad.refresh(0, 0, 0, 0, curses.LINES - 1 , curses.COLS - 1)
        key_press = start_menu_pad.getch()

        match (key_press):
            case 68:
                if player_count > 1:
                    player_count -= 1
                    start_menu_pad.addstr(i + 7, pos_mid - 3, "<")
            case 67:
                if player_count < 4:
                    player_count += 1
                    start_menu_pad.addstr(i + 7, pos_mid + 3, ">")

    for _ in range(player_count):
        characters.create_character(characters.RoleType.PLAYER.value, random.randint(1,2))
    for _ in range(enemy_count):
        characters.create_character(characters.RoleType.ENEMY.value, random.randint(1,2))


def start():

    pos_mid = int(curses.COLS / 2)
    start_menu_pad = curses.newpad(curses.LINES + PAD_BUFFER, curses.COLS + PAD_BUFFER)

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
        start_menu_pad.addstr(i + 1, pos_mid - int(len(line)/2) , line)

    player_count_message = ["Please use arrow keys to select player count (Max 4)", "Press enter to confirm"]
    for j, line in enumerate(player_count_message):
        start_menu_pad.addstr(len(castle) + j + 3, pos_mid - int(len(line)/2) , line)

    select_player_count(start_menu_pad, i)

def set_char_stat():

    curses.curs_set(0)
    character_stat_pad = curses.newpad(curses.LINES + PAD_BUFFER, curses.COLS + PAD_BUFFER)

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
            f"{character.dmg_dice}",
            f"{character.initiative}"
        ]
        char_table_contents.append(character_stat)

    col_width = 12
    table_width = len(char_table_contents[0]) * col_width + 2
    pos_mid = int(curses.COLS / 2)
    pos_x = max(0, pos_mid - table_width // 2)
    char_table = character_stat_pad.subpad(len(char_table_contents)+2, table_width, 5, pos_x)
    char_table.box()

    for i, line in enumerate(char_table_contents):
        for j, content in enumerate(line):
            char_table.addstr(i + 1, 2 + j * col_width, content)

    character_stat_pad.refresh(0, 0, 0, 0, curses.LINES - 1 , curses.COLS - 1)
    character_stat_pad.getch()
