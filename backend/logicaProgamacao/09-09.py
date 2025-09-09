# Exercício 01
# cadastrar meus produtos
# listar os produtos cadastrados
# alterar em caso de erro
# excluir quando acabar o estoque
# ter um menu para visualizar todas as opções disponíveis

def cadastrar():
    #aqui vou cadastrar todos os produtos da padaria 
    arquivo = open("produtos.txt","a")
    produto = input("produto (nome/preco/quantidade): ")
    arquivo.write(produto + "\n")
    arquivo.close()

def listar():
    #aqui vou listar todos os produtos que foram cadastrados
    try:
        arquivo = open("produtos.txt","r")
        produtos = arquivo.readlines()
        arquivo.close()
        if produtos == []:
            print("nenhum produto cadastrado")
        else:
            for produto in produtos:
                print(produto.strip())
    except:
        print("nenhum produto cadastrado")

def alterar():
    #aqui vai alterar todos os podrutos cadastrados que colocar 
    try:
        arquivo = open("produtos.txt","r")
        produtos = arquivo.readlines()
        arquivo.close()

        print("lista de produtos:")
        for produto in produtos:
            print(produto.strip())

        numero = int(input("numero do produto para alterar: "))
        produtos[numero-1] = input("novo produto (nome/preco/quantidade): ") + "\n"

        arquivo = open("produtos.txt","w")
        arquivo.writelines(produtos)
        arquivo.close()
    except:
        print("erro ao alterar")

def excluir():
    #aqui vou excluir todos os arquivos que adicionar e quiser excluir ou tirar erros que der
    try:
        arquivo = open("produtos.txt","r")
        produtos = arquivo.readlines()
        arquivo.close()

        print("lista de produtos:")
        for produto in produtos:
            print(produto.strip())

        numero = int(input("numero do produto para excluir: "))
        produtos.pop(numero-1)

        arquivo = open("produtos.txt","w")
        arquivo.writelines(produtos)
        arquivo.close()
    except:
        print("erro ao excluir")

while True:
    #aqui vou a lista vai ficar se repitindo ate colocar a opcao 5 para sair 
    print("\n1.cadastrar 2.listar 3.alterar 4.excluir 5.sair")
    opcao = input("escolha: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        break
    else:
        print("opcao invalida")


# exercicio 02
# sou dono de uma consecssionaria de carros e vi o sistema do dono da padaria.Gostaria de um sistema igual para carros

def cadastrar():
    #aqui vou cadastrar todos os carros da consessioria, como fiat, ford, mclaren, bmw
    arquivo = open("carros.txt","a")
    produto = input("carro (nome/preco/quantidade): ")
    arquivo.write(carro + "\n")
    arquivo.close()

    def listar():
    #aqui vou listar todos os carros que tem na concessionaria  que foram cadastrados
    try:
        arquivo = open("carros.txt","r")
        carros = arquivo.readlines()
        arquivo.close()
        if len(carros) == 0:
            print("nenhum carro cadastrado")
        else:
            for i in range(len(carros)):
                print(i+1, carros[i].strip())
    except:
        print("nenhum carro cadastrado")

        def alterar():
    #aqui vai alterar todos os carros cadastrados que colocar 
    try:
        arquivo = open("carros.txt","r")
        carros = arquivo.readlines()
        arquivo.close()

        print("lista de carros:")
        for i in range(len(carros)):
            print(i+1, carros[i].strip())

        numero = int(input("numero do carro para alterar: "))
        carros[numero] = input("novo carro (nome/preco/quantidade): ") + "\n"

        arquivo = open("carros.txt","w")
        arquivo.writelines(carros)
        arquivo.close()
    except:
        print("erro ao alterar")
        
        def excluir():
    #aqui vou excluir todos os carros que vou adicionar e se  quiser excluir ou tirar erros que der
    try:
        arquivo = open("carros.txt","r")
        carros = arquivo.readlines()
        arquivo.close()

        print("lista de carros:")
        for i in range(len(carros)):
            print(i+1, carros[i].strip())

        numero = int(input("numero do carro para excluir: "))
        carros.pop(numero)

        arquivo = open("carros.txt","w")
        arquivo.writelines(carros)
        arquivo.close()
    except:
        print("erro ao excluir")

        while True:
    #aqui vou a lista vai ficar se repitindo ate colocar a opcao 5 para sair ou se colocar um numero ou opcao que nao esta disponivel ele vai dar erro 
    print("\n1.cadastrar 2.listar 3.alterar 4.excluir 5.sair")
    opcao = input("escolha: ")
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        break
    else:
        print("opcao invalida")

# exercicio 03
#explique porque quando tenho mais de um atributo (variavel), torna-se dificil/complicado o uso de arquivos.txt para guardar as informacoes

# com varias variaveis os arquivos.txt ficam dificeis porque voce precisa separar e organizar e ler cada valor na ordem certa,se nao ler em ordem certa vai aumentar a chance do erro