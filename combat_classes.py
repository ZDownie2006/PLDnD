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
        self.window.addstr(position[0] + 1, position[1] - (len(text)//2), text)
        self.window.refresh()
        time.sleep(display_time)
        self.window.addstr(position[0] + 1, position[1] - (len(text)//2), " " * len(text))
