class Animal:
    __contador = 0

    def __init__(self, nome, especie, idade, cor, raca, vacinas=False, castrado = False):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.cor = cor
        self.raca = raca
        self.vacinas = vacinas
        self.castrado = castrado
        self.disponibilidade = True  
        self.__situacao_adocao = "Disponível" #todo o animal comeecara como disponivel
        self.codigo = self.__gerar_codigo()

    @property
    def situacao_adocao(self):
        return self.__situacao_adocao

    def __gerar_codigo(self):
        Animal.__contador += 1
        return f"{self.especie[:3].upper()}-{Animal.__contador:03d}"

    def atualizar_disponibilidade(self, status):
        # Altera se o animal estiver disponivel ou nao
        self.disponibilidade = status
        if not status:
            self.__situacao_adocao = "Adotado"
        else:
            self.__situacao_adocao = "Disponível"

    def detalhe_especifico(self):
        raise NotImplementedError

    def exibir_ficha_sanitaria(self):
        vacinas = "Sim" if self.vacinas else "Não"
        castracao = "Sim" if self.castrado else "Não"
        return (
            f"Ficha sanitária — {self.nome} ({self.especie})\n"
            f"Idade: {self.idade}\n"
            f"{self.detalhe_especifico()}\n"
            f"Cor: {self.cor}\n"
            f"Raça: {self.raca}\n"
            f"Vacinado: {vacinas}\n"
            f"Castrado: {castracao}\n"
            f"Código: {self.codigo}"
        )

class Cachorro(Animal):
    def __init__(self, nome, idade, porte, cor, raca, vacinas=False, castrado=False):
        super().__init__(nome, "Cachorro", idade, cor, raca, vacinas, castrado)
        self.porte = porte

    def detalhe_especifico(self):
        return f"Porte: {self.porte}"


class Gato(Animal):
    def __init__(self, nome, idade, pelagem, cor, raca, vacinas=False, castrado=False):
        super().__init__(nome, "Gato", idade, cor, raca, vacinas, castrado)
        self.pelagem = pelagem

    def detalhe_especifico(self):
        return f"Pelagem: {self.pelagem}"


