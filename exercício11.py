opcao = 1
bd_estoque = []
contador = 0
while opcao != 4:
    print("=" *30)
    print("1- Adicionar produto")
    print("2- Consultar estoque")
    print("3- Consultar valor total do estoque")
    print("4- Quantidade ")
    opcao = int(input("Opcao >>>> "))
    if opcao == 1:
        print("Adicionar produto")
        codigo = int(input("Informe o código: "))
        nome = input("Informe o nome: ")
        descricao = input("Informe a descrição: ")
        preco = float(input("Informe o preço:R$ "))
        produto = [codigo, nome, descricao, preco]
        bd_estoque.append(produto) #adicionar produto na lista do estoque
        print(" ---- Adicionado com sucesso ---- ")
    elif opcao == 2:
        print(" ---- Estoque ---- ")
        print('Código\tNome\tDescrição\tPreço')
        for prod in bd_estoque:
            print(prod[0], end='\t') ###\t tab
            print(prod[1], end='\t')
            print(prod[2], end='\t')
            print(prod[3])
    elif opcao == 3:  
         print(" ---- Consultar valor do estoque ----")
         for soma in bd_estoque:
             soma = soma[3]  
             total = soma + 1
         print(f'O valor de estoque é de R$ {total:.2f} ')
    elif opcao == 4:
        print(" ---- Quantidade ---- ")
        for qtd in bd_estoque:
            estoque = qtd[0]
            quantidade = estoque 
        print(f"O total é de {quantidade} produtos! ") 
    else:
        print("Opção inválida! ")