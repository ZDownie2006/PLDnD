#!/usr/bin/env python3

import curses
import time
import combat_back
import characters
import sys

INITIATIVE_LIST = [
    characters.fighter,
    characters.goblin,
]

# Visuals on certain actions
def action_text(text, position, window: curses.window):
    window.addstr(position[0] + 1, position[1] - (len(text)//2), text)
    window.refresh()
    time.sleep(0.5)
    window.addstr(position[0] + 1, position[1] - (len(text)//2), " " * len(text))

def attack_vis(window: curses.window, player_pos, enemy_pos):
    characters.goblin.hp -= 3
    action_text("ATTACK!", player_pos, window)
    action_text("OW!", enemy_pos, window)
    if characters.goblin.hp <= 0:
        action_text("ARGHHH!", enemy_pos, window)
        window.addstr(enemy_pos[0], enemy_pos[1], "💀")
        INITIATIVE_LIST.pop()
    elif characters.goblin.hp <= characters.goblin.max_hp // 2:
        window.addstr(enemy_pos[0], enemy_pos[1], "👿")
        action_text("THAT HURTS!", enemy_pos, window)

def dodge_vis(window: curses.window, player_pos):
    action_text("LEAVE ME ALONE!", player_pos, window)

def heal_vis(window: curses.window, player_pos):
    action_text("HEALING UP!", player_pos, window)

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
