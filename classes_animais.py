class Cachorro(Animal):
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
