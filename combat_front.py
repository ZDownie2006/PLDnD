#!/usr/bin/env python3

import curses
import time
import combat_back
import characters
import random
import display_classes
import sprite_classes
from sound_effects import battle_music, victory_music

INITIATIVE_LIST = characters.get_initative_list()

def fight_vis(window: curses.window):
    try:
        background_music = battle_music()
        curses.init_pair(2, curses.COLOR_RED, -1)
        curses.init_pair(3, -1, curses.COLOR_RED)
        curses.init_pair(4, curses.COLOR_BLUE, -1)
        curses.init_pair(5, curses.COLOR_GREEN, -1)

        combat_window = display_classes.Display(int(curses.LINES * 0.75), curses.COLS, (0, 0))
        combat_window.create_border()

        options_window = display_classes.Actions(int(curses.LINES * 0.20), curses.COLS, (int(curses.LINES * 0.80), 0))
        options_window.create_border()

        # combat_window.window.refresh()
        # options_window.window.refresh()

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

        while (enemy_list and player_list):
            if not background_music.is_alive():
                background_music = battle_music()

            combat_window.window.refresh()
            options_window.window.refresh()

            # Define which character's turn it is
            active_character = INITIATIVE_LIST.pop(0)
            active_sprite = sprite_dictionary[active_character]

            # Display active character's name and pointer
            options_window.display_turn(active_character.name)
            active_sprite.is_active(True)

            # Select action character is going to take
            curses.flushinp()
            actions = [0, 1, 2, 3]
            if active_character.role_type == "Enemy":
                action = random.choices(actions, [0, 3, 2, 1], k=1)[0]
                target = random.choice(player_list)
            else:
                action = options_window.select_action()

            if active_character.role_type == "Player" and action == 1:
                target = combat_window.select_target(sprite_dictionary, enemy_list)

            match (action):
                case 1:
                    active_sprite.attack_visual(combat_window, active_character, target, player_list, enemy_list, sprite_dictionary)
                case 2:
                    active_sprite.dodge_visual(combat_window, active_character, sprite_dictionary)
                case 3:
                    active_sprite.heal_visual(combat_window, active_character, sprite_dictionary)
                case 0:
                    background_music.stop()
                    return
                
            active_sprite.is_active(False)
            INITIATIVE_LIST.append(active_character)

        background_music.stop()
        endgame_music = victory_music()
        win_string = f"YOUR PARTY WINS!" if player_list else "GAME OVER"
        window.addstr(int(curses.LINES * 0.4), int((curses.COLS - len(win_string)) * 0.5), win_string)
        window.addstr(int(curses.LINES * 0.5), int(curses.COLS * 0.5) - 10, "Press any key to exit")
        window.get_wch()
        endgame_music.stop()
    except Exception:
        print("Unknown Error: Game closing!")
        background_music.stop()
