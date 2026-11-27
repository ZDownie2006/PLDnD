#!/usr/bin/env python3

import curses
import time

ENTER_KEYS = (curses.KEY_ENTER, 10, 13)


class Display:
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(
            self.height, self.width, self.coordinates[0], self.coordinates[1]
        )
        self.size = self.window.getmaxyx()

    def create_border(self, ls="|", rs="|", ts="-", bs="-"):
        self.window.border(ls, rs, ts, bs)

    def display_text(self, text="", position=(0, 0), display_time=0.75):
        half_of_text_length = int(len(text) * 0.5)
        x_coordinate = position[0]
        y_coordinate = int(position[1] - half_of_text_length)
        clear_text = " " * len(text)

        self.window.addstr(y_coordinate, x_coordinate, text)
        self.window.refresh()
        time.sleep(display_time)
        self.window.addstr(y_coordinate, x_coordinate, clear_text)
        self.window.refresh()

    def select_target(self, sprite_dictionary, enemy_list):

        # Initialise colors being used
        default_color = curses.color_pair(1)
        red_text = curses.color_pair(2)

        self.window.keypad(True)
        key_press = ""
        enemy_list_index = 0

        # Loop that determines which enemy is selected
        while key_press not in ENTER_KEYS:
            current_enemy = enemy_list[abs(enemy_list_index) % len(enemy_list)]

            # Make a box
            red_background = curses.color_pair(3)
            self.window.addstr(
                sprite_dictionary[current_enemy].position[0],
                sprite_dictionary[current_enemy].position[1],
                sprite_dictionary[current_enemy].state,
                red_background,
            )

            # Initialising attack string and coordinates
            attack_string = f"Attack {current_enemy.name}"
            clear_text = " " * len(attack_string)
            middle_of_display = int(self.width * 0.5)
            half_of_attack_string_length = int(len(attack_string) * 0.5)
            atk_string_coor = (
                self.height - 2,
                middle_of_display - half_of_attack_string_length,
            )

            self.window.addstr(atk_str_coor[0], atk_str_coor[1], atk_string, red_text)
            self.window.refresh()

            # User presses a key
            # Moves highlighted enemy up if up key is pressed
            # Moves highlighted enemy down if down key is pressed
            # Exits the loop if enter/return key is pressed
            key_press = self.window.getch()
            match (key_press):
                case curses.KEY_UP:
                    enemy_list_index -= 1
                case curses.KEY_DOWN:
                    enemy_list_index += 1

            # Clears red background from selected target
            self.window.addstr(
                sprite_dictionary[current_enemy].position[0],
                sprite_dictionary[current_enemy].position[1],
                sprite_dictionary[current_enemy].state,
                default_color,
            )
            self.window.addstr(
                attack_string_coordinates[0], attack_string_coordinates[1], clear_text
            )

        # Return enemy object in enemy_list
        self.window.refresh()
        return current_enemy


class Actions(Display):
    def __init__(self, height=0, width=0, coordinates=(0, 0)):
        self.height = height
        self.width = width
        self.coordinates = coordinates
        self.window = curses.newwin(
            self.height, self.width, self.coordinates[0], self.coordinates[1]
        )
        self.buttons = self.add_actions()

    def add_actions(self):
        action_strings = ["ATTACK 👊", "DODGE 💨", "HEAL 💊", "QUIT 😰"]

        # Holds the button objects for each action
        action_buttons = []

        horizontal_placement_ratio = 0.20
        adjust_placement = 0.20
        vertical_center_of_actions_display = int(self.height * 0.5)

        # Create and display button objects for each action
        for string in action_strings:
            half_of_string_length = int(len(string) * 0.5)
            x_coordinate = (
                int(curses.COLS * horizontal_placement_ratio) - half_of_string_length
            )

            new_button = Button(
                string, (vertical_center_of_actions_display, x_coordinate)
            )
            action_buttons.append(new_button)
            self.window.addstr(
                new_button.coordinates[0], new_button.coordinates[1], new_button.string
            )
            horizontal_placement_ratio += adjust_placement

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

        while key_press not in ENTER_KEYS:
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
            window.addstr(
                self.coordinates[0],
                self.coordinates[1],
                self.string,
                self.highlighted_text,
            )
        else:
            window.addstr(
                self.coordinates[0],
                self.coordinates[1],
                self.string,
                self.standard_text,
            )
