#!/usr/bin/env python3


class Characters:
    def __init__(
        self,
        name,
        role,
        role_type,
        max_hp,
        hp,
        cur_ac,
        ac,
        at_mod,
        dmg,
        initiative,
        is_alive,
        position,
        healthy_sprite,
        injured_sprite
    ):
        self.name = name
        self.role = role
        self.role_type = role_type
        self.max_hp = max_hp
        self.hp = hp
        self.cur_ac = cur_ac
        self.ac = ac
        self.at_mod = at_mod
        self.dmg = dmg
        self.initiative = initiative
        self.is_alive = is_alive
        self.position = position
        self.healthy_sprite = healthy_sprite
        self.injured_sprite = injured_sprite

        def __str__(self):
            print(self.name)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> str:
        self.__name = name

    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str) -> str:
        self.__role = role

    @property
    def role_type(self) -> str:
        return self.__role_type

    @role_type.setter
    def role_type(self, role_type: str) -> str:
        self.__role_type = role_type

    @property
    def at_mod(self) -> int:
        return self.__at_mod

    @at_mod.setter
    def at_mod(self, at_mod: int) -> int:
        self.__at_mod = at_mod

    @property
    def dmg(self) -> int:
        return self.__dmg

    @dmg.setter
    def dmg(self, dmg: int) -> int:
        self.__dmg = dmg

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative: int) -> int:
        self.__initiative = initiative


fighter = Characters("Steve", "Fighter", "Player", 15, 15, 14, 14, 3, 6, 0, True, (), "😎", "🤕")
mage = Characters("Gandalf", "Mage", "Player", 10, 10, 12, 12, 6, 6, 0, True, (), "🔮", "🤢")
goblin = Characters("Boggard", "Goblin", "Enemy", 12, 12, 14, 14, 5, 2, 0, True, (), "👺", "🐸")
demon = Characters("Asmodeus", "Demon", "Enemy", 15, 15, 12, 12, 4, 4, 0, True, (), "😈", "👿")
