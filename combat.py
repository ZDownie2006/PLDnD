#!/usr/bin/env python3

import characters
from random import randint
import time


def combat():
    initiative_list = [characters.fighter, characters.goblin]
    while True:

        for i in range(len(initiative_list)):
            attack = 0
            initiative_list[i].cur_ac = initiative_list[i].ac
            if (initiative_list[i].role_type) == "Player":
                move = int(
                    input("Choose your Action: \n 1: Attack, 2: Dodge, 3: Heal\n")
                )
            else:
                move = randint(1, 3)
            if move == 1:
                attack = randint(1, 20) + (initiative_list[i].at_mod)
                print(f"{(initiative_list[i]).name} attacks with a {attack}")
                if initiative_list[-1]:
                    if attack >= (initiative_list[i - 1].cur_ac):
                        print(
                            f"{initiative_list[i].name} hits! dealing {initiative_list[i].dmg} damage to {initiative_list[i - 1].name}!"
                        )
                        initiative_list[i - 1].hp = (initiative_list[i - 1].hp) - (
                            initiative_list[i].dmg
                        )
                    else:
                        print(f"{initiative_list[i].name} Missed! Unfortunate")
                else:
                    if attack >= (initiative_list[i + 1].cur_ac):
                        print(
                            f"{initiative_list[i].name} hits! dealing {initiative_list[i].dmg} damage to {initiative_list[i + 1].name}!"
                        )
                        initiative_list[i + 1].hp = (initiative_list[i + 1].hp) - (
                            initiative_list[i].dmg
                        )
                    else:
                        print(f"{initiative_list[i].name} Missed! Unfortunate")
            elif move == 2:
                initiative_list[i].cur_ac = initiative_list[i].ac + 5
                print(
                    f"{initiative_list[i].name} prepares to dodge new AC: {initiative_list[i].cur_ac}"
                )

            elif move == 3:
                if initiative_list[i].hp < initiative_list[i].max_hp:
                    heal = randint(1, 5)
                    initiative_list[i].hp = initiative_list[i].hp + heal
                    print(f"{initiative_list[i].name} heals for {heal} hp!")
                    if initiative_list[i].hp > initiative_list[i].max_hp:
                        initiative_list[i].hp = initiative_list[i].max_hp
                        print(f"{initiative_list[i].name} healed to full")
                elif initiative_list[i].hp >= initiative_list[i].max_hp:
                    print(f"{initiative_list[i].name} is at full hp")
            else:
                print("please choose a value input")
                move = input()

            time.sleep(2)

        if initiative_list[i].hp <= 0 or initiative_list[i - 1].hp <= 0:

            print(
                f"{initiative_list[i].name} has died!! leaving {initiative_list[i - 1].name} left! on {initiative_list[i - 1].hp}"
            )
            break


combat()
