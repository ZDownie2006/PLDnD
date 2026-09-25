import curses
import characters

def start(window: curses.window):
    window.box()

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

    window.refresh()
