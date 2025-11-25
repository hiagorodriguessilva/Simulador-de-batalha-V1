import random

class Vocation:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.alive = True

    def display_stats(self):
        print(f"\n{self.name}")
        print(f" Health:   {self.health}")
        print(f" Mana:     {self.mana}")
        print(f" Strength: {self.strength}")
        print(f" Agility:  {self.agility}")

    def attack(self, target):
        """Método genérico de ataque"""
        damage = self.strength + random.randint(1, 6)
        print(f"{self.name} ataca {target.name} causando {damage} de dano!")
        target.defend(damage)

    def defend(self, damage):
        """Método genérico de defesa"""
        defense = random.randint(0, int(self.agility / 2))
        real_damage = max(0, damage - defense)
        self.health -= real_damage
        print(f"{self.name} defendeu {defense} e recebeu {real_damage} de dano! (HP: {self.health})")

        if self.health <= 0:
            self.alive = False
            print(f"💀 {self.name} foi derrotado!")


# ====== Classes concretas ======
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
        damage = int((self.strength + self.agility) * 1.3) + random.randint(0, 4)
        print(f"🏹 {self.name} dispara flecha em {target.name}! Dano: {damage}")
        target.defend(damage)


class Mage(Vocation):
    def __init__(self):
        super().__init__("Mage", 80, 120, 8, 12)

    def attack(self, target):
        damage = int(self.mana * 0.2) + random.randint(0, 8)
        print(f"✨ {self.name} lança magia em {target.name}! Dano: {damage}")
        target.defend(damage)


# ====== Simulação com log ======
if __name__ == "__main__":
    hero1 = Warrior()
    hero2 = Archer()
    hero3 = Mage()

    enemies = [
        Vocation("Orc", 140, 20, 18, 8),
        Vocation("Goblin", 90, 30, 10, 16),
        Vocation("Necromancer", 100, 150, 6, 10)
    ]

    heroes = [hero1, hero2, hero3]

    print("\n=== INÍCIO DA BATALHA ===\n")

    # Loop de rodadas
    round_count = 1
    while any(h.alive for h in heroes) and any(e.alive for e in enemies):
        print(f"\n===== RODADA {round_count} =====")

        hero = random.choice([h for h in heroes if h.alive])
        enemy = random.choice([e for e in enemies if e.alive])

        attacker, defender = random.choice([(hero, enemy), (enemy, hero)])

        print(f"\n🎯 {attacker.name} ataca {defender.name}!")
        attacker.attack(defender)

        round_count += 1

    print("\n🏁 FIM DA BATALHA 🏁")
    if any(h.alive for h in heroes):
        print("✨ Os heróis venceram!")
    else:
        print("☠️ Os inimigos venceram!")
