"""Classes Cachorro e Gato para o sistema de adoção.

Esperam uma classe Animal em animal.py com o construtor Animal(nome, especie, idade).
"""

from animal import Animal


class Cachorro(Animal):
    """Animal canino com dados específicos e ficha sanitária própria."""

    def __init__(self, nome, idade, porte, cor, raca, vacinas=False, castrado=False):
        super().__init__(nome, "Cachorro", idade)
        self.porte = porte
        self.cor = cor
        self.raca = raca
        self.vacinas = vacinas
        self.castrado = castrado

    def exibir_ficha_sanitaria(self):
        vacinas = "Sim" if self.vacinas else "Não"
        castracao = "Sim" if self.castrado else "Não"
        return (
            f"Ficha sanitária — {self.nome} (Cachorro)\n"
            f"Idade: {self.idade}\n"
            f"Porte: {self.porte}\n"
            f"Cor: {self.cor}\n"
            f"Raça: {self.raca}\n"
            f"Vacinado: {vacinas}\n"
            f"Castrado: {castracao}"
        )


class Gato(Animal):
    """Animal felino com dados específicos e ficha sanitária própria."""

    def __init__(self, nome, idade, pelagem, cor, raca, vacinas=False, castrado=False):
        super().__init__(nome, "Gato", idade)
        self.pelagem = pelagem
        self.cor = cor
        self.raca = raca
        self.vacinas = vacinas
        self.castrado = castrado

    def exibir_ficha_sanitaria(self):
        vacinas = "Sim" if self.vacinas else "Não"
        castracao = "Sim" if self.castrado else "Não"
        return (
            f"Ficha sanitária — {self.nome} (Gato)\n"
            f"Idade: {self.idade}\n"
            f"Pelagem: {self.pelagem}\n"
            f"Cor: {self.cor}\n"
            f"Raça: {self.raca}\n"
            f"Vacinado: {vacinas}\n"
            f"Castrado: {castracao}"
        )
