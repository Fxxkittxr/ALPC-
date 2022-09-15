'''
6)	Faça um programa que receba duas notas, e calcule e 
mostre a média aritmética e a mensagem que esta na tabela 
abaixo:
0,0 - 4,0 - reprovado 
4,0 - 7,0 - exame
7,0 - 10 - aprovado
'''
n1 = int(input("Insira a primeira nota: "))
n2 = int(input("Insira a segunda nota: "))
nf = (n1 + n2) / 2 
if nf <= 4:
    input(f"Sua media é igual à: {nf}\nVocê esta reprovado.")
else:
    if nf <= 7:
        input(f"Sua media é igual à: {nf}\nVocê esta em exame.")
    else:
        if nf <= 10:
            input(f"Sua media é igual à: {nf}\nVocê esta aprovado.")
