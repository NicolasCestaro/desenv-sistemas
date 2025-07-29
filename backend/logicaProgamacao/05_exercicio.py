# soma = 0
# for i in range(1, 21):
#     soma = soma + i
# print("Soma de 1 a 20:", soma)


# soma2 = 0
# numero = int(input("Digite um número (0 para parar): "))

# while numero != 0:
#     soma2 = soma2 + numero
#     numero = int(input("Digite um número (0 para parar): "))

# print("Soma dos números digitados:", soma2)



# senha = input("Digite a senha: ")

# while senha != senha_correta:
#     print("Senha inválida")
#     senha = input("Digite a senha: ")

# print("Acesso permitido")


# pedir nome e senha ao usuario 

# mostrar "bem vindo" quando acertara senha e o nome 

# apos pedir o salario do usuario 

# mostrar salario anual 

# se o salario anual for maior que 100mil mostrar mensagem "rico"

nome = ""
senha = ""

while nome == "" or senha == "":
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")

print("Bem-vindo")

salario = float(input("Digite seu salário mensal: "))
salario_anual = salario * 12

print("Seu salário anual é:", salario_anual)

if salario_anual > 100000:
    print("Rico")

