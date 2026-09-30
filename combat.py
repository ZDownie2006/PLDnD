#!/usr/bin/env python3

import characters
from random import randint
import time
from combat_back import attack, dodge, heal


def combat():
    initiative_list = [characters.fighter, characters.goblin]
    while True:

        for i in range(len(initiative_list)):
            initiative_list[i].cur_ac = initiative_list[i].ac
            if (initiative_list[i].role_type) == "Player":
                move = int(
                    input(
                        "Choose your Action: \n 1: Attack, 2: Dodge, 3: Heal, 0: Exit\n"
                    )
                )
            else:
                move = randint(1, 3)
            if move == 1:
                # the use of -1 is to target the previous character, i.e goblin attacking fighter
                attack(initiative_list[i], initiative_list[i - 1])
            elif move == 2:
                dodge(initiative_list[i])
            elif move == 3:
                heal(initiative_list[i])
            elif move == 0:
                break
            else:
                print("please choose a value input")
                move = input()

            time.sleep(2)

        if initiative_list[i].hp <= 0 or initiative_list[i - 1].hp <= 0:

            print(
                f"{initiative_list[i].name} has died!! leaving {initiative_list[i - 1].name} left! on {initiative_list[i - 1].hp}"
            )
            break
        if move == 0:
            break


combat()
