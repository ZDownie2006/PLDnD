#!/usr/bin/env python3

import characters
from random import randint
import time
from combat_back import hp_check, player_list, enemy_list


def combat():
    initiative_list = characters.get_initiative_list()

    game_state = True
    while game_state == True:
        plist = player_list(initiative_list)
        elist = enemy_list(initiative_list)

        for character in initiative_list:
            character.cur_ac = character.ac
            current = character
            if (current.role_type) == "Player":
                try:
                    move = int(input())
                except ValueError:
                    break
            else:
                move = randint(1, 3)
            match move:
                case 1:
                    target = None
                    if (current.role_type) == "Player":
                        while target == None:
                            try:
                                target = elist[int(input())]
                            except IndexError, ValueError:
                                continue
                    else:
                        idx = randint(0, (len(plist) - 1))
                        target = plist[idx]
                    current.attack(target)
                    if hp_check(target):
                        target.is_alive = False
                        initiative_list.remove(target)
                        if plist and not elist:
                            print("Players win")
                            game_state = False
                            break
                        if elist and not plist:
                            print("Enemies Win")
                            game_state = False
                            break
                case 2:
                    current.dodge(current)
                case 3:
                    current.heal(current)
                case 0:
                    game_state = False
                    break
                case _:
                    break
            plist = player_list(initiative_list)
            elist = enemy_list(initiative_list)

            time.sleep(0.5)


if __name__ == "__main__":
    combat()
