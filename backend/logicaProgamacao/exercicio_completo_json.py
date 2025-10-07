import json

# arquivo
arquivo_json = "petshop.json"
petshop = []

# lendo o arquivo json
try:
    with open(arquivo_json, "r") as arquivo:
        petshop = json.load(arquivo)
except FileNotFoundError:
    print("Arquivo não encontrado, criando novo arquivo.")
    with open(arquivo_json, "w") as arquivo:
        json.dump([], arquivo)

# adicionar pet
try:
    id = int(input("Digite o ID do pet: "))
    nome = input("Digite o nome do pet: ")
    raca = input("Digite a raça: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")
    nome_dono = input("Digite o nome do dono: ")
    telefone_dono = input("Digite o telefone do dono: ")

except ValueError:
    print("Digite certo")

novo_pet = {
    "id": id,
    "nome": nome,
    "raca": raca,
    "idade": idade,
    "sexo": sexo,
    "nome_dono": nome_dono,
    "telefone_dono": telefone_dono
}

petshop.append(novo_pet)

with open(arquivo_json, "w") as arquivo:
    json.dump(petshop, arquivo, indent=4)
    
print("Pet adicionado com sucesso.")

# modificar pet
try:
    id_pet_modificar = int(input("Digite o ID do pet para modificar: "))
except ValueError:
    print("ID inválido. Pulando modificação.")
    id_pet_modificar = None

if id_pet_modificar is not None:
    pet_encontrado = False
    for pet in petshop:
        if pet["id"] == id_pet_modificar:
            # nome
            novo = input(f"Novo nome ({pet['nome']}): ")
            if novo:
                pet["nome"] = novo

            # raça
            novo = input(f"Nova raça ({pet['raca']}): ")
            if novo:
                pet["raca"] = novo

            # idade (tratamento para entrada vazia ou inválida)
            novo = input(f"Nova idade ({pet['idade']}): ")
            if novo:
                try:
                    pet["idade"] = int(novo)
                except ValueError:
                    print("Idade inválida. Mantendo a idade anterior.")

            # sexo
            novo = input(f"Novo sexo ({pet['sexo']}): ")
            if novo:
                pet["sexo"] = novo

            # nome do dono
            novo = input(f"Novo dono ({pet['nome_dono']}): ")
            if novo:
                pet["nome_dono"] = novo

            # telefone do dono
            novo = input(f"Novo telefone ({pet['telefone_dono']}): ")
            if novo:
                pet["telefone_dono"] = novo

            pet_encontrado = True
            break

    if pet_encontrado:
        with open(arquivo_json, "w") as arquivo:
            json.dump(petshop, arquivo, indent=4)
        print("Pet modificado com sucesso.")
    else:
        print("ID não encontrado.")

# excluir pet
id_excluir = int(input("Digite o ID do pet para excluir: "))
novo_petshop = [p for p in petshop if p["id"] != id_excluir]
if len(novo_petshop) == len(petshop):
    print("ID não encontrado.")
else:
    with open(arquivo_json, "w") as arquivo:
        json.dump(novo_petshop, arquivo, indent=4)
    print("Pet excluído com sucesso.")

# listar pets
try:
    with open(arquivo_json, "r") as arquivo:
        petshop = json.load(arquivo)
        if not petshop:
            print("Nenhum pet cadastrado.")
        else:
            print("\n---- Lista de Pets ----")
            for pet in petshop:
                print(f"\nID: {pet['id']}")
                print(f"Nome: {pet['nome']}")
                print(f"Raça: {pet['raca']}")
                print(f"Idade: {pet['idade']} anos")
                print(f"Sexo: {pet['sexo']}")
                print(f"Dono: {pet['nome_dono']}")
                print(f"Telefone: {pet['telefone_dono']}")
except FileNotFoundError:
    print("Arquivo não encontrado.")