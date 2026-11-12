#!/usr/bin/env python3

class Checks:
    def __init__(self, initiative_list, target):
        self.initiative_list = initiative_list,
        
    def player_list(initiative_list):
        plist = []
        idx = 0
        for idx in range(len(initiative_list)):
            if (initiative_list[idx].role_type) == "Player" and (
                initiative_list[idx].is_alive
            ) == True:
                plist.append(initiative_list[idx])
            else:
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
            else:
                continue

        return elist


    def hp_check(target) -> bool:
        return (target.hp <= 0)
