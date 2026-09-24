#!/usr/bin/env python3

import random

class Characters:
    def __init__(self, name, role, role_type, hp, ac, at_mod, dmg):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.hp = hp
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg

fighter = Characters("Jeff", "Player", "Fighter", 10, 12, 5, 10)
goblin = Characters("Boggard", "Enemy", "Goblin", 8, 15, 3, 7)
