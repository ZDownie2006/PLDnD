#!/usr/bin/env python3

import curses
import time
import combat_back
import characters
import sys

def attack_vis(window: curses.window, player_pos, enemy_pos):
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("ATTACK!")//2), "ATTACK!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("ATTACK!")//2), "       ")
    window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("OW!")//2), "OW!")
    window.refresh()
    time.sleep(1)
    window.addstr(enemy_pos[0] + 1, enemy_pos[1] - (len("OW!")//2), "   ")

def dodge_vis(window: curses.window, player_pos):
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("RUN AWAY!")//2), "RUN AWAY!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("RUN AWAY!")//2), "         ")

def heal_vis(window: curses.window, player_pos):
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("HEALING UP!")//2), "HEALING UP!")
    window.refresh()
    time.sleep(1)
    window.addstr(player_pos[0] + 1, player_pos[1] - (len("HEALING UP!")//2), "           ")

def fight_vis(window: curses.window):
    window.clear()
    window.box()

    # Create Sprites
    player_pos = (int(curses.LINES * 0.5), int(curses.COLS * 0.25))
    enemy_pos = (int(curses.LINES * 0.5), int(curses.COLS * 0.75))
    window.addstr(enemy_pos[0], enemy_pos[1], "😈")
    window.addstr(player_pos[0], player_pos[1], "😎")

    while (True):
        action = window.get_wch()
        match (action):
            case "1":
                attack_vis(window, player_pos, enemy_pos)
            case "2":
                dodge_vis(window, player_pos)
            case "3":
                heal_vis(window, player_pos)
        
        window.refresh()  # Refresh
