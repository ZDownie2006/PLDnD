#!/usr/bin/env python3
from random import randint

import random


class Characters:
    def __init__(
        self,
        name,
        role,
        role_type,
        max_hp,
        hp,
        cur_ac,
        ac,
        at_mod,
        dmg,
        is_alive,
        position,
        healthy_sprite,
        injured_sprite,
    ):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.max_hp = max_hp
        self.hp = hp
        self.cur_ac = cur_ac
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg
        self.initiative = random.randint(1,20)
        self.is_alive = is_alive
        self.position = position
        self.healthy_sprite = healthy_sprite
        self.injured_sprite = injured_sprite

    def attack(self, target):
        hit = randint(1, 20) + (self.at_mod)
        # print(f"{(attacker).name} attacks {(target).name} with a {hit}")
        if hit >= (target.cur_ac):
            # print(f"{attacker.name} hits! dealing {attacker.dmg} damage to {target.name}!")
            (target).hp = (target.hp) - (self.dmg)
        # else:
        # print(f"{attacker.name} Missed! Unfortunate")
        return hit

    def dodge(current):
        current.cur_ac = (current.ac) + 5

    def heal(current):
        if current.hp < current.max_hp:
            heal = randint(1, 5)
            current.hp = current.hp + heal
        # print(f"{current.name} heals for {heal} hp!")
        if current.hp > current.max_hp:
            current.hp = current.max_hp
        # print(f"{current.name} healed to full")
        elif current.hp >= current.max_hp:
            return

    def __str__(self):
        print(self.name)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> str:
        self.__name = name

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str) -> str:
        self.__role = role

    @property
    def role_type(self) -> str:
        return self.__role_type

    @role_type.setter
    def role_type(self, role_type: str) -> str:
        self.__role_type = role_type

    @property
    def at_mod(self) -> int:
        return self.__at_mod

    @at_mod.setter
    def at_mod(self, at_mod: int) -> int:
        self.__at_mod = at_mod

    @property
    def dmg(self) -> int:
        return self.__dmg

    @dmg.setter
    def dmg(self, dmg: int) -> int:
        self.__dmg = dmg

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative: int) -> int:
        self.__initiative = initiative

fighter = Characters("Steve", "Fighter", "Player", 15, 15, 14, 14, 3, 6, True, (), "😎", "🤕")
mage = Characters("Gandalf", "Mage", "Player", 10, 10, 12, 12, 6, 6, True, (), "🔮", "🤢")
goblin = Characters("Boggard", "Goblin", "Enemy", 12, 12, 14, 14, 5, 2, True, (), "👺", "🐸")
demon = Characters("Asmodeus", "Demon", "Enemy", 15, 15, 12, 12, 4, 4, True, (), "😈", "👿")

def get_initative_list():
    characters = [fighter, goblin, demon, mage]
    characters.sort(key=lambda x: x.initiative, reverse=True)
    return characters
