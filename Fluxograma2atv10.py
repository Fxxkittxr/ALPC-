'''
Escreva um algoritmo que calcule o valor de Imposto de Renda que uma Pessoa Física deve pagar de acordo com o valor total de seu rendimento anual: abaixo de R$19.200 isento, acima deste valor e até R$30.000 8%. Mais que R$30.000 anuais 11%.
'''
rm = float(input("Informe o valor do seu rendimento mensal:"))

ra = rm * 12

if ra < 19200:
    print  ("Isento de Imposto de Renda.")
else:
    if ra < 30000:
        ir = (rm * 8) / 100
        print (f"Imposto de Renda igual à R${ir}")
    else:
        ir = (rm * 11) / 100
        print (f"Imposto de Renda igual à R${ir}")