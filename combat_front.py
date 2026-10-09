#!/usr/bin/env python3

import curses
import time
import combat_back
import characters
import random

INITIATIVE_LIST = [
    characters.fighter,
    characters.goblin,
]

ENEMY_POSITIONS = {}
PLAYER_POSITIONS = {}

# Visuals on certain actions
def action_text(text, position, window: curses.window, display_time=0.75):
    window.addstr(position[0] + 1, position[1] - (len(text)//2), text)
    window.refresh()
    time.sleep(display_time)
    window.addstr(position[0] + 1, position[1] - (len(text)//2), " " * len(text))

def attack_vis(window: curses.window, attacker, target):
    old_health = target.hp
    combat_back.attack(attacker, target)
    damage = old_health - target.hp
    centre = (int(curses.LINES * 0.5), int(curses.COLS * 0.5))

    action_text("ATTACK!", attacker.position, window, 1)
    if damage == 0:
        action_text("HA! YOU MISSED!", target.position, window)
    else:
        action_text("OW!", target.position, window)

    if target.hp <= 0:
        action_text("ARGHHH!", target.position, window, 1)
        window.addstr(target.position[0], target.position[1], "💀")
        INITIATIVE_LIST.pop()
    elif target.hp <= target.max_hp // 2 and old_health > target.max_hp // 2:
        if target.role_type == "Enemy":
            window.addstr(target.position[0], target.position[1], "👿")
        else:
            window.addstr(target.position[0], target.position[1], "🤕")
        action_text("THAT HURTS!", target.position, window)
        
    action_text(f"{attacker.name} did {damage} damage to {target.name}", centre, window, 1)

def dodge_vis(window: curses.window, player):
    centre = (int(curses.LINES * 0.5), int(curses.COLS * 0.5))
    combat_back.dodge(player)
    action_text("LEAVE ME ALONE!", player.position, window)
    action_text(f"{player.name} prepares to dodge! New AC {player.cur_ac}", centre, window, 2)

def heal_vis(window: curses.window, player):
    centre = (int(curses.LINES * 0.5), int(curses.COLS * 0.5))
    old_health = player.hp
    combat_back.heal(player)
    action_text("HEALING UP!", player.position, window)
    healed = player.hp - old_health
    action_text(f"{player.name} heals for {healed} hp!", centre, window, 1)
    if old_health < player.max_hp // 2 and player.hp > player.max_hp // 2:
        if player.role_type == "Enemy":
            window.addstr(player.position[0], player.position[1], "😈")
        else:
            window.addstr(player.position[0], player.position[1], "😎")
        action_text("COOL AS A CUCUMBER!", player.position, window)


def options_vis(window: curses.window):
    pos_quarter = int(curses.LINES * 0.75)
    options = window.derwin(int(curses.LINES * 0.275), curses.COLS, pos_quarter, 0)
    options.box()

    options.addstr(4, int(curses.COLS * 0.20)-5, "1. ATTACK ⚔️")
    options.addstr(4, int(curses.COLS * 0.40)-5, "2. DEFEND 🛡️")
    options.addstr(4, int(curses.COLS * 0.60)-3, "3. HEAL 🧪")
    options.addstr(4, int(curses.COLS * 0.80)-3, "0. QUIT 💨")

def create_sprites(window: curses.window, character):
    if character.role_type == "Player":
        character.position = (int(curses.LINES * 0.4), int(curses.COLS * 0.25))
        window.addstr(character.position[0], character.position[1], "😎")
    elif character.role_type == "Enemy":
        character.position = (int(curses.LINES * 0.4), int(curses.COLS * 0.75))
        window.addstr(character.position[0], character.position[1], "😈")

def fight_vis(window: curses.window):
    window.clear()
    window.border("|", "|", "-", 0, "+", "+")

    # Create Options Window
    options_vis(window)

    # Create Sprites
    for character in INITIATIVE_LIST:
        create_sprites(window, character)

    while (len(INITIATIVE_LIST) > 1):
        window.refresh()
        active_character = INITIATIVE_LIST.pop(0)

        new_window = window.derwin(1, curses.COLS - 2, int(curses.LINES * 0.8), 1)
        turn_string = f"{active_character.name}'s turn".upper()
        new_window.addstr(0, int((curses.COLS - len(turn_string)) * 0.5), turn_string)
        new_window.refresh()
        time.sleep(0.5)

        action = -1
        actions = ["0", "1", "2", "3"]
        if active_character.role_type == "Player":
            while action not in actions:
                action = window.get_wch()
        else:
            action = random.choices(actions, [0, 3, 2, 1], k=1)[0]
        target = INITIATIVE_LIST[0]
        action = int(action)

        match (action):
            case 1:
                attack_vis(window, active_character, target)
            case 2:
                dodge_vis(window, active_character)
            case 3:
                heal_vis(window, active_character)
            case 0:
                return
        
        window.refresh()  # Refresh
        INITIATIVE_LIST.append(active_character)
        new_window.clear()

    win_string = f"{INITIATIVE_LIST[0].name} WINS!"
    window.addstr(int(curses.LINES * 0.4), int((curses.COLS - len(win_string)) * 0.5), f"{INITIATIVE_LIST[0].name} WINS!")
    window.addstr(int(curses.LINES * 0.5), int(curses.COLS * 0.5) - 10, "Press any key to exit")
    window.get_wch()
