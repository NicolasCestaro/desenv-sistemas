nota1 = int(input("digite sua nota1:"))
nota2 = int(input("digite sua nota2:"))
nota3 = int(input("digite sua nota3:"))
nota4 = int(input("digite sua nota4:"))

notafinal = (nota1 + nota2 + nota3 + nota4)/4

if (notafinal >= 80):
    print("Excelente")
elif (notafinal < 80 and notafinal >= 60):
    print ("passou")
elif (notafinal < 60):
    print ("até ano que vem")