#!/usr/bin/env python3


class Characters:
    def __init__(self, name, role, hp, ac, attack, dmg):
        self.name = name
        self.role = role
        self.hp = hp
        self.ac = ac
        self.attack = attack
        self.dmg = dmg


Fighter = Characters("Jeff", "Fighter", 10, 12, 18, 10)
Goblin = Characters("Boggard", "Goblin", 8, 15, 17, 7)
