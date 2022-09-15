'''
Faça um programa que receba o preço de um produto 
e o seu código de origem e mostre a sua procedência. 
A procedência obedece a tabela a seguir
Código de origem   Procedência
1	               Sul
2	               Norte
3	               Leste
4	               Oeste
5 ou 6  	       Nordeste
7 ou 8 ou 9	       Sudeste
10 a 20	           Centro-Oeste
21 a 30	           Nordeste

'''

v = int(input("Insira o valor do produto: "))
co = int(input("Insira ocodigo de origem do produto: "))
if co == 1: 
    input("O produto tem procedencia do Sul")
else:
    if co == 2: 
        input("O produto tem procedencia do Norte")
    else: 
        if co == 3: 
            input("O produto tem procedencia do Leste")
        else:
            if co == 4: 
                input("O produto tem procedencia do Oeste")
            else:
                if co == 5 or co == 6: 
                    input("O produto tem procedencia do Nordeste")
                else: 
                    if co >= 7 and co <= 9: 
                        input("O produto tem procedencia do Sudoeste")
                    else:
                        if co >= 10 and co <= 20: 
                            input("O produto tem procedencia do Centro- Oeste")
                        else: 
                            if co >= 21 and co <= 30:
                                input("O produto tem procedencia do Nordeste")
