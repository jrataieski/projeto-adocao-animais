from cadastro import cadastrar_cachorro, cadastrar_gato, cadastrar_adotante

adotantes = []
gatos = []
cachorros = []
animais_adotados = []


while True:
    print("\n=== MENU DE ADOÇÃO ===")
    print("1. Cadastrar animal")
    print("2. Cadastrar adotante")
    print("3. Registrar adoção")
    print("4. Consultar animais cadastrados")
    print("5. Consultar adotantes cadastrados")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n=== CADASTRO DE ANIMAL ===")
        print("1. Cadastrar cachorro")
        print("2. Cadastrar gato")
        tipo_animal = input("Escolha o tipo de animal: ")

        if tipo_animal == "1":
            cachorro = cadastrar_cachorro()
            cachorros.append(cachorro)  
        elif tipo_animal == "2":
            gato = cadastrar_gato()
            gatos.append(gato)  
        else:
            print("Opção inválida.")

    elif opcao == "2":
        print("\n=== CADASTRO DE ADOTANTE ===")
        adotante = cadastrar_adotante()
        adotantes.append(adotante)

    elif opcao == "3":
        print("\n=== REGISTRAR ADOÇÃO ===")
        if not adotantes:
            print("Não há adotantes cadastrados.")
            continue

    
    elif opcao == "4":
        print("\n=== CONSULTAR ANIMAIS ===")
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
        print("\n=== CONSULTAR ADOTANTES ===")
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
        print("\nSaindo do sistema. Até logo!")
        break