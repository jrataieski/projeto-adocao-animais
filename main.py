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
            cachorros.append(cachorro)  # Adiciona o cachorro à lista de cachorros

        elif tipo_animal == "2":
            gato = cadastrar_gato()
            gatos.append(gato)  # Adiciona o gato à lista de gatos
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
        