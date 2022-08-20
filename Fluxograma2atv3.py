'''
Escreva um algoritmo que solicite a quantidade total em miligramas de colesterol mau existente no sangue de um paciente. 
Considerando que o valor máximo ideal para uma pessoa saudável é 130mg, caso a quantidade esteja 
menor apresente uma mensagem indicando que esta menor. Caso esteja acima, calcule o percentual que 
esta acima e apresente uma mensagem.
'''
c = int(input("Insira a quantidade de colesterol mau que existe no seu sangue em mg: "))
if c <= 130:
  print("Colesterol ideal")
else:
    ca = ((c * 100) / 130) - 100
    print (f"Colesterol esta {ca}% a cima do ideal.")