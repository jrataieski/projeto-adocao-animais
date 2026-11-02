"""Funções de cadastro pelo terminal para cães e gatos."""

from classes_animais import Cachorro, Gato


def perguntar_sim_nao(pergunta):
    while True:
        resposta = input(f"{pergunta} (Sim/Não): ").strip().lower()
        if resposta == "sim":
            return True
        if resposta in ("não", "nao"):
            return False
        print("Responda Sim ou Não.")


def pedir_idade():
    while True:
        try:
            return int(input("Idade: "))
        except ValueError:
            print("Digite a idade usando um número inteiro.")


def cadastrar_cachorro():
    print("
Cadastro de cachorro")
    nome = input("Nome: ")
    idade = pedir_idade()
    porte = input("Porte: ")
    cor = input("Cor: ")
    raca = input("Raça: ")
    vacinas = perguntar_sim_nao("Está vacinado?")
    castrado = perguntar_sim_nao("É castrado?")

    cachorro = Cachorro(nome, idade, porte, cor, raca, vacinas, castrado)
    print("
Cachorro cadastrado!")
    print(cachorro.exibir_ficha_sanitaria())
    return cachorro


def cadastrar_gato():
    print("
Cadastro de gato")
    nome = input("Nome: ")
    idade = pedir_idade()
    pelagem = input("Pelagem: ")
    cor = input("Cor: ")
    raca = input("Raça: ")
    vacinas = perguntar_sim_nao("Está vacinado?")
    castrado = perguntar_sim_nao("É castrado?")

    gato = Gato(nome, idade, pelagem, cor, raca, vacinas, castrado)
    print("
Gato cadastrado!")
    print(gato.exibir_ficha_sanitaria())
    return gato
