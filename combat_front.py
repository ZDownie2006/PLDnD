#!/usr/bin/env python3

import curses
from curses.textpad import rectangle
import time
import combat_back
import characters
import random

INITIATIVE_LIST = [
    characters.fighter,
    characters.mage,
    characters.goblin,
    characters.demon
]

# Visuals on certain actions
def action_text(text, position, window: curses.window, display_time=0.75):
    window.addstr(position[0] + 1, position[1] - (len(text)//2), text)
    window.refresh()
    time.sleep(display_time)
    window.addstr(position[0] + 1, position[1] - (len(text)//2), " " * len(text))

def attack_vis(window: curses.window, attacker, target, player_list, enemy_list):
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
        INITIATIVE_LIST.remove(target)
        enemy_list.remove(target) if target.role_type == "Enemy" else player_list.remove(target)
    elif target.hp <= target.max_hp // 2 and old_health > target.max_hp // 2:
        window.addstr(target.position[0], target.position[1], target.injured_sprite)
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
            window.addstr(player.position[0], player.position[1], player.healthy_sprite)
        else:
            window.addstr(player.position[0], player.position[1], player.healthy_sprite)
        action_text("COOL AS A CUCUMBER!", player.position, window)


def options_vis(window: curses.window, turn_string):
    pos_quarter = int(curses.LINES * 0.75)
    height = int(curses.LINES * 0.275)
    width = curses.COLS
    options = window.derwin(height, width, pos_quarter, 0)
    options.box()

    options.addstr(int(height * 0.5), int(curses.COLS * 0.20)-4, "ATTACK 🗡️")
    options.addstr(int(height * 0.5), int(curses.COLS * 0.40)-4, "DODGE 💨")
    options.addstr(int(height * 0.5), int(curses.COLS * 0.60)-3, "HEAL 💊")
    options.addstr(int(height * 0.5), int(curses.COLS * 0.80)-3, "QUIT 😰")

    options.addstr(0, int((width - len(turn_string)) * 0.5), turn_string)

    options.refresh()

    return options

def create_sprites(window: curses.window, characters):
    party_size = len(characters)
    x_coordinate = int(curses.COLS * 0.25) if characters[0].role_type == "Player" else int(curses.COLS * 0.75)
    for index, character in enumerate(characters):
        y_coordinate = int(0 + (index + 1) * (curses.LINES - (curses.LINES * 0.25)) / (party_size + 1))
        character.position = (y_coordinate, x_coordinate)
        window.addstr(character.position[0], character.position[1], character.healthy_sprite)

def select_action(options: curses.window, window: curses.window):
    window.keypad(True)
    options.keypad(True)
    key_press = ""
    i = 1
    while key_press not in (curses.KEY_ENTER, 10, 13):
        centres = [0.80, 0.20, 0.40, 0.60]
        centre = centres[abs(i) % 4]
        height = int(curses.LINES * 0.275)

        # Make a box
        curses.init_pair(3, curses.COLOR_BLUE, -1)
        blue = curses.color_pair(3)
        options.addstr(int(height * 0.5) + 1, int(curses.COLS * centre - 5), "-----------", blue)
        options.addstr(int(height * 0.5), int(curses.COLS * centre) + 5, "⎪", blue)
        options.addstr(int(height * 0.5), int(curses.COLS * centre) - 5, "⎪", blue)
        options.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) - 5, "-----------", blue)

        key_press = options.getch()
        match (key_press):
            case curses.KEY_LEFT:
                i -= 1
            case curses.KEY_RIGHT:
                i += 1
        if i <= -1:
            i = 4

        options.addstr(int(height * 0.5) + 1, int(curses.COLS * centre) - 5, "           ")
        options.addstr(int(height * 0.5), int(curses.COLS * centre) + 5, " ")
        options.addstr(int(height * 0.5), int(curses.COLS * centre) - 5, " ")
        options.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) - 5, "           ")

    return i

def select_target(window: curses.window, enemy_list):
    window.keypad(True)
    key_press = ""
    i = 0
    while key_press not in (curses.KEY_ENTER, 10, 13):
        current_enemy = enemy_list[abs(i) % len(enemy_list)]
        
        # Make a box
        curses.init_pair(2, curses.COLOR_RED, -1)
        red = curses.color_pair(2)
        window.addstr(current_enemy.position[0] + 1, current_enemy.position[1], "--", red)
        window.addstr(current_enemy.position[0], current_enemy.position[1] + 1, "|", red)
        window.addstr(current_enemy.position[0], current_enemy.position[1] - 1, "|", red)
        window.addstr(current_enemy.position[0] - 1, current_enemy.position[1], "--", red)

        key_press = window.getch()
        match (key_press):
            case curses.KEY_UP:
                i -= 1
            case curses.KEY_DOWN:
                i += 1

        window.addstr(current_enemy.position[0] + 1, current_enemy.position[1], "  ")
        window.addstr(current_enemy.position[0], current_enemy.position[1] + 1, " ")
        window.addstr(current_enemy.position[0], current_enemy.position[1] - 1, " ")
        window.addstr(current_enemy.position[0] - 1, current_enemy.position[1], "  ")

    return current_enemy

    
def fight_vis(window: curses.window):
    window.clear()
    window.border("|", "|", "-", 0, "+", "+")

    # Create Player Sprites
    player_list = combat_back.player_list(INITIATIVE_LIST)
    # player_list = [character for character in INITIATIVE_LIST if character.role_type == "Player"]
    create_sprites(window, player_list)

    # Create Enemy Sprites
    enemy_list = combat_back.enemy_list(INITIATIVE_LIST)
    # enemy_list = [character for character in INITIATIVE_LIST if character.role_type == "Enemy"]
    create_sprites(window, enemy_list)

    while (enemy_list and player_list):        
        window.refresh()
        
        active_character = INITIATIVE_LIST.pop(0)
        turn_string = f"{active_character.name}'s turn".upper()

        # Update Options Window
        options_win = options_vis(window, turn_string)
        
        time.sleep(0.5)

        # Ignore key presses during action processes
        curses.flushinp()

        action = -1
        actions = ["0", "1", "2", "3"]
        if active_character.role_type == "Player":
            while action not in actions:
                # action = window.get_wch()
                action = str(select_action(options_win, window))
            if action == "1":
                target = select_target(window, enemy_list)
        else:
            action = random.choices(actions, [0, 3, 2, 1], k=1)[0]
            target = random.choice(player_list)
        action = int(action)

        match (action):
            case 1:
                attack_vis(window, active_character, target, player_list, enemy_list)
            case 2:
                dodge_vis(window, active_character)
            case 3:
                heal_vis(window, active_character)
            case 0:
                return
        
        window.refresh()  # Refresh
        INITIATIVE_LIST.append(active_character)

    win_string = f"YOUR PARTY WINS!" if player_list else "GAME OVER"
    window.addstr(int(curses.LINES * 0.4), int((curses.COLS - len(win_string)) * 0.5), win_string)
    window.addstr(int(curses.LINES * 0.5), int(curses.COLS * 0.5) - 10, "Press any key to exit")
    window.get_wch()
