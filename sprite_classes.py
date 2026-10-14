#!/usr/bin/env python3

import curses
import time
import random

class Sprite:
    def __init__(self, window: curses.window, character, position):
        self.character = character
        self.position = position
        self.state = self.character.healthy_sprite
        self.display_sprite(window)

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def display_sprite(self, window: curses.window):
        window.addstr(self.position[0], self.position[1], self.state)
        window.refresh()

    def update_state(self):
        if self.state == self.character.healthy_sprite:
            self.state = self.character.injured_sprite
        else:
            self.state = self.character.healthy_sprite
