'''
Escreva um algoritmo que defina a faixa etária de uma pessoa e apresente a 
faixa em tela. Caso a idade seja até 20 anos ele será considerado Jovem. Se 
a idade esteja entre 21 até 69 ele será considerado “Adulto”. Caso seja maior 
ou igual a 70 será considerado “Idoso”.
'''
print ("Insira a sua idade:")
id = int(input())
if id <= 20:
    print ("O usuário é considerado jovem.")
else:
    if id <= 69:
        print ("O usuário é considerado adulto.")
    else:
        print ("O usuário é considerado idoso.")