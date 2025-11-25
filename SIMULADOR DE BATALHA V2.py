import random

class Vocation:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.alive = True

    def attack(self, target):
        """Ataque genérico - será modificado pelas subclasses"""
        damage = self.strength + random.randint(0, 10)
        print(f"{self.name} ataca {target.name} causando {damage} de dano!")
        target.defend(damage)

    def defend(self, damage):
        """Defesa genérica - reduz o dano com base na agilidade"""
        defense = int(self.agility * 0.5)
        final_damage = max(0, damage - defense)
        self.health -= final_damage

        print(f"{self.name} defendeu {defense}, recebeu {final_damage} de dano. HP restante: {self.health}")

        if self.health <= 0:
            self.alive = False
            print(f"💀 {self.name} foi derrotado!")

    def is_alive(self):
        return self.alive

    def display_stats(self):
        print(f"\n{self.name}")
        print(f" Health:   {self.health}")
        print(f" Mana:     {self.mana}")
        print(f" Strength: {self.strength}")
        print(f" Agility:  {self.agility}")

class Warrior(Vocation):
    def __init__(self):
        super().__init__("Warrior", 150, 30, 20, 10)

    def attack(self, target):
        damage = self.strength * 2 + random.randint(0, 5)
        print(f"🗡️ {self.name} golpeia {target.name} com força! Dano: {damage}")
        target.defend(damage)


class Archer(Vocation):
    def __init__(self):
        super().__init__("Archer", 100, 50, 12, 18)

    def attack(self, target):
        damage = int((self.strength + self.agility) * 1.5) + random.randint(0, 5)
        print(f"🏹 {self.name} dispara flecha em {target.name}! Dano: {damage}")
        target.defend(damage)


class Mage(Vocation):
    def __init__(self):
        super().__init__("Mage", 80, 120, 8, 12)

    def attack(self, target):
        damage = int(self.mana * 0.3 + random.randint(0, 8))
        print(f"✨ {self.name} lança magia em {target.name}! Dano: {damage}")
        target.defend(damage)

def battle(vocations):
    print("\n⚔️ INÍCIO DO COMBATE ⚔️\n")
    round_num = 1

    while sum(v.is_alive() for v in vocations) > 1:
        print(f"\n===== ROUND {round_num} =====")

        attacker, defender = random.sample([v for v in vocations if v.is_alive()], 2)
        print(f"\n🎯 {attacker.name} vai atacar {defender.name}!")
        attacker.attack(defender)

        round_num += 1

    print("\n🏁 FIM DO COMBATE 🏁")
    for v in vocations:
        status = "VIVO ✅" if v.is_alive() else "MORTO ☠️"
        print(f"{v.name}: {status}")


# ====== Execução principal ======
if __name__ == "__main__":
    vocations = [Warrior(), Archer(), Mage()]
    for v in vocations:
        v.display_stats()

    battle(vocations)
