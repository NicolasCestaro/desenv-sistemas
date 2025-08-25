# try: onde você coloca o código que pode gerar erro
# except: onde que trata o erro caso aconteça
#ex: 1 acessar item da lista
def acessar_lista(lista, indice):
    try:
        return lista[indice]  
    except IndexError:
        return "Índice fora do alcance"

#ex: 2 somar números da lista
def soma(lista):
    try:
        total = 0
        for i in lista:
            total += int(i)
        return total
    except:
        return "Erro: valor inválido na lista"

valores = ["1", "2", "a"]
print(soma(valores))  

#ex: 3  remover item da lista
def remover(lista, item):
    try:
        lista.remove(item)
        return lista
    except:
        return "Erro: item não existe"

frutas = ["maçã", "banana", "uva"]
print(remover(frutas, "banana"))  
print(remover(frutas, "laranja"))0 