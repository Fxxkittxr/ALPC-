'''
Faça um programa que receba o código correspondente ao cargo 
de um funcionário e seu salário atual e mostre o cargo, o 
valor do aumento e seu novo salário. Os cargos estão na 
seguinte tabela:
1 - Escrituario - 50%
2 - Secretario - 35%
3 - Caixa - 20%
4 - Gerente - 10%
5 - Diretor - Não tem aumento
'''
input("1 - Escrituario - 50%\n2 - Secretario - 35%\n3 - Caixa - 20%\n4 - Gerente - 10%\n5 - Diretor - Não tem aumento")
REPETE = True
while REPETE == True:
    c = int(input("Insira o codigo do seu cargo: "))
    if c <= 5 :
        if c >=1 :
            REPETE = False

s = int(input("Insira o valor do seu salário atual: "))

if c == 1:
    tt = s + ((s * 50)/100)
    input(f"Seu salário é igual à: R${tt}")
else:
    if c == 2:
        tt = s + ((s * 35)/100)
        input(f"Seu salário é igual à: R${tt}")
    else:
        if c == 3:
            tt = s + ((s * 20)/100)
            input(f"Seu salário é igual à: R${tt}")
        else:
            if c == 4:
                tt = s + ((s * 10)/100)
                input(f"Seu salário é igual à: R${tt}")
            else:
                if c == 5:
                    input(f"Não há alteração no seu salário, continua o mesmo")
