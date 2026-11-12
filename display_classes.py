#!/usr/bin/env python3

import curses
import time

class Display:
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(self.height, self.width, self.coordinates[0], self.coordinates[1])
        self.size = self.window.getmaxyx()

    def create_border(self, ls="|", rs="|", ts="-", bs="-"):
        self.window.border(ls, rs, ts, bs)

    def display_text(self, text="", position=(0, 0), display_time=0.75):
        self.window.addstr(position[0], int(position[1] - (len(text) * 0.5)), text)
        self.window.refresh()
        time.sleep(display_time)
        self.window.addstr(position[0], int(position[1] - (len(text) * 0.5)), " " * len(text))
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
            
            attack_string = f"Attack {current_enemy.name}"
            self.window.addstr(self.height - 2, int(self.width * 0.5) - int(len(attack_string) * 0.5), attack_string, red)

            self.window.refresh()

            key_press = self.window.getch()
            match (key_press):
                case curses.KEY_UP:
                    i -= 1
                case curses.KEY_DOWN:
                    i += 1

            self.window.addstr(sprite_dictionary[current_enemy].position[0], sprite_dictionary[current_enemy].position[1], sprite_dictionary[current_enemy].state, curses.color_pair(1))
            self.window.addstr(self.height - 2, int(self.width * 0.5) - int(len(attack_string) * 0.5), " " * len(attack_string))

        self.window.refresh()
        return current_enemy

class Actions(Display):
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(self.height, self.width, self.coordinates[0], self.coordinates[1])
        self.buttons = self.add_actions()
        

    def add_actions(self):
        action_strings = ["ATTACK 👊", "DODGE 💨", "HEAL 💊", "QUIT 😰"]
        action_buttons = []

        horizontal_placement_ratio = 0.20
        vertical_center_of_actions_display = int(self.height * 0.5)


        for string in action_strings:
            half_of_string_length = int(len(string) * 0.5)
            x_coordinate = int(curses.COLS * horizontal_placement_ratio) - half_of_string_length

            new_button = Button(string, (vertical_center_of_actions_display, x_coordinate))
            action_buttons.append(new_button)
            self.window.addstr(new_button.coordinates[0], new_button.coordinates[1], new_button.string)
            horizontal_placement_ratio += 0.20
            
        self.window.refresh()
        return action_buttons


    def display_turn(self, name):
        self.create_border()
        turn_string = f"{name}'s turn".upper()
        self.window.addstr(0, int((curses.COLS - len(turn_string)) * 0.5), turn_string)
        self.window.refresh()


    def select_action(self):
        self.window.keypad(True)
        key_press = ""
        i = 0
        self.window.refresh()

        while key_press not in (curses.KEY_ENTER, 10, 13):
            current_index = i % len(self.buttons)
            self.buttons[current_index].button_selected(self.window, True)
            self.window.refresh()
            key_press = self.window.getch()

            match (key_press):
                case curses.KEY_LEFT:
                    i -= 1
                case curses.KEY_RIGHT:
                    i += 1
    
            if i <= -1:
                i = 3

            self.buttons[current_index].button_selected(self.window, False)
        
        self.window.refresh()
        return current_index

class Button:
    def __init__(self, string, coordinates):
        self.string = string
        self.width = len(self.string) + 2
        self.height = 3
        self.coordinates = coordinates
        self.standard_text = curses.color_pair(1)
        self.highlighted_text = curses.color_pair(6)

    def button_selected(self, window, selected):
        if selected:
            window.addstr(self.coordinates[0], self.coordinates[1], self.string, self.highlighted_text)
        else:
            window.addstr(self.coordinates[0], self.coordinates[1], self.string, self.standard_text)

        


