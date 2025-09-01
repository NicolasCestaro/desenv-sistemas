with  open ("alunos.txt","w") as arquivo:
    arquivo.write("Rafael\n")
    arquivo.write("Nicolas\n")
    arquivo.write("Agner\n")
    arquivo.write("Julia\n")
    arquivo.write("Guilherme\n")
    
    print("Arquivo criado com sucesso!")
    with open ("alunos.txt","r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)