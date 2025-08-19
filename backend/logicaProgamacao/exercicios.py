# # # # # # # soma = 0
# # # # # # # for i in range(1, 21):
# # # # # # #     soma = soma + i
# # # # # # # print("Soma de 1 a 20:", soma)


# # # # # # # soma2 = 0
# # # # # # # numero = int(input("Digite um número (0 para parar): "))

# # # # # # # while numero != 0:
# # # # # # #     soma2 = soma2 + numero
# # # # # # #     numero = int(input("Digite um número (0 para parar): "))

# # # # # # # print("Soma dos números digitados:", soma2)



# # # # # # # senha = input("Digite a senha: ")

# # # # # # # while senha != senha_correta:
# # # # # # #     print("Senha inválida")
# # # # # # #     senha = input("Digite a senha: ")

# # # # # # # print("Acesso permitido")


# # # # # # # pedir nome e senha ao usuario 

# # # # # # # mostrar "bem vindo" quando acertara senha e o nome 

# # # # # # # apos pedir o salario do usuario 

# # # # # # # mostrar salario anual 

# # # # # # # se o salario anual for maior que 100mil mostrar mensagem "rico"

# # # # # # # nome = ""
# # # # # # # senha = ""

# # # # # # # while nome == "" or senha == "":
# # # # # # #     nome = input("Digite seu nome: ")
# # # # # # #     senha = input("Digite sua senha: ")

# # # # # # # print("Bem-vindo")

# # # # # # # salario = float(input("Digite seu salário mensal: "))
# # # # # # # salario_anual = salario * 12

# # # # # # # print("Seu salário anual é:", salario_anual)

# # # # # # # if salario_anual > 100000:
# # # # # # #     print("Rico")

# # # # # # # valor1 = int(input("Digite um numero: "))
# # # # # # # valor2 = int(input("Digite um numero: "))

# # # # # # # if (valor1 > valor2):
# # # # # # #     print("o maior valor é:", valor1)
# # # # # # # elif (valor1 < valor2):
# # # # # # #     print("o maior valor é:", valor2)
# # # # # # # elif (valor1 == valor2):
# # # # # # #     print("os valores são iguais")

# # # # # # nota1 = int(input("digite sua nota1:"))
# # # # # # nota2 = int(input("digite sua nota2:"))
# # # # # # nota3 = int(input("digite sua nota3:"))
# # # # # # nota4 = int(input("digite sua nota4:"))

# # # # # # notafinal = (nota1 + nota2 + nota3 + nota4)/4

# # # # # # if (notafinal >= 80):
# # # # # #     print("Excelente")
# # # # # # elif (notafinal < 80 and notafinal >= 60):
# # # # # #     print ("passou")
# # # # # # elif (notafinal < 60):
# # # # # #     print ("até ano que vem")

# # # # # valor1 = float(input("Digite o primeiro valor: "))
# # # # # valor2 = float(input("Digite o segundo valor: "))

# # # # # print("Soma:", valor1 + valor2)
# # # # # print("Subtração:", valor1 - valor2)
# # # # # print("Multiplicação:", valor1 * valor2)
# # # # # print("divisão:", valor1 / valor2)
    

# # # # salario = float(input("Digite o salário mensal: "))
# # # # salario_anual = salario * 12
# # # # print("Salário anual:", salario_anual)

# # # # if salario > 5000:
# # # #     imposto = salario * 0.08
# # # # elif salario <= 5000:
# # # #     imposto = salario * 0.05

# # # # print("Imposto:", imposto)

# # # def saudacao(nome):
# # #     print("Olá",nome)
# # #     saudacao ("Nícolas")

# # #     def soma(num1,num2):
# # #         soma=num1+num2
# # #         print("soma:",soma)

# # #         soma(3,4)


# # # 1) Crie uma função que faça a média de 3 valores

# # def media(num1, num2, num3):
# #     soma = num1 + num2 + num3
# #     media = soma / 3
# #     print("sua media é:", media)

# # # 2) Crie uma função que calcule o imposto anual do seu salario 

# # def calcular_imposto_anual(salario_mensal):
# #     imposto_anual = salario_mensal * 12 * 0.22
# #     print("vc pagara:", imposto_anual)


# # # 3) crie uma função que valide se a senha esta correta 
# def senha(senha_correta):
#     senha = int(input("digite sua senha:"))
#     while senha != senha_correta:
#         print("senha incorreta")
#         senha = int(input("digite sua senha:"))
#     print("Sucesso")

# senha(1234)

# criar função de menu de opçoes e pedir a opção desejada ao usuario
# -criar função de depósito
# -criar função de saque
# -criar função de ver saldo 
# -ao digitar "sair" encerrar o progama

# saldo = 0
# def menu():
#     print("1 - Depósito")
#     print("2 - Saque")
#     print("3 - Ver saldo")
#     print("Digite 'sair' para encerrar")

# def deposito(saldo):
#     valor = float(input("Valor do depósito: "))
#     return saldo + valor

# def saque(saldo):
#     valor = float(input("Valor do saque: "))
#     return saldo - valor

# def ver_saldo(saldo):
#     print("Saldo:", saldo)

# saldo = 0
# opcao = ""

# while opcao != "sair":
#     menu()
#     opcao = input("Opção: ")
#     if opcao == "1":
#         saldo = deposito(saldo)
#     elif opcao == "2":
#         saldo = saque(saldo)
#     elif opcao == "3":
#         ver_saldo(saldo)

# Atividade do dia 19/08/25
# crie uma lista de tarefas 

# adicione 5 tarefas na  lista

# adicione uma tarefa na posição 2 da lista 

# remova a  "lavar louça" da lista 

# remover a tarefa da posição 1 da lista


# lista_tarefas = ["estudar", "lavar louça", "fazer compras", "limpar o quarto", "pagar contas"]  
# lista_tarefas.insert(1, "ir à academia")  
# lista_tarefas.remove("lavar louça") 
# del lista_tarefas[1]   
# print("Lista de tarefas atualizada:", lista_tarefas)

# crie uma lista de 10 alunos mostre "ola" + nome de cada aluno
# alunos = ["Rafael", "Nicolas", "Agner", "Julia", "Guilherme", "Fernando", "Guilherme magni", "Breno", "Vitor", "Rafaela"]

# for aluno in alunos:
#     print("Olá " + aluno)

# crie uma lista de 10 numeros mostre a soma de todos os numeros da lista
# numeros = [21, 32, 23, 44, 55, 66, 97, 38, 29, 19]

# soma = sum(numeros)

# print("A soma é:", soma)

numeros = [1,2,3,4,5,6,7,8,9,10,
           11,12,13,14,15,16,17,18,19,20]

pares = len([n for n in numeros if n % 2 == 0])
impares = len([n for n in numeros if n % 2 != 0])

print("Pares:", pares)
print("Ímpares:", impares)
print("Total:", len(numeros))  
