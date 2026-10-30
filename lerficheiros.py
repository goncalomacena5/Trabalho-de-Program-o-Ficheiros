def pedir_frutas():
    while True:
        try:
            num_frutas = int(input("Quantas frutas deseja adicionar? "))
            if num_frutas > 0:
                break
            print("O número de frutas deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    frutas = []
    while len(frutas) < num_frutas:
        fruta = input("Nome da fruta: ").strip()
        if fruta == "":
            print("O nome não pode estar vazio.")
        elif fruta in frutas:
            print(f"A fruta {fruta} já está na lista.")
        else:
            frutas.append(fruta)
            print(f"A fruta {fruta} foi adicionada.")
    return frutas


print("PROGRAMA FRUTAS")
print()
nome = input("Nome do ficheiro a ler/escrever: ")

opcao = ""
while opcao != "0":
    print()
    print("* Opções:")
    print("1) Ler o ficheiro")
    print("2) Acrescentar ao ficheiro")
    print("3) Criar/Sobrescrever o ficheiro")
    print("0) Sair")
    print()
    opcao = input("> ")

    if opcao == "1":
        try:
            with open(nome, "r", encoding="utf-8") as f:
                print("Conteúdo do ficheiro:")
                print(f.read())
        except FileNotFoundError:
            print(f"O ficheiro '{nome}' não existe.")

    elif opcao == "2":
        frutas = pedir_frutas()
        with open(nome, "a", encoding="utf-8") as f:
            for fruta in frutas:
                f.write(fruta + "\n")
        print("Frutas acrescentadas ao ficheiro.")

    elif opcao == "3":
        frutas = pedir_frutas()
        with open(nome, "w", encoding="utf-8") as f:
            for fruta in frutas:
                f.write(fruta + "\n")
        print("Ficheiro criado/sobrescrito.")

    elif opcao == "0":
        print("Adeus!")

    else:
        print("Opção inválida.")