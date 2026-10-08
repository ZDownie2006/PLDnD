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
def action_text(text, position, window: curses.window, display_time=0.5):
    window.addstr(position[0] + 1, position[1] - (len(text)//2), text)
    window.refresh()
    time.sleep(display_time)
    window.addstr(position[0] + 1, position[1] - (len(text)//2), " " * len(text))

def attack_vis(window: curses.window, player_pos, enemy_pos):
    old_health = characters.goblin.hp
    combat_back.attack(characters.fighter, characters.goblin)
    damage = old_health - characters.goblin.hp
    centre = (int(curses.LINES * 0.5), int(curses.COLS * 0.5))

    action_text("ATTACK!", player_pos, window)
    if damage == 0:
        action_text("HA! YOU MISSED!", enemy_pos, window)
    else:
        action_text("OW!", enemy_pos, window)

    if characters.goblin.hp <= 0:
        action_text("ARGHHH!", enemy_pos, window)
        window.addstr(enemy_pos[0], enemy_pos[1], "💀")
        INITIATIVE_LIST.pop()
    elif characters.goblin.hp <= characters.goblin.max_hp // 2 and old_health > characters.goblin.max_hp:
        window.addstr(enemy_pos[0], enemy_pos[1], "👿")
        action_text("THAT HURTS!", enemy_pos, window)
        
    action_text(f"{characters.fighter.name} did {damage} damage to {characters.goblin.name}", centre, window, 2)

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
