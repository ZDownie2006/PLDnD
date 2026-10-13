#!/usr/bin/env python3

from playsound3 import playsound
import random


def battle_music():
    files = [
        "sound_effects/dragon_dance_with_demons.mp3",
        "sound_effects/fierce_cat.mp3",
        "sound_effects/japanese_electronic.mp3"
    ]

    return playsound(random.choice(files), block=False)

def victory_music():
    return playsound("sound_effects/victory.mp3", block=False)
