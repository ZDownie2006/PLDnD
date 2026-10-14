#!/usr/bin/env python3

import curses
import time
import combat_back
import characters
import random
import display_classes
import sprite_classes
from sound_effects import battle_music, victory_music

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
    roll = combat_back.attack(attacker, target)
    damage = old_health - target.hp
    centre = (int(curses.LINES * 0.5), int(curses.COLS * 0.5))

    action_text("ATTACK!", attacker.position, window, 1)
    if attacker.role_type == "Player":
        action_text(f"{attacker.name} rolled a {roll}", centre, window, 1)

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

# Creates and displays actions the player can take via a subwindow
# Returns the subwindow
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

# Creates a visual sprite for each character and places them evenly on the screen
def create_sprites(window: curses.window, characters):
    party_size = len(characters)
    x_coordinate = int(curses.COLS * 0.25) if characters[0].role_type == "Player" else int(curses.COLS * 0.75)
    for index, character in enumerate(characters):
        y_coordinate = int(0 + (index + 1) * (curses.LINES - (curses.LINES * 0.25)) / (party_size + 1))
        character.position = (y_coordinate, x_coordinate)
        
        window.addstr(character.position[0], character.position[1], character.healthy_sprite)

# Allows player to choose an action via arrow keys
def select_action(options: curses.window):
    options.keypad(True)
    key_press = ""
    i = 1
    while key_press not in (curses.KEY_ENTER, 10, 13):
        centres = [0.80, 0.20, 0.40, 0.60]
        centre = centres[abs(i) % 4]
        height = int(curses.LINES * 0.275)

        # Make a box
        blue = curses.color_pair(4)
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

    options.refresh()    
    return i

# Allows player to select a target via arrow keys
def select_target(window: curses.window, enemy_list):
    window.keypad(True)
    key_press = ""
    i = 0
    while key_press not in (curses.KEY_ENTER, 10, 13):
        current_enemy = enemy_list[abs(i) % len(enemy_list)]
        
        # Make a box
        red = curses.color_pair(2)
        window.addstr(current_enemy.position[0], current_enemy.position[1], current_enemy.healthy_sprite, curses.color_pair(3))

        attack_string = f"Attack {current_enemy.name}"
        window.addstr(int(curses.LINES * 0.65), int((curses.COLS - len(attack_string)) * 0.5), attack_string, red)

        key_press = window.getch()
        match (key_press):
            case curses.KEY_UP:
                i -= 1
            case curses.KEY_DOWN:
                i += 1

        window.addstr(current_enemy.position[0], current_enemy.position[1], current_enemy.healthy_sprite, curses.color_pair(1))
        window.addstr(int(curses.LINES * 0.65), int((curses.COLS - len(attack_string)) * 0.5), " " * len(attack_string))

    return current_enemy

    
def fight_vis(window: curses.window):

    combat_window = display_classes.Display(int(curses.LINES * 0.75), curses.COLS, (0, 0))
    combat_window.create_border()

    options_window = display_classes.Actions(int(curses.LINES * 0.15), curses.COLS, (int(curses.LINES * 0.85), 0))
    options_window.create_border()

    combat_window.window.refresh()
    options_window.window.refresh()

    ## Create Sprites
    sprite_dictionary = {}
    
    # Create Player Sprites
    player_list = combat_back.player_list(INITIATIVE_LIST)
    party_size = len(player_list)
    x_coordinate = int(curses.COLS * 0.25)
    for index, player in enumerate(player_list):
        y_coordinate = int(0 + (index + 1) * (curses.LINES - (curses.LINES * 0.25)) / (party_size + 1))
        sprite_dictionary[player] = sprite_classes.Sprite(combat_window.window, player, (y_coordinate, x_coordinate))

    # Create Enemy Sprites
    enemy_list = combat_back.enemy_list(INITIATIVE_LIST)
    party_size = len(enemy_list)
    x_coordinate = int(curses.COLS * 0.75)
    for index, enemy in enumerate(enemy_list):
        y_coordinate = int(0 + (index + 1) * (curses.LINES - (curses.LINES * 0.25)) / (party_size + 1))
        sprite_dictionary[enemy] = sprite_classes.Sprite(combat_window.window, enemy, (y_coordinate, x_coordinate))

    while True:
        pass
    # background_music = battle_music()

    # window.clear()
    # window.border("|", "|", "-", 0, "+", "+")
    # curses.init_pair(2, curses.COLOR_RED, -1)
    # curses.init_pair(3, -1, curses.COLOR_RED)
    # curses.init_pair(4, curses.COLOR_BLUE, -1)
    # curses.init_pair(5, curses.COLOR_GREEN, -1)

    # # Create Player Sprites
    # player_list = combat_back.player_list(INITIATIVE_LIST)
    # create_sprites(window, player_list)

    # # Create Enemy Sprites
    # enemy_list = combat_back.enemy_list(INITIATIVE_LIST)
    # create_sprites(window, enemy_list)

    # while (enemy_list and player_list):        
    #     window.refresh()
    #     if not background_music.is_alive():
    #         background_music = battle_music()
        
    #     active_character = INITIATIVE_LIST.pop(0)
    #     turn_string = f"{active_character.name}'s turn".upper()
    #     window.addstr(active_character.position[0] - 1, active_character.position[1], "▼", curses.color_pair(5))
    #     window.refresh()

    #     # Update Options Window
    #     options_win = options_vis(window, turn_string)
        
    #     time.sleep(0.5)

    #     # Ignore key presses during action processes
    #     curses.flushinp()

    #     action = -1
    #     actions = [0, 1, 2, 3]
    #     if active_character.role_type == "Player":
    #         while action not in actions:
    #             action = select_action(options_win)
    #         if action == 1:
    #             target = select_target(window, enemy_list)
    #     else:
    #         action = random.choices(actions, [0, 3, 2, 1], k=1)[0]
    #         target = random.choice(player_list)

    #     match (action):
    #         case 1:
    #             attack_vis(window, active_character, target, player_list, enemy_list)
    #         case 2:
    #             dodge_vis(window, active_character)
    #         case 3:
    #             heal_vis(window, active_character)
    #         case 0:
    #             background_music.stop()
    #             return
        
    #     window.refresh()  # Refresh
    #     INITIATIVE_LIST.append(active_character)
    #     window.addstr(active_character.position[0] - 1, active_character.position[1], " ", curses.color_pair(1))

    # background_music.stop()
    # endgame_music = victory_music()
    # win_string = f"YOUR PARTY WINS!" if player_list else "GAME OVER"
    # window.addstr(int(curses.LINES * 0.4), int((curses.COLS - len(win_string)) * 0.5), win_string)
    # window.addstr(int(curses.LINES * 0.5), int(curses.COLS * 0.5) - 10, "Press any key to exit")
    # window.get_wch()
    # endgame_music.stop()
