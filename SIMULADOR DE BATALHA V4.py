import random

# ============================================================
# ===============  CLASSE BASE (HERANÇA)  ====================
# ============================================================
class Personagem:
    """
    Classe base (superclasse)
    Heróis e inimigos herdam dela → Herança
    """
    def __init__(self, nome, forca, inteligencia, velocidade, vitalidade):
        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        self.velocidade = velocidade
        self.vitalidade = vitalidade
        self.vivo = True

    def atacar(self, alvo):
        """Método genérico — será sobrescrito (Polimorfismo + Sobrescrita)"""
        pass

    def defender(self, dano):
        defesa = self.calcular_defesa()
        dano_real = max(0, dano - defesa)
        self.vitalidade -= dano_real

        print(f"{self.nome} defendeu {defesa} e recebeu {dano_real} de dano! (HP: {self.vitalidade})")

        if self.vitalidade <= 0:
            self.vivo = False
            print(f"💀 {self.nome} foi derrotado!")

    def calcular_defesa(self):
        """Sobrescrito pelas subclasses se necessário"""
        return int((self.velocidade + self.inteligencia) / 4)


# ============================================================
# ================== HERANÇA + POLIMORFISMO ==================
# ============================================================

class Guerreiro(Personagem):
    def atacar(self, alvo):
        dano = self.forca * 2 + random.randint(0, 5)
        print(f"🗡️ {self.nome} ataca {alvo.nome} causando {dano} de dano!")
        alvo.defender(dano)

class Mago(Personagem):
    def atacar(self, alvo):
        dano = self.inteligencia * 2 + random.randint(0, 8)
        print(f"✨ {self.nome} lança magia em {alvo.nome} causando {dano} de dano!")
        alvo.defender(dano)

class Arqueiro(Personagem):
    def atacar(self, alvo):
        dano = int((self.velocidade + self.forca) * 1.5) + random.randint(0, 4)
        print(f"🏹 {self.nome} dispara flecha em {alvo.nome} causando {dano} de dano!")
        alvo.defender(dano)


# ============================================================
# ================ INIMIGOS (TAMBÉM HERANÇA) =================
# ============================================================

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


# ============================================================
# ===================== PADRÃO 1: FACTORY ====================
# ============================================================

class PersonagemFactory:
    """
    Factory Method: cria personagens sem expor diretamente suas classes.
    """
    @staticmethod
    def criar(tipo, nome):
        tipos = {
            "guerreiro": Guerreiro(nome, 8, 4, 5, 40),
            "mago": Mago(nome, 3, 9, 4, 30),
            "arqueiro": Arqueiro(nome, 5, 5, 8, 35),
            "orc": Orc(nome, 9, 3, 4, 40),
            "goblin": Goblin(nome, 4, 4, 9, 25),
            "necromante": Necromante(nome, 2, 10, 3, 30)
        }
        return tipos.get(tipo.lower())


# ============================================================
# ===================== PADRÃO 2: BUILDER ====================
# ============================================================

class PersonagemBuilder:
    """
    Permite criar personagens totalmente personalizados passo a passo
    """
    def __init__(self, nome):
        self.nome = nome
        self.forca = 5
        self.inteligencia = 5
        self.velocidade = 5
        self.vitalidade = 30

    def set_forca(self, f): self.forca = f; return me
    def set_inteligencia(self, i): self.inteligencia = i; return self
    def set_velocidade(self, v): self.velocidade = v; return self
    def set_vitalidade(self, h): self.vitalidade = h; return self

    def build(self):
        return Personagem(self.nome, self.forca, self.inteligencia, self.velocidade, self.vitalidade)

personagem = (PersonagemBuilder("aldeão")
                .set_forca(10)
                .set_inteligencia(3)
                .set_velocidade(7)
                .set_vitalidade(50)
                .build())
# ============================================================
# ===================== FUNÇÃO DE BATALHA ====================
# ============================================================

def batalha(herois, inimigos):
    """
    herois e inimigos são LISTAS contendo objetos do tipo Personagem.
    Isso demonstra POLIMORFISMO + ARRAYS GENÉRICOS
    """
    print("\n⚔️ INÍCIO DA BATALHA ⚔️\n")

    while any(h.vivo for h in herois) and any(i.vivo for i in inimigos):
        heroi = random.choice([h for h in herois if h.vivo])
        inimigo = random.choice([i for i in inimigos if i.vivo])

        atacante, defensor = random.choice([(heroi, inimigo), (inimigo, heroi)])

        print(f"\n🎯 {atacante.nome} vai atacar {defensor.nome}!")
        atacante.atacar(defensor)

    print("\n🏁 FIM DA BATALHA 🏁")
    print("✨ Heróis venceram!" if any(h.vivo for h in herois) else "☠️ Inimigos venceram!")


# ============================================================
# ===================== CRIAÇÃO COM FACTORY ==================
# ============================================================

herois = [
    PersonagemFactory.criar("guerreiro", "Guerreiro"),
    PersonagemFactory.criar("mago", "Mago"),
    PersonagemFactory.criar("arqueiro", "Arqueiro")
]

inimigos = [
    PersonagemFactory.criar("orc", "Orc"),
    PersonagemFactory.criar("goblin", "Goblin"),
    PersonagemFactory.criar("necromante", "Necromante")
]


# ============================================================
# ===================== EXECUTAR A BATALHA ===================
# ============================================================

batalha(herois, inimigos)
