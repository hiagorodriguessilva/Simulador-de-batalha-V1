import random

# =========================
# PERSONAGEM BASE (HERANÇA)
# =========================
class Personagem:
    def __init__(self, nome, forca, inteligencia, velocidade, vitalidade):
        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        self.velocidade = velocidade
        self.vitalidade = vitalidade
        self.vivo = True

    def atacar(self, alvo):
        raise NotImplementedError("Subclasses devem sobrescrever atacar()")

    def defender(self, dano):
        defesa = self.calcular_defesa()
        dano_real = max(0, dano - defesa)
        self.vitalidade -= dano_real
        print(f"{self.nome} defendeu {defesa} e recebeu {dano_real} de dano! (HP: {self.vitalidade})")

        if self.vitalidade <= 0:
            self.vivo = False
            print(f"💀 {self.nome} foi derrotado!")

    def calcular_defesa(self):
        return int((self.velocidade + self.inteligencia) / 4)


# ======================
#        HERÓIS
# ======================
class Guerreiro(Personagem):
    def atacar(self, alvo):
        dano = self.forca * 2 + random.randint(0, 5)
        print(f"🗡️ {self.nome} golpeia {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Mago(Personagem):
    def atacar(self, alvo):
        dano = self.inteligencia * 2 + random.randint(0, 8)
        print(f"✨ {self.nome} conjura magia contra {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Arqueiro(Personagem):
    def atacar(self, alvo):
        dano = int((self.velocidade + self.forca) * 1.5) + random.randint(0, 4)
        print(f"🏹 {self.nome} dispara flecha em {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)


# ======================
#       INIMIGOS
# ======================
class Orc(Personagem):
    def atacar(self, alvo):
        dano = self.forca * 2 + random.randint(3, 7)
        print(f"👹 {self.nome} golpeia {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Goblin(Personagem):
    def atacar(self, alvo):
        dano = self.velocidade * 2 + random.randint(0, 3)
        print(f"👺 {self.nome} ataca rapidamente {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Necromante(Personagem):
    def atacar(self, alvo):
        dano = self.inteligencia * 2 + random.randint(0, 10)
        print(f"💀 {self.nome} conjura feitiço sombrio! Dano: {dano}")
        alvo.defender(dano)


# ======================
#     FACTORY METHOD
# ======================
class PersonagemFactory:
    @staticmethod
    def criar_heroi(tipo, nome):
        match tipo.lower():
            case "guerreiro": return Guerreiro(nome, 8, 4, 5, 40)
            case "mago":      return Mago(nome, 3, 9, 4, 30)
            case "arqueiro":  return Arqueiro(nome, 5, 5, 8, 35)
            case _: raise ValueError("Tipo de herói inválido")

    @staticmethod
    def criar_inimigo(tipo):
        match tipo.lower():
            case "orc":        return Orc("Orc", 9, 3, 4, 40)
            case "goblin":     return Goblin("Goblin", 4, 4, 9, 25)
            case "necromante": return Necromante("Necromante", 2, 10, 3, 30)
            case _: raise ValueError("Tipo de inimigo inválido")


# ======================
#       BUILDER
# ======================
class PersonagemBuilder:
    def __init__(self):
        self.nome = "SemNome"
        self.forca = 5
        self.inteligencia = 5
        self.velocidade = 5
        self.vitalidade = 30

    def set_nome(self, nome):
        self.nome = nome
        return self

    def set_forca(self, valor):
        self.forca = valor
        return self

    def set_inteligencia(self, valor):
        self.inteligencia = valor
        return self

    def set_velocidade(self, valor):
        self.velocidade = valor
        return self

    def set_vitalidade(self, valor):
        self.vitalidade = valor
        return self

    def build(self):
        return Personagem(
            self.nome, self.forca,
            self.inteligencia,
            self.velocidade,
            self.vitalidade
        )


# ======================
#     SIMULADOR DE BATALHA
# ======================
def batalha(herois, inimigos):
    print("\n⚔️ INÍCIO DA BATALHA ⚔️\n")

    while any(h.vivo for h in herois) and any(i.vivo for i in inimigos):

        heroi = random.choice([h for h in herois if h.vivo])
        inimigo = random.choice([i for i in inimigos if i.vivo])

        atacante, defensor = random.choice([(heroi, inimigo), (inimigo, heroi)])

        print(f"\n🎯 {atacante.nome} vai atacar {defensor.nome}!")
        atacante.atacar(defensor)

    print("\n🏁 FIM DA BATALHA 🏁")
    print("✨ Heróis venceram!" if any(h.vivo for h in herois) else "☠️ Inimigos venceram!")


# ======================
#   CRIAÇÃO VIA FACTORY
# ======================
herois = [
    PersonagemFactory.criar_heroi("guerreiro", "Guerreiro"),
    PersonagemFactory.criar_heroi("mago", "Mago"),
    PersonagemFactory.criar_heroi("arqueiro", "Arqueiro")
]

inimigos = [
    PersonagemFactory.criar_inimigo("orc"),
    PersonagemFactory.criar_inimigo("goblin"),
    PersonagemFactory.criar_inimigo("necromante")
]

# EXECUTAR BATALHA
batalha(herois, inimigos)
