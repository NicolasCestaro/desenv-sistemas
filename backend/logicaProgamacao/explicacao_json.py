# {} -> chaves: definir um objeto -> ficha de cadastro -> pessoa, nome,cpf telefone
# [] -> colchetes: definir uma lista -> lista de compras, lista de tarefas
# chave/valor: chave -> telefone descreve o valor -> 449518596



# #sempre importar a json
import json 
inventario = []
#lendo o arquivo json
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando um novo arquivo.")
    with open("loja.json", "w") as arquivo:
        json.dump([], arquivo)
    
try:
    id = int(input("digite o id do produto: "))
    nome = input("digite o nome do produto: ")
    quantidade = int(input("digite a quantidade: "))
    preco = float(input("digite o preço: "))
except ValueError:
    print("digite o valor corretamente")
else:
    # montar o objeto
    novo_produto = {
        "id": id,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "em_estoque": quantidade > 0  # expressao verdadeira ou falsa
    }
    # escrever o objeto no arquivo json
    inventario.append(novo_produto)
    with open("loja.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent=4)  # indent=4 -> Formatar o arquivo json
    print("Produto adicionado com sucesso")

    #modificar protudo no json
    #id -> identificador
    #pão da vó neuza - 1 
    # pão dona benta - 2

    #modificar produto
    id_produto_modificar = int(input("digite o id do produto para modificar: "))
    nova_quantidade = int(input("digite a nova quantidade: "))
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
    inventario = []

produto_encontrado = False
for produto in inventario:
    if produto["id"] == id_produto_modificar:
        produto["quantidade"] = nova_quantidade
        produto["em_estoque"] = nova_quantidade > 0
        produto_encontrado = True
        break
if produto_encontrado:
    with open("loja.json", "w") as arquivo:
        json.dump(inventario, arquivo, indent=4)
    print("Produto modificado com sucesso.")
else:
    print("O produto com id informado não foi encontrado.")


if not produto_encontrado:
        print("O produto com id informado não foi encontrado.")

else:    
    with open("loja.json", "w") as arquivo:
        json.dump(inventario,arquivo, indent=4)
    
#excluir produto no json
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado.")

novo_produto = []
produto_excluido = False
id_produto_excluir = int(input("digite o id do produto para excluir: "))
for produto in inventario:
    if produto["id"] == id_produto_excluir:
        #se o id fr diferente, adiciona o produto na nova lista
        novo_produto.append(produto)
    else:
        print("produto excluido com sucesso")
        produto_excluido = True
        
if not produto_excluido:
    print("O produto com id informado não foi encontrado.")
else:
    with open("loja.json", "w") as arquivo:
        json.dump(novo_produto,arquivo, indent=4)
        print("o arquivo foi atualizado,produto removido")
    #listar produtos do arquivo json
try:
    with open("loja.json", "r") as arquivo:
        inventario = json.load(arquivo)
    if not inventario:
        print("o arquivo está vazio!")
    else:
    print("---- Lista de produtos no inventário ----")

    for produto in inventario:
        print(f"\n-- Produto {produto.get('id')} --")
        print(f" Nome: {produto.get('nome_produto', 'N/A')}")
        print(f" Preço: {produto.get('preco', 0):.2f}")
        print(f" Quantidade: {produto.get('quantidade', 0)} unidades")
        print(f" Em estoque: {produto.get('em_estoque')}")
        
except FileNotFoundError:
    print("Arquivo não encontrado.")
    
    #crud
    #create -> criar
    #read -> ler
    #update -> atualizar
    #delete -> excluir