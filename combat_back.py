#!/usr/bin/env python3

from random import randint


def player_list(initiative_list):
    plist = []
    idx = 0
    for idx in range(len(initiative_list)):
        if (initiative_list[idx].role_type) == "Player" and (
            initiative_list[idx].is_alive
        ) == True:
            plist.append(initiative_list[idx])
        elif (initiative_list[idx].role_type) == "Enemy":
            continue
    return plist


def enemy_list(initiative_list):
    elist = []
    idx = 0
    for idx in range(len(initiative_list)):
        if (initiative_list[idx].role_type) == "Enemy" and (
            initiative_list[idx].is_alive
        ) == True:
            elist.append(initiative_list[idx])
        elif (initiative_list[idx].role_type) == "Player":
            continue

    return elist


def attack(attacker, target):
    hit = randint(1, 20) + (attacker.at_mod)
    print(f"{(attacker).name} attacks {(target).name} with a {hit}")
    if hit >= (target.cur_ac):
        print(f"{attacker.name} hits! dealing {attacker.dmg} damage to {target.name}!")
        (target).hp = (target.hp) - (attacker.dmg)
    else:
        print(f"{attacker.name} Missed! Unfortunate")


def dodge(current):
    current.cur_ac = (current.ac) + 5
    print(f"{current.name} prepares to dodge!, New AC {current.cur_ac}")


def heal(current):
    if current.hp < current.max_hp:
        heal = randint(1, 5)
        current.hp = current.hp + heal
        print(f"{current.name} heals for {heal} hp!")
    if current.hp > current.max_hp:
        current.hp = current.max_hp
        print(f"{current.name} healed to full")
    elif current.hp >= current.max_hp:
        print(f"{current.name} is at full hp")


def hp_check(target) -> bool:
    if target.hp <= 0:
        print(f"{target.name} has been defeated!")
        return True
    else:
        return False
