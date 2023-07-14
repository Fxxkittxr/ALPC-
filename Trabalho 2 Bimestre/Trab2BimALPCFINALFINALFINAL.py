import random
memoria = []
opcao = 0
tamanho = 0
letra = ' '

for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria.append('x')
    else:
        memoria.append(' ')


while(opcao != 4):
    for i in range(0,20):
        print(memoria[i],end="|")
    print()
    for i in range(20,40):
        print(memoria[i],end="|")
    print()
    for i in range(40,60):
        print(memoria[i],end="|")
    print()
    for i in range(60,80):
        print(memoria[i],end="|")
    print()
    for i in range(80,100):
        print(memoria[i],end="|")
    print()
    #Menu do programa
    print("1 - Primeira Escolha")
    print("2 - Melhor Escolha")
    print("3 - Pior Escolha")
    print("4 - Sair")
    print("Escolha o algoritmo pelo numero:")
    opcao = int(input())
    if (opcao == 4):
        print("Finalizando Programa")
        break
    print("Digite o tamanho da informacao:")
    tamanho = int(input())
    print("Digite a letra a ser utiliada:")
    letra = input()

    
    cont = 0  #Definindo cont para recomeçar
    vago = 0  #Definindo vago para recomeçar
    x = True #Definindo x para recomeçar
    primeiro_vago = 123  #Definindo primeiro vago para recomeçar
    ultimo_vago = 0  #Definindo ultimo vago para recomeçar
    maior_vago = 0 #Definindo maior vago para recomeçar
    encontrou = False 
    colocado = tamanho  #Para verificar se ja fpr inserido todos os dados

    if(opcao == 1):
        #Implemente aqui a lógica da primeira escolha ACHAR O PRIMEIRO LUGAR QUE CAIBA
        for cont in range (100):
            if (memoria[cont] == ' '):
                if (primeiro_vago == 123):  #Verificar se o primeiro vago é 123 (se não foi redefinido ainda) para redefinir
                    primeiro_vago = cont
                ultimo_vago = cont  # Definindo o ultimo vago conforme o programa roda
                vago += 1  #Anotando numero de casas vagas
            else:  #Caso o tamanho seja maior que 1, fazer a verificação de casas vagas.
                if(memoria[cont] != ' '):  #Verificação caso o primeiro espaço não seja vago, verificar o proximo.
                    vago = 0  #Redefinindo os valores para verificação.
                    primeiro_vago = 123
                    ultimo_vago = 0
            if (tamanho == vago):  #Caso o valor do tamanho seja igual o dos espaços vagos começa o processo de preencher os vagos.
                while (x == True): 
                    memoria[primeiro_vago] = letra 
                    primeiro_vago += 1  #Espaço a espaço vai ser preenchido.
                    if (primeiro_vago > ultimo_vago):  #Quando o espaço de preenchidos tiver ultrapassado o espaço do ultimo vago, finaliza e volta para o menu.
                        x = False
            if x == False:
                break
            if(cont == 99):
                    print("Opção Invalida, sem espaços vagos\nTente novamente:")  
    if (opcao == 2): #lista_vagos.append(oq quero colocar)
        for cont in range (100):


            if (memoria[cont] == ' '):

                if (primeiro_vago == 123):  #Verificar se o primeiro vago é 123 (se não foi redefinido ainda) para redefinir
                    primeiro_vago = cont

                ultimo_vago = cont  # Definindo o ultimo vago conforme o programa roda
                vago += 1  #Anotando numero de casas vagas

            else:  #Caso o tamanho seja maior que 1, fazer a verificação de casas vagas.

                if(memoria[cont] != ' '):  #Verificação caso o primeiro espaço não seja vago, verificar o proximo.
                    vago = 0  #Redefinindo os valores para verificação.
                    primeiro_vago = 123
                    ultimo_vago = 0 ##########

                    
            if vago == tamanho and memoria[cont + 1] == 'x':

                if encontrou == False:

                    maior_primeiro_vago = primeiro_vago
                    maior_ultimo_vago = ultimo_vago
                    encontrou = True


                while (x == True): 
                    memoria[maior_primeiro_vago] = letra 
                    maior_primeiro_vago += 1  #Espaço a espaço que vai ser preenchido.
                    colocado -= 1

                    if (colocado == 0):  #Verifica se foi preenchido com todos os valores necessarios, finaliza e volta para o menu.
                        x = False

                if x == False:
                    break  #Break o for e volta para o menu 



            if(cont == 99):
                    print("Opção Invalida, sem espaços vagos para esse tamanho de informação\nTente novamente:")  


    if(opcao == 3):
        for cont in range (100):
            if (memoria[cont] == ' '):
                if (primeiro_vago == 123):  #Verificar se o primeiro vago é 123 (se não foi redefinido ainda) para redefinir
                    primeiro_vago = cont
                ultimo_vago = cont  # Definindo o ultimo vago conforme o programa roda
                vago += 1  #Anotando numero de casas vagas
            else:  #Caso o tamanho seja maior que 1, fazer a verificação de casas vagas.
                if(memoria[cont] != ' '):  #Verificação caso o primeiro espaço não seja vago, verificar o proximo.
                    vago = 0  #Redefinindo os valores para verificação.
                    primeiro_vago = 123
                    ultimo_vago = 0 ##########
            if (vago > maior_vago): #Armazenar o maior buraco vago.
                maior_vago = vago
                maior_primeiro_vago = primeiro_vago
                maior_ultimo_vago = ultimo_vago
            if (cont == 99) and maior_vago >= tamanho:  #Para no ultimo loop fazer o preenchimento na memoria.
                while (x == True): 
                    memoria[maior_primeiro_vago] = letra 
                    maior_primeiro_vago += 1  #Espaço a espaço que vai ser preenchido.
                    colocado -= 1
                    if (colocado == 0):  #Verifica se foi preenchido com todos os valores necessarios, finaliza e volta para o menu.
                        break
                if x == False:
                    break
            if (cont == 99) and colocado == tamanho:
                print("Opção Invalida, sem espaços vagos para esse tamanho de informação\nTente novamente:")


'''
if (tamanho == vago):  #Caso o valor do tamanho seja igual o dos espaços vagos começa o processo de preencher os vagos.
                if cont != 99: 
                    if (memoria[cont + 1] == 'x'): #verificar se a casa seguinte esta disponivel.
                        while (x == True): 
                            memoria[primeiro_vago] = letra 
                            primeiro_vago += 1  #Espaço a espaço vai ser preenchido.
                            if (primeiro_vago > ultimo_vago):  #Quando o espaço de preenchidos tiver ultrapassado o espaço do ultimo vago, finaliza e volta para o menu.
                                x = False
                else: #no caso de ser a ultima casa ja 
                    while (x == True): 
                            memoria[primeiro_vago] = letra 
                            primeiro_vago += 1  #Espaço a espaço vai ser preenchido.
                            if (primeiro_vago > ultimo_vago):  #Quando o espaço de preenchidos tiver ultrapassado o espaço do ultimo vago, finaliza e volta para o menu.
                                x = False
'''