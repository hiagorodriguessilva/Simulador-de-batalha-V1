import random

# ===== Classe base =====
class Vocation:
    def __init__(self, name, health, mana, strength, agility):
        self.name = name
        self.health = health
        self.mana = mana
        self.strength = strength
        self.agility = agility
        self.alive = True

    def attack(self, target):
        """Método genérico, reimplementado nas subclasses"""
        pass

    def defend(self, damage):
        """Reduz o dano baseado na agilidade"""
        defense = self.calculate_defense()
        real_damage = max(0, damage - defense)
        self.health -= real_damage
        print(f"{self.name} defendeu {defense} e recebeu {real_damage} de dano. (HP: {self.health})")

        if self.health <= 0:
            self.alive = False
            print(f"💀 {self.name} foi derrotado!")

    def calculate_defense(self):
        """Cálculo genérico de defesa"""
        return int(self.agility * 0.5)

    def display_stats(self):
        print(f"\n{self.name}")
        print(f" Health:   {self.health}")
        print(f" Mana:     {self.mana}")
        print(f" Strength: {self.strength}")
        print(f" Agility:  {self.agility}")


# ====== Heróis ======
class Warrior(Vocation):
    def __init__(self):
        super().__init__("Warrior", 150, 30, 20, 10)

    def attack(self, target):
        damage = self.strength * 2 + random.randint(0, 5)
        print(f"🗡️ {self.name} ataca {target.name} com espada! Dano: {damage}")
        target.defend(damage)


class Archer(Vocation):
    def __init__(self):
        super().__init__("Archer", 100, 50, 12, 18)

    def attack(self, target):
        damage = int((self.strength + self.agility) * 1.5) + random.randint(0, 4)
        print(f"🏹 {self.name} dispara flecha em {target.name}! Dano: {damage}")
        target.defend(damage)


class Mage(Vocation):
    def __init__(self):
        super().__init__("Mage", 80, 120, 8, 12)

    def attack(self, target):
        damage = self.mana * 0.3 + self.strength + random.randint(0, 10)
        print(f"✨ {self.name} lança magia em {target.name}! Dano: {int(damage)}")
        target.defend(int(damage))


# ====== Inimigos ======
class Enemy(Vocation):
    pass

class Orc(Enemy):
    def __init__(self):
        super().__init__("Orc", 140, 20, 18, 8)

    def attack(self, target):
        damage = self.strength * 2 + random.randint(3, 7)
        print(f"👹 {self.name} golpeia {target.name}! Dano: {damage}")
        target.defend(damage)


class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 90, 30, 10, 16)

    def attack(self, target):
        damage = self.agility * 1.8 + random.randint(0, 5)
        print(f"👺 {self.name} ataca rapidamente {target.name}! Dano: {int(damage)}")
        target.defend(int(damage))


class Necromancer(Enemy):
    def __init__(self):
        super().__init__("Necromancer", 100, 150, 6, 10)

    def attack(self, target):
        damage = self.mana * 0.25 + random.randint(5, 12)
        print(f"💀 {self.name} conjura feitiço sombrio contra {target.name}! Dano: {int(damage)}")
        target.defend(int(damage))


# ====== Função de batalha ======
def battle(heroes, enemies):
    print("\n⚔️ INÍCIO DA BATALHA ⚔️\n")

    while any(h.alive for h in heroes) and any(e.alive for e in enemies):
        hero = random.choice([h for h in heroes if h.alive])
        enemy = random.choice([e for e in enemies if e.alive])

        # Aleatoriza quem ataca primeiro
        attacker, defender = random.choice([(hero, enemy), (enemy, hero)])

        print(f"\n🎯 {attacker.name} vai atacar {defender.name}!")
        attacker.attack(defender)

    print("\n🏁 FIM DA BATALHA 🏁")
    if any(h.alive for h in heroes):
        print("✨ Os heróis venceram!")
    else:
        print("☠️ Os inimigos venceram!")


# ====== Execução principal ======
if __name__ == "__main__":
    heroes = [Warrior(), Archer(), Mage()]
    enemies = [Orc(), Goblin(), Necromancer()]

    # Mostrar status antes da luta
    print("=== HERÓIS ===")
    for h in heroes:
        h.display_stats()

    print("\n=== INIMIGOS ===")
    for e in enemies:
        e.display_stats()

    # Iniciar batalha
    battle(heroes, enemies)