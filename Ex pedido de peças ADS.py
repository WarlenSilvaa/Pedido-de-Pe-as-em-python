print("Bem vindo ao Controle de Estoque da Bicicletaria do Warlen da Silva Alfredo")

# Variaveis Globais
listaPeca = []
codigoPeca = 0


# criando def cadastrar_produtos
def cadastrarPeca(codigo):
    print("Bem vindo ao menu de cadastrar produto")
    print("Código do Produto: {}".format(codigo))
    nome = input("Entre com o nome da peça: ")
    fabricante = input("Entre com o fabricante da peça: ")
    valor = int(input("Entre com o valor(R$) da peça: "))
    #inserindo os valores dentro do dicionario
    dicionarioPeca = {"codigo": codigoPeca,
                      "nome": nome,
                      "fabricante": fabricante,
                      "preço": valor}
#adicionando os valores na listaPeca
    listaPeca.append(dicionarioPeca.copy())


# criando def consultar_produtos
def consultarPeca():
    print("Bem vindo ao menu de consultar produto")
    #criando as opções de escolha de consultaPeca
    while True:
        opcao_consultar = input("\nEscolha a opção desejada: \n" +
                                "1-Consultar Todas as Peças\n" +
                                "2-Consultar Peças por Código\n" +
                                "3-Consultar Peças por Fabricante\n" +
                                "4-Retornar\n"
                                ">>")

        if opcao_consultar == "1":
            print("Você escolheu a opção consultar todos as Peças")
            for peca in listaPeca:
                print("---------------------------")
                for key, value in peca.items():
                    print("{}: {}".format(key, value))



        elif opcao_consultar == "2":
            print("Você escolheu a opção consultar Peças por Código")
            Ncodigo = int(input("entre com o codigo da peça:"))
            for peca in listaPeca:
                if peca["codigo"] == Ncodigo:
                    print("---------------------------")
                    for key, value in peca.items():
                        print("{}: {}".format(key, value))
                    print("---------------------------")

        elif opcao_consultar == "3":
            print("Você escolheu a opção consultar Peças por Fabricante")
            Ncodigo = str(input("entre com o fabricante da peça:"))
            for peca in listaPeca:
                if peca["fabricante"] == Ncodigo:
                    print("---------------------------")
                    for key, value in peca.items():
                        print("{}: {}".format(key, value))
                    print("---------------------------")

        elif opcao_consultar == "4":
            return  # sai da função consultarPeca

        else:
            print("Opção Inválida. Tente Novamente")
            continue  # volta ao inicio do laço consultar


# criando def removerr_produtos
def removerPeca():
    print("Bem vindo ao menu de remover produto")
    #inserindo o numero do codigo da peca que deseja remover
    Ncodigo = int(input("Digite o código da peça que deseja remover:"))
    for peca in listaPeca:
        if peca['codigo'] == Ncodigo:
            listaPeca.remove(peca)
            print("produto Removido")


# Main
while True:
    #criando as opções do main
    opcao_principal = input("\nEscolha a opção desejada: \n" +
                            "1-Cadastrar Peças\n" +
                            "2-Consultar Peças\n" +
                            "3-Remover Peças\n" +
                            "4-Sair\n"
                            ">>")

    if opcao_principal == "1":
        codigoPeca += 1
        cadastrarPeca(codigoPeca)

    elif opcao_principal == "2":
        consultarPeca()

    elif opcao_principal == "3":
        removerPeca()

    elif opcao_principal == "4":
        break  # encerra o laço principal

    else:
        print("Opção Inválida. Tente Novamente")
        continue  # volta ao inicio do laço principal
