'''
Escreva um algoritmo que calcule o número de páginas mínimo que um leitor deve ler para terminar um livro em um determinado numero de dias informado. Caso o número de paginas a ler por dia for maior que 100, informe ao usuário que é impossível de realizar a leitura, caso contrário apresente o número de paginas.
'''
p = int(input("Informe o número de páginas do livro: "))
d = int(input("Informe o número de dias que se tem para ler o livro: "))
pd = p / d
if pd > 100 :
  print("Impossivel fazer a leitura nesse periodo de tempo.")
else:
    print (f"É possivel ler {pd} paginas em {d} dias.")