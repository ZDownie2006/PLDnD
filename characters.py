#!/usr/bin/env python3

import random
from enum import Enum


CHARACTERS = []


class PlayerRole(Enum):
    FIGHTER = 1
    MAGE = 2


class EnemyRole(Enum):
    GOBLIN = 1
    DEMON = 2


class RoleType(Enum):
    PLAYER = 1
    ENEMY = 2


class Character:
    def __init__(self, name, role, role_type, max_hp, hp, cur_ac, ac, at_mod, dmg, is_alive,):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.max_hp = max_hp
        self.hp = hp
        self.cur_ac = cur_ac
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg
        self.initiative = random.randint(1, 20)
        self.is_alive = is_alive

    def attack(self, target):
        hit = random.randint(1, 20) + (self.at_mod)
        if hit >= (target.cur_ac):
            (target).hp = (target.hp) - (self.dmg)
        return hit

    def dodge(current):
        current.cur_ac = (current.ac) + 5

    def heal(current):
        if current.hp < current.max_hp:
            heal = random.randint(1, ((current.max_hp) // 3))
            current.hp = current.hp + heal
        if current.hp > current.max_hp:
            current.hp = current.max_hp
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

class Char_Visual:
    def __init__(self, position, healthy_sprite, injured_sprite):
        self.position = position
        self.healthy_sprite = healthy_sprite
        self.injured_sprite = injured_sprite


class Fighter(Character, Char_Visual):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Fighter",
            role_type="Player",
            max_hp=15,
            hp=15,
            cur_ac=14,
            ac=14,
            at_mod=3,
            dmg=6,
            is_alive=True,
            position=(),
            healthy_sprite="😎",
            injured_sprite="🤕",)


class Mage(Character, Char_Visual):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Mage",
            role_type="Player",
            max_hp=10,
            hp=10,
            cur_ac=12,
            ac=12,
            at_mod=6,
            dmg=6,
            is_alive=True,
            position=(),
            healthy_sprite="🔮",
            injured_sprite="🤢",)


class Goblin(Character, Char_Visual):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Goblin",
            role_type="Enemy",
            max_hp=12,
            hp=12,
            cur_ac=14,
            ac=14,
            at_mod=5,
            dmg=2,
            is_alive=True,
            position=(),
            healthy_sprite="👺",
            injured_sprite="🐸",)


class Demon(Character, Char_Visual):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Demon",
            role_type="Enemy",
            max_hp=15,
            hp=15,
            cur_ac=12,
            ac=12,
            at_mod=4,
            dmg=4,
            is_alive=True,
            position=(),
            healthy_sprite="😈",
            injured_sprite="👿",)


class RoleCharacterCount():
    FIGHTER = 0
    MAGE = 0
    GOBLIN = 0
    DEMON = 0


def create_character(role_type, role):
    match role_type:
        case RoleType.PLAYER.value:
            match role:
                case PlayerRole.FIGHTER.value:
                    RoleCharacterCount.FIGHTER = RoleCharacterCount.FIGHTER + 1
                    CHARACTERS.append(Fighter(f"Steve {RoleCharacterCount.FIGHTER}"))
                case PlayerRole.MAGE.value:
                    RoleCharacterCount.MAGE = RoleCharacterCount.MAGE + 1
                    CHARACTERS.append(Mage(f"Gandalf {RoleCharacterCount.MAGE}"))
        case RoleType.ENEMY.value:
            match role:
                case EnemyRole.GOBLIN.value:
                    RoleCharacterCount.GOBLIN = RoleCharacterCount.GOBLIN + 1
                    CHARACTERS.append(Goblin(f"Boggard {RoleCharacterCount.GOBLIN}"))
                case EnemyRole.DEMON.value:
                    RoleCharacterCount.DEMON = RoleCharacterCount.DEMON + 1
                    CHARACTERS.append(Demon(f"Asmodeus {RoleCharacterCount.DEMON}"))


def get_initative_list():
    CHARACTERS.sort(key=lambda x: x.initiative, reverse=True)
    return CHARACTERS
