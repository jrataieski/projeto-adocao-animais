from cadastro import cadastrar_cachorro, cadastrar_gato, cadastrar_adotante
from adocao import Adocao
from relatorios import gerar_relatorio_lotacao, gerar_relatorio_saude, exportar_json # < relatorios json

adotantes = []
gatos = []
cachorros = []
animais_adotados = []


while True:
    print("\nMENU DE ADOÇÃO DE ANIMAIS")
    print("1. Cadastrar animal")
    print("2. Cadastrar adotante")
    print("3. Registrar adoção")
    print("4. Consultar animais cadastrados")
    print("5. Consultar adotantes cadastrados")
    print("6. Gerar Relatórios Municipais")
    print("7. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\nCADASTRO DE ANIMAL")
        print("1. Cadastrar cachorro")
        print("2. Cadastrar gato")
        tipo_animal = input("Escolha o tipo de animal: ")
    

        if tipo_animal == "1":
            cachorro = cadastrar_cachorro()
            cachorros.append(cachorro)
            print("Animal cadastrado com sucesso.")
        elif tipo_animal == "2":
            gato = cadastrar_gato()
            gatos.append(gato)
            print("Animal cadastrado com sucesso.")
        else:
             print("Opção inválida.")

    elif opcao == "2":
        print("\nCADASTRO DE ADOTANTE")
        adotante = cadastrar_adotante()
        adotantes.append(adotante)

    elif opcao == "3":
        print("\nREGISTRAR ADOÇÃO")
        if not adotantes:
            print("Não há adotantes cadastrados.")
            continue

        disponiveis = [a for a in cachorros + gatos if a.disponibilidade]
        if not disponiveis:
            print("Não há animais disponíveis para adoção.")
            continue

        print("\n--- ANIMAIS DISPONÍVEIS ---")
        for i, a in enumerate(disponiveis, start=1):
            print(f"{i}. {a.nome} ({a.especie})")
        escolha_animal= input("Digite o número do animal: ")

        print("\n --- ADOTANTES ---")
        for i, ad in enumerate(adotantes, start=1):
            print(f"{i}. {ad.nome}")
        escolha_adotante = input("Digite o número do adotante: ")

        if not escolha_animal.isdigit() or not escolha_adotante.isdigit():
            print("Digite apenas números.")
            continue

        if not 1 <= int(escolha_animal) <= len(disponiveis) or not 1 <= int(escolha_adotante) <= len(adotantes):
            print("Número fora da lista.")
            continue

        animal = disponiveis[int(escolha_animal) - 1]
        adotante = adotantes[int(escolha_adotante) - 1]

        adocao = Adocao(animal, adotante)
        if adocao.registrar_adocao():
            animais_adotados.append(animal)

    
    elif opcao == "4":
        print("\nCONSULTAR ANIMAIS")
        print("1. Apenas Cachorros")
        print("2. Apenas Gatos")
        print("3. Todos os Animais")
        filtro = input("Escolha o filtro de consulta: ")

        # Mostra qual lista consultar conforme a escolha do usuário
        if filtro == "1":
            animais_consulta = cachorros
            mensagem_vazio = "Nenhum cachorro cadastrado."
            titulo = "Lista de Cachorros"
        elif filtro == "2":
            animais_consulta = gatos
            mensagem_vazio = "Nenhum gato cadastrado."
            titulo = "Lista de Gatos"
        elif filtro == "3":
            animais_consulta = cachorros + gatos
            mensagem_vazio = "Nenhum animal cadastrado."
            titulo = "Lista de Todos os Animais"
        else:
            print("Filtro inválido.")
            continue

        
        if not animais_consulta:
            print(mensagem_vazio)
        else:
            print(f"\n--- {titulo} ---")
            for animal in animais_consulta:
                print("-" * 30)
                print(animal.exibir_ficha_sanitaria())
                print(f"Situação da Adoção: {animal.situacao_adocao}")

    elif opcao == "5":
        print("\nCONSULTAR ADOTANTES")
        if not adotantes:
            print("Nenhum adotante cadastrado.")
        else:
            print("\n--- Lista de Adotantes ---")
            for adotante in adotantes:
                print("-" * 30)
               #comprovante em "Sim" ou "Não" para ficar mais bonito na tela
                comprovante_texto = "Sim" if adotante.comprovante_residencia else "Não"
                
                print(f"Nome: {adotante.nome}")
                print(f"CPF: {adotante.cpf}")
                print(f"Idade: {adotante.idade} anos")
                print(f"Endereço: {adotante.endereco}")
                print(f"Telefone: {adotante.telefone}")
                print(f"Comprovante de residência: {comprovante_texto}")

    elif opcao == "6":
        print("\nRELATÓRIOS MUNICIPAIS")
        print("1. Relatório de Lotação")
        print("2. Relatório de Saúde (Vacinas/Castração)")
        escolha_rel = input("Escolha o relatório desejado: ")

        if escolha_rel == "1":
            rel_lotacao = gerar_relatorio_lotacao(cachorros, gatos)
            salvar = input("Deseja exportar este relatório para JSON? (Sim/Não): ").strip().lower()
            if salvar == "sim":
                exportar_json(rel_lotacao, "relatorio_lotacao.json")
                
        elif escolha_rel == "2":
            rel_saude = gerar_relatorio_saude(cachorros, gatos)
            salvar = input("Deseja exportar este relatório para JSON? (Sim/Não): ").strip().lower()
            if salvar == "sim":
                exportar_json(rel_saude, "relatorio_saude.json")
        else:
            print("Opção inválida.")

    elif opcao == "7": 
        print("\nSaindo do sistema. Até logo!")
        break
    