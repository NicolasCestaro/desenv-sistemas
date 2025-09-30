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
    nome = input("digite o nome do produto: ")
    quantidade = int(input("digite a quantidade: "))
    preco = float(input("digite o preço: "))
except ValueError:
    print("digite o valor corretamente")
else:
    # montar o objeto
    novo_produto = {
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