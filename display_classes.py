#!/usr/bin/env python3

import curses
import time

class Display:
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(self.height, self.width, self.coordinates[0], self.coordinates[1])

    def create_border(self, ls="|", rs="|", ts="-", bs="-"):
        self.window.border(ls, rs, ts, bs)

    def display_text(self, text="", position=(0, 0), display_time=0.75):
        self.window.addstr(position[0], position[1], text)
        self.window.refresh()
        time.sleep(display_time)
        self.window.addstr(position[0], position[1], " " * len(text))
        self.window.refresh()

    def select_target(self, sprite_dictionary, enemy_list):
        self.window.keypad(True)
        key_press = ""
        i = 0

        while key_press not in (curses.KEY_ENTER, 10, 13):
            current_enemy = enemy_list[abs(i) % len(enemy_list)]

            # Make a box
            red = curses.color_pair(2)
            self.window.addstr(sprite_dictionary[current_enemy].position[0], sprite_dictionary[current_enemy].position[1], sprite_dictionary[current_enemy].state, curses.color_pair(3))
            # self.window.addstr(sprite_dictionary[current_enemy].position[0], sprite_dictionary[current_enemy].position[1], sprite_dictionary[current_enemy].state, curses.color_pair(3))
            
            attack_string = f"Attack {current_enemy.name}"
            # self.window.addstr(20, 20, attack_string, red)
            self.window.addstr(curses.LINES - 10, int(curses.COLS * 0.5), attack_string, red)

            self.window.refresh()

            key_press = self.window.getch()
            match (key_press):
                case curses.KEY_UP:
                    i -= 1
                case curses.KEY_DOWN:
                    i += 1

            self.window.addstr(sprite_dictionary[current_enemy].position[0], sprite_dictionary[current_enemy].position[1], sprite_dictionary[current_enemy].state, curses.color_pair(1))
            # self.window.addstr(20, 20, " " * len(attack_string))
            self.window.addstr(curses.LINES - 5, int((curses.COLS - len(attack_string)) * 0.5), " " * len(attack_string))

        return current_enemy

class Actions(Display):
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(self.height, self.width, self.coordinates[0], self.coordinates[1])
        self.add_actions()

    def add_actions(self):
        self.window.addstr(int(self.height * 0.5), int(curses.COLS * 0.20)-4, "ATTACK 🗡️")
        self.window.addstr(int(self.height * 0.5), int(curses.COLS * 0.40)-4, "DODGE 💨")
        self.window.addstr(int(self.height * 0.5), int(curses.COLS * 0.60)-3, "HEAL 💊")
        self.window.addstr(int(self.height * 0.5), int(curses.COLS * 0.80)-3, "QUIT 😰")

    def display_turn(self, name):
        self.create_border()
        turn_string = f"{name}'s turn".upper()
        self.window.addstr(0, int((curses.COLS - len(turn_string)) * 0.5), turn_string)
        self.window.refresh()

    def select_action(self):
        self.window.keypad(True)
        key_press = ""
        i = 1
        self.window.refresh()

        while key_press not in (curses.KEY_ENTER, 10, 13):
            centres = [0.80, 0.20, 0.40, 0.60]
            centre = centres[abs(i) % 4]
            height = int(curses.LINES * 0.275)

            # Make a box
            blue = curses.color_pair(4)
            self.window.addstr(int(height * 0.5) - 2, int(curses.COLS * centre - 5), "-----------", blue)
            self.window.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) + 5, "⎪", blue)
            self.window.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) - 5, "⎪", blue)
            self.window.addstr(int(height * 0.5), int(curses.COLS * centre) - 5, "-----------", blue)

            self.window.refresh()
    
            key_press = self.window.getch()
            match (key_press):
                case curses.KEY_LEFT:
                    i -= 1
                case curses.KEY_RIGHT:
                    i += 1
    
            if i <= -1:
                i = 4
    
            self.window.addstr(int(height * 0.5) - 2, int(curses.COLS * centre) - 5, "           ")
            self.window.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) + 5, " ")
            self.window.addstr(int(height * 0.5) - 1, int(curses.COLS * centre) - 5, " ")
            self.window.addstr(int(height * 0.5), int(curses.COLS * centre) - 5, "           ")
    
        self.window.refresh()
        return i % 4
