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
    plist = player_list(initiative_list)
    elist = enemy_list(initiative_list)
    while True:

        for i in range(len(initiative_list)):
            initiative_list[i].cur_ac = initiative_list[i].ac
            current = initiative_list[i]
            if (current.role_type) == "Player":
                print(f"{current.name}: {current.hp} / {current.max_hp}")
                move = int(
                    input(
                        "Choose your Action: \n 1: Attack, 2: Dodge, 3: Heal, 0: Exit\n"
                    )
                )
            else:
                move = randint(1, 3)
            if move == 1:
                if (current.role_type) == "Player":
                    print("Choose your target: ", end='')
                    for idx, enemy in enumerate(elist):
                        print(idx, enemy.name, end=' ')
                    print('')
                    target = elist[int(input())]
                else:
                    idx = randint(0, (len(plist) - 1))
                    target = plist[idx]
                attack(current, target)
                if hp_check(current, target):
                    break
            elif move == 2:
                dodge(current)
            elif move == 3:
                heal(current)
            elif move == 0:
                break
            else:
                print("please choose a value input")
                move = input()

            time.sleep(0.5)

        if current.hp <= 0 or target.hp <= 0:
            break
        if move == 0:
            break

if __name__ == "__main__":
    combat()
