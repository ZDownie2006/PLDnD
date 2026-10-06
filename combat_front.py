#!/usr/bin/env python3

import curses
import time
import combat
import characters
import sys

INITIATIVE_LIST = [
    characters.fighter,
    characters.goblin,
]

def attack_vis(window: curses.window, player_pos, enemy_pos):
    characters.goblin.hp -= 3
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("ATTACK!")//2), "ATTACK!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("ATTACK!")//2), "       ")
    window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("OW!")//2), "OW!")
    window.refresh()
    time.sleep(1)
    window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("OW!")//2), "   ")
    if characters.goblin.hp <= 0:
        window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("ARGHHH!")//2), "ARGHHH!")
        window.refresh()
        time.sleep(1)
        window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("ARGHHH!")//2), "       ")
        window.addstr(enemy_pos[0], enemy_pos[1], "💀")
        INITIATIVE_LIST.pop()
    elif characters.goblin.hp <= characters.goblin.max_hp // 2:
        window.addstr(enemy_pos[0], enemy_pos[1], "👿")
        window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("THAT HURTS!")//2), "THAT HURTS!")
        window.refresh()
        time.sleep(1)
        window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("THAT HURTS!")//2), "           ")

def dodge_vis(window: curses.window, player_pos):
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("LEAVE ME ALONE!")//2), "LEAVE ME ALONE!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("LEAVE ME ALONE!")//2), "               ")

def heal_vis(window: curses.window, player_pos):
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("HEALING UP!")//2), "HEALING UP!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("HEALING UP!")//2), "           ")

def options_vis(window: curses.window):
    pos_quarter = int(curses.LINES * 0.75)
    options = window.derwin(int(curses.LINES * 0.275), curses.COLS, pos_quarter, 0)
    options.box()

    options.addstr(4, int(curses.COLS * 0.20)-5, "1. ATTACK ⚔️")
    options.addstr(4, int(curses.COLS * 0.40)-5, "2. DEFEND 🛡️")
    options.addstr(4, int(curses.COLS * 0.60)-3, "3. HEAL 🧪")
    options.addstr(4, int(curses.COLS * 0.80)-3, "0. QUIT 💨")

def fight_vis(window: curses.window):
    window.clear()
    window.border("|", "|", "-", 0, "+", "+")

    # Create Options Window
    options_vis(window)

    # Create Sprites
    player_pos = (int(curses.LINES * 0.4), int(curses.COLS * 0.25))
    enemy_pos = (int(curses.LINES * 0.4), int(curses.COLS * 0.75))
    window.addstr(enemy_pos[0], enemy_pos[1], "😈")
    window.addstr(player_pos[0], player_pos[1], "😎")


    while (len(INITIATIVE_LIST) > 1):
        action = window.get_wch()
        match (action):
            case "1":
                attack_vis(window, player_pos, enemy_pos)
            case "2":
                dodge_vis(window, player_pos)
            case "3":
                heal_vis(window, player_pos)
            case "0":
                return
        
        window.refresh()  # Refresh

    window.addstr(int(curses.LINES * 0.4), int(curses.COLS * 0.5) - 4, "YOU WIN!")
    window.addstr(int(curses.LINES * 0.5), int(curses.COLS * 0.5) - 10, "Press any key to exit")
    window.get_wch()
