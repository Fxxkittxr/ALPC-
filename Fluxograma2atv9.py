'''
Construa um algoritmo que calcule o consumo de combustível de um veículo qualquer baseado nas informações de quilometragem inicial e final de um percurso, e a quantidade de gasolina consumida em litros. Caso o consumo esteja entre 10 e 16 litros/km mostre a mensagem “consumo normal”, caso seja maior que 16 litros/km apresente a mensagem “consumo anormal”.
'''
kmc = float(input("Informe a km inicial do percurso: "))
kmf = float(input("Informe a km final do percurso:  "))
g = float(input("Informe a quantidade de gasolina consumida em litros:"))
tt = (g /(kmf - kmc))* 100

if tt > 16:
    print  (f"Consumo anormal {tt}")
else:
    if tt > 10:
        print (f"Consumo normal {tt}")
    else:
        print (f"Consumo baixo {tt}")
