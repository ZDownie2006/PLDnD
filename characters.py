#!/usr/bin/env python3

import dice
from enum import Enum
import random


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

"""Class to delcare the characters checks & base information"""
class Character:
    def __init__(self, name, role, role_type, is_alive,):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.initiative = dice.D20.roll()
        self.is_alive = is_alive

    def __str__(self):
        print(self.name)



"""Class to declare and initialise the visual aspects of the characters"""
class Char_Visual:
    def __init__(self, position, healthy_sprite, injured_sprite):
        self.position = position
        self.healthy_sprite = healthy_sprite
        self.injured_sprite = injured_sprite


"""Class Stats and combat information"""
class Char_Stats:
    def __init__(self, max_hp, hp, cur_ac, ac, at_mod, dmg, dmg_dice):
        self.max_hp = max_hp
        self.hp = hp
        self.cur_ac = cur_ac
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg
        self.dmg_dice = dmg_dice
    
    def attack(self, target):
        hit = dice.D20.roll() + (self.at_mod)
        if hit >= (target.cur_ac):
            self.damage(target)
        return hit

    def damage(self, target):
        (target).hp = (target.hp) - (self.dmg.roll())

    def dodge(current):
        current.cur_ac = (current.ac) + ((current.ac) // 2)

    def heal(current):
        if current.hp < current.max_hp:
            heal = random.randint(1, ((current.max_hp) // 3))
            current.hp = min((current.hp + heal), current.max_hp)


"""Class initialisation"""
class Fighter(Character, Char_Visual, Char_Stats):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Fighter",
            role_type="Player",
            is_alive=True,)
        Char_Visual.__init__(
            self,
            position=(),
            healthy_sprite="😎",
            injured_sprite="🤕",)
        Char_Stats.__init__(
            self,
            max_hp=15,
            hp=15,
            cur_ac=14,
            ac=14,
            at_mod=3,
            dmg=dice.D8,
            dmg_dice="D8",
        )

class Mage(Character, Char_Visual, Char_Stats):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Mage",
            role_type="Player",
            is_alive=True,)
        Char_Visual.__init__(
            self,
            position=(),
            healthy_sprite="🔮",
            injured_sprite="🤢",
        )
        Char_Stats.__init__(
            self,
            max_hp=10,
            hp=10,
            cur_ac=12,
            ac=12,
            at_mod=6,
            dmg=dice.D6,
            dmg_dice="D6",
        )


class Goblin(Character, Char_Visual, Char_Stats):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Goblin",
            role_type="Enemy",
            is_alive=True,)
        Char_Visual.__init__(
            self,
            position=(),
            healthy_sprite="👺",
            injured_sprite="🐸",)
        Char_Stats.__init__(
            self,
            max_hp=12,
            hp=12,
            cur_ac=14,
            ac=14,
            at_mod=6,
            dmg=dice.D4,
            dmg_dice="D4",
        )


class Demon(Character, Char_Visual, Char_Stats):
    def __init__(self, name):
        Character.__init__(
            self,
            name,
            role="Demon",
            role_type="Enemy",
            is_alive=True,)
        Char_Visual.__init__(
            self,
            position=(),
            healthy_sprite="😈",
            injured_sprite="👿",)
        Char_Stats.__init__(
            self,
            max_hp=15,
            hp=15,
            cur_ac=12,
            ac=12,
            at_mod=4,
            dmg=dice.D6,
            dmg_dice="D6",
        )


class RoleCharacterCount():
    FIGHTER = 0
    MAGE = 0
    GOBLIN = 0
    DEMON = 0


class Names:
    def player_name():
        names = ["Steve", "Gandalf", "Joe", "Jonathan", "Chris"]
        return (random.choice(names))

    def enemy_name():
        names = ["Boggard", "Asmodeus", "Lut", "Lucifer", "Gricko"]
        return (random.choice(names))




def create_character(role_type, role):
    match role_type:
        case RoleType.PLAYER.value:
            match role:
                case PlayerRole.FIGHTER.value:
                    RoleCharacterCount.FIGHTER = RoleCharacterCount.FIGHTER + 1
                    CHARACTERS.append(Fighter(f"{Names.player_name()} {RoleCharacterCount.FIGHTER}"))
                case PlayerRole.MAGE.value:
                    RoleCharacterCount.MAGE = RoleCharacterCount.MAGE + 1
                    CHARACTERS.append(Mage(f"{Names.player_name()} {RoleCharacterCount.MAGE}"))
        case RoleType.ENEMY.value:
            match role:
                case EnemyRole.GOBLIN.value:
                    RoleCharacterCount.GOBLIN = RoleCharacterCount.GOBLIN + 1
                    CHARACTERS.append(Goblin(f"{Names.enemy_name()} {RoleCharacterCount.GOBLIN}"))
                case EnemyRole.DEMON.value:
                    RoleCharacterCount.DEMON = RoleCharacterCount.DEMON + 1
                    CHARACTERS.append(Demon(f"{Names.enemy_name()} {RoleCharacterCount.DEMON}"))


def get_initative_list():
    CHARACTERS.sort(key=lambda x: x.initiative, reverse=True)
    return CHARACTERS
