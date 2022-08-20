'''
Escreva um algoritmo que calcule o número de páginas mínimo que um leitor deve ler para terminar um livro em um determinado numero de dias informado. Caso o número de paginas a ler por dia for maior que 100, informe ao usuário que é impossível de realizar a leitura, caso contrário apresente o número de paginas.
'''
v = int(input("Informe a velocidade do carro em km/h: "))

if v > 160 :
  print("Multa gravíssima, 180 UFIR.")
else:
    if v > 100:
        print ("Multa grave, 120 UFIR.")
    else:
        if v > 60:
            print ("Multa média, 60 UFIR.")
        else:
            print ("Sem multa.")