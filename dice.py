#!/usr/bin/env python3

import random
from abc import ABC, abstractmethod

class Dice():
    min_range = 1

    def __init__(self, max_range):
        self.max_range = max_range

    def roll(self):
        return random.randint(self.min_range, self.max_range)

D20 = Dice(20)
D6 = Dice(6)
