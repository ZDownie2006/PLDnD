#!/usr/bin/env python3

import characters
from random import randint
import time
from combat_back import attack, dodge, heal, hp_check, player_list, enemy_list


def combat():
    initiative_list = [
        characters.fighter,
        characters.goblin,
        characters.demon,
        characters.mage,
    ]
    game_state = True
    while game_state == True:
        plist = player_list(initiative_list)
        elist = enemy_list(initiative_list)

        for character in initiative_list:
            character.cur_ac = character.ac
            current = character
            if (current.role_type) == "Player":
                print(f"{current.name}: {current.hp} / {current.max_hp}")
                try:
                    move = int(
                        input(
                            "Choose your Action: \n 1: Attack, 2: Dodge, 3: Heal, 0: Exit\n"
                        )
                    )
                except ValueError:
                    print("Choose a valid input")
                    break
            else:
                move = randint(1, 3)
            match move:
                case 1:
                    target = None
                    if (current.role_type) == "Player":
                        print("Choose your target: ", end='')
                        for idx, enemy in enumerate(elist):
                            print(idx, enemy.name, end=' ')
                        print('')
                        while target == None:
                            try:
                                target = elist[int(input())]
                            except IndexError, ValueError:
                                print("invalid option")
                    else:
                        idx = randint(0, (len(plist) - 1))
                        target = plist[idx]
                    attack(current, target)
                    if hp_check(target):
                        target.is_alive = False
                        initiative_list.remove(target)
                        plist = player_list(initiative_list)
                        elist = enemy_list(initiative_list)
                        if plist and not elist:
                            print("Players win")
                            game_state = False
                            break
                        if elist and not plist:
                            print("Enemies Win")
                            game_state = False
                            break
                case 2:
                    dodge(current)
                case 3:
                    heal(current)
                case 0:
                    break
                case _:
                    print("please choose a value input")
                    break

            time.sleep(0.5)
        try:
            if move == 0:
                break
        except UnboundLocalError:
            continue


if __name__ == "__main__":
    combat()
