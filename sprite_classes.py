#!/usr/bin/env python3

import curses
import time
import random
import characters
import combat_front
from combat_back import Checks

class Sprite:
    def __init__(self, window: curses.window, character, position):
        self.character = character
        self.position = position
        self.state = self.character.healthy_sprite
        self.active = False
        self.window = window
        self.display_sprite()

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def display_sprite(self):
        self.window.addstr(self.position[0], self.position[1], self.state)
        self.window.refresh()

    def sprite_is_dead(self):
        self.window.addstr(self.position[0], self.position[1], "💀")
        self.window.refresh()

    def is_active(self, active):
        if active:
            self.window.addstr(self.position[0] - 1, self.position[1], "▼", curses.color_pair(5))
        else:
            self.window.addstr(self.position[0] - 1, self.position[1], " ", curses.color_pair(5))
        self.window.refresh()

    def update_state(self):
        if self.state == self.character.healthy_sprite:
            self.state = self.character.injured_sprite
        else:
            self.state = self.character.healthy_sprite
        self.display_sprite()

    def attack_visual(self, window: curses.window, attacker: characters.Character, target: characters.Character, player_list: list, enemy_list: list, sprite_dictionary: dict):
        old_health = target.hp
        roll = attacker.attack(target)
        damage = old_health - target.hp
        centre = (window.size[0] - 2, int(window.size[1] * 0.5))
    
        window.display_text(text="ATTACK!", position=(self.position[0] + 1, self.position[1]), display_time=1)
        if attacker.role_type == "Player":
            display_string = f"{attacker.name} rolled a {roll}"
            window.display_text(display_string, centre, 1)
            
    
        if damage == 0:
            window.display_text("HA! YOU MISSED!", (sprite_dictionary[target].position[0] + 1, sprite_dictionary[target].position[1]))
        else:
            window.display_text("OW!", (sprite_dictionary[target].position[0] + 1, sprite_dictionary[target].position[1]))
    
        if Checks.hp_check(target):
            window.display_text("ARGHHH!", (sprite_dictionary[target].position[0] + 1, sprite_dictionary[target].position[1]), 1)
            sprite_dictionary[target].sprite_is_dead()
            combat_front.INITIATIVE_LIST.remove(target)
            enemy_list.remove(target) if target.role_type == "Enemy" else player_list.remove(target)
        elif target.hp <= target.max_hp // 2 and old_health > target.max_hp // 2:
            sprite_dictionary[target].update_state()
            window.display_text("THAT HURTS!", (sprite_dictionary[target].position[0] + 1, sprite_dictionary[target].position[1]))

        display_string = f"{attacker.name} did {damage} damage to {target.name}"
        window.display_text(display_string, centre, 2)

    def dodge_visual(self, window: curses.window, player, sprite_dictionary):
        centre = (window.size[0] - 2, int(window.size[1] * 0.5))
        player.dodge()
        window.display_text("LEAVE ME ALONE!", (sprite_dictionary[player].position[0] + 1, sprite_dictionary[player].position[1]))
        display_string = f"{player.name} prepares to dodge! New AC {player.cur_ac}"
        window.display_text(display_string, centre, 1)

    def heal_visual(self, window: curses.window, player, sprite_dictionary):
        centre = (window.size[0] - 2, int(window.size[1] * 0.5))
        old_health = player.hp
        player.heal()
        window.display_text("HEALING UP!", (sprite_dictionary[player].position[0] + 1, sprite_dictionary[player].position[1]))
        healed = player.hp - old_health
        window.display_text(f"{player.name} heals for {healed} hp!", centre, 1)
        if old_health < player.max_hp // 2 and player.hp > player.max_hp // 2:
            if player.role_type == "Enemy":
                self.update_state()
            else:
                self.update_state()
            window.display_text("COOL AS A CUCUMBER!", (sprite_dictionary[player].position[0] + 1, sprite_dictionary[player].position[1]))

