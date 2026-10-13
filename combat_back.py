#!/usr/bin/env python3


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


def hp_check(target) -> bool:
    if target.hp <= 0:
        print(f"{target.name} has been defeated!")
        return True
    else:
        return False
