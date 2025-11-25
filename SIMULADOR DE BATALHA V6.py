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
        """Deve ser sobrescrito nas subclasses."""
        raise NotImplementedError("Subclasses devem implementar atacar()")

    def defender(self, dano):
        defesa = self.calcular_defesa()
        dano_real = max(0, dano - defesa)
        self.vitalidade -= dano_real
        print(f"{self.nome} defendeu {defesa} e recebeu {dano_real} de dano! (HP: {self.vitalidade})")

        if self.vitalidade <= 0 and self.vivo:
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
        print(f"🗡️ {self.nome} ataca {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Mago(Personagem):
    def atacar(self, alvo):
        dano = self.inteligencia * 2 + random.randint(0, 8)
        print(f"✨ {self.nome} lança magia em {alvo.nome}! Dano: {dano}")
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
        print(f"👹 {self.nome} ataca com força bruta {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Goblin(Personagem):
    def atacar(self, alvo):
        dano = self.velocidade * 2 + random.randint(0, 3)
        print(f"👺 {self.nome} ataca rápido {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class Necromante(Personagem):
    def atacar(self, alvo):
        dano = self.inteligencia * 2 + random.randint(0, 10)
        print(f"💀 {self.nome} conjura feitiço sombrio em {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)


# ======================
#  SUBCLASSES ESPECIAIS
# ======================
class ExGeneral(Guerreiro):
    def atacar(self, alvo):
        # ataque especial: maior multiplicador e chance de golpe crítico
        base = self.forca * 2 + random.randint(2, 8)
        crítico = 1
        if random.random() < 0.2:  # 20% chance de crítico
            crítico = 2
            print(f"💥 CRÍTICO! {self.nome} (Ex-General) acerta um golpe devastador!")
        dano = int(base * crítico)
        print(f"🛡️ {self.nome} (Ex-General) ataca {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)

class MagoAnciao(Mago):
    def atacar(self, alvo):
        # ataque especial: dano baseado fortemente em inteligência + efeito extra
        dano = self.inteligencia * 3 + random.randint(5, 12)
        print(f"✨👴 {self.nome} (Mago Ancião) invoca magia ancestral em {alvo.nome}! Dano: {dano}")
        alvo.defender(dano)
        # efeito secundário: reduzir um pouco a velocidade do alvo (simulado)
        if alvo.vivo:
            redução = 1
            alvo.velocidade = max(1, alvo.velocidade - redução)
            print(f"🔻 {alvo.nome} tem sua velocidade reduzida em {redução} (agora {alvo.velocidade})")


# ======================
#     FACTORY METHOD
# ======================
class PersonagemFactory:
    """
    Factory para presets. Retorna instâncias prontas.
    Pode receber overrides opcionais via kwargs.
    """
    @staticmethod
    def criar_heroi(tipo, nome=None, **overrides):
        t = tipo.lower()
        nome = nome or tipo.capitalize()
        # default stats por tipo
        defaults = {
            "guerreiro": (8, 4, 5, 40),
            "mago":     (3, 9, 4, 30),
            "arqueiro": (5, 5, 8, 35)
        }
        if t not in defaults:
            raise ValueError(f"Tipo de herói inválido: {tipo}")

        f, i, v, hp = defaults[t]
        # sobrescrever se passado em overrides
        f = overrides.get("forca", f)
        i = overrides.get("inteligencia", i)
        v = overrides.get("velocidade", v)
        hp = overrides.get("vitalidade", hp)

        if t == "guerreiro":
            return Guerreiro(nome, f, i, v, hp)
        if t == "mago":
            return Mago(nome, f, i, v, hp)
        if t == "arqueiro":
            return Arqueiro(nome, f, i, v, hp)

    @staticmethod
    def criar_inimigo(tipo, nome=None, **overrides):
        t = tipo.lower()
        # defaults para inimigos (nome padrao pode ser o tipo)
        defaults = {
            "orc": (9, 3, 4, 40),
            "goblin": (4, 4, 9, 25),
            "necromante": (2, 10, 3, 30)
        }
        if t not in defaults:
            raise ValueError(f"Tipo de inimigo inválido: {tipo}")

        f, i, v, hp = defaults[t]
        f = overrides.get("forca", f)
        i = overrides.get("inteligencia", i)
        v = overrides.get("velocidade", v)
        hp = overrides.get("vitalidade", hp)
        nome = nome or tipo.capitalize()

        if t == "orc":
            return Orc(nome, f, i, v, hp)
        if t == "goblin":
            return Goblin(nome, f, i, v, hp)
        if t == "necromante":
            return Necromante(nome, f, i, v, hp)


# ======================
#        BUILDER
# ======================
class PersonagemBuilder:
    """
    Builder que aceita escolha de classe (por string), nome e distribuição de pontos.
    Validação da classe: se inválida -> ValueError (opção A).
    Ao build() retorna uma instância da subclasse correta (Guerreiro/Mago/Arqueiro).
    """
    CLASSES_VALIDAS = {"guerreiro", "mago", "arqueiro", "orc", "goblin", "necromante", "exgeneral", "magoanciao"}

    def __init__(self):
        self._classe = None
        self._nome = "SemNome"
        # valores base neutros, você deve setar de acordo com a classe desejada
        self._forca = 5
        self._inteligencia = 5
        self._velocidade = 5
        self._vitalidade = 30

    def set_classe(self, classe_str):
        if not isinstance(classe_str, str):
            raise ValueError("Classe deve ser uma string.")
        chave = classe_str.strip().lower()
        if chave not in self.CLASSES_VALIDAS:
            raise ValueError(f"Classe inválida: {classe_str}")
        self._classe = chave
        return self

    def set_nome(self, nome):
        self._nome = nome
        return self

    def set_forca(self, valor):
        self._forca = int(valor)
        return self

    def set_inteligencia(self, valor):
        self._inteligencia = int(valor)
        return self

    def set_velocidade(self, valor):
        self._velocidade = int(valor)
        return self

    def set_vitalidade(self, valor):
        self._vitalidade = int(valor)
        return self

    def build(self):
        if not self._classe:
            raise ValueError("Classe não definida. Use set_classe('guerreiro'|'mago'|'arqueiro'|...)")

        c = self._classe

        # permitir criação de subclasses especiais via nomes curtos
        if c == "guerreiro":
            return Guerreiro(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "mago":
            return Mago(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "arqueiro":
            return Arqueiro(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "orc":
            return Orc(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "goblin":
            return Goblin(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "necromante":
            return Necromante(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "exgeneral":
            # ExGeneral é subclasse de Guerreiro, mas o builder permite criá-lo diretamente
            return ExGeneral(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)
        if c == "magoanciao":
            return MagoAnciao(self._nome, self._forca, self._inteligencia, self._velocidade, self._vitalidade)

        # (nunca chega aqui por causa da validação)
        raise ValueError(f"Classe não suportada: {self._classe}")


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
#    EXEMPLOS / DEMO
# ======================

if __name__ == "__main__":
    # --- Usando Factory (presets) ---
    heroi1 = PersonagemFactory.criar_heroi("guerreiro", "GuerreiroPadrao")
    heroi2 = PersonagemFactory.criar_heroi("mago", "MagoPadrao")
    heroi3 = PersonagemFactory.criar_heroi("arqueiro", "ArqueiroPadrao")

    # --- Usando Builder (escolhe classe por string + customiza pontos) ---
    ex_general_builder = (
        PersonagemBuilder()
        .set_classe("exgeneral")      # cria a subclasse ExGeneral (ataque especial)
        .set_nome("Ex-General")
        .set_forca(12)
        .set_inteligencia(6)
        .set_velocidade(7)
        .set_vitalidade(60)
        .build()
    )

    mago_anciao_builder = (
        PersonagemBuilder()
        .set_classe("magoanciao")     # cria a subclasse MagoAnciao
        .set_nome("Mago Ancião")
        .set_forca(2)
        .set_inteligencia(16)
        .set_velocidade(3)
        .set_vitalidade(40)
        .build()
    )

    # --- Criando inimigos via Factory e Builder ---
    inimigo1 = PersonagemFactory.criar_inimigo("orc")
    inimigo2 = PersonagemFactory.criar_inimigo("goblin")
    boss_builder = (
        PersonagemBuilder()
        .set_classe("necromante")
        .set_nome("Necromante Supremo")
        .set_forca(3)
        .set_inteligencia(18)
        .set_velocidade(4)
        .set_vitalidade(80)
        .build()
    )

    # montar listas (arrays genéricos de Personagem)
    herois = [heroi1, ex_general_builder, mago_anciao_builder, heroi3]
    inimigos = [inimigo1, inimigo2, boss_builder]

    # iniciar batalha de demonstração
    batalha(herois, inimigos)
