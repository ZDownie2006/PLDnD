#!/usr/bin/env python3

import random


class Characters:
    def __init__(self, name, role, role_type, hp, ac, at_mod, dmg, initiative):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.hp = hp
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg
        self.initiative = initiative

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
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, hp: int) -> int:
        self.__hp = hp

    @property
    def ac(self) -> int:
        return self.__ac

    @ac.setter
    def ac(self, ac: int) -> int:
        self.__ac = ac

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


fighter = Characters("Steve", "Fighter", "Player", 10, 12, 5, 10, 0)
goblin = Characters("Boggard", "Goblin", "Enemy", 8, 15, 4, 7, 0)
