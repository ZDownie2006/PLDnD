#!/usr/bin/env python3

from playsound3 import playsound
import random


def battle_music():
    files = [
    ]

    return playsound(random.choice(files), block=False)

def victory_music():
    return playsound("", block=False)
