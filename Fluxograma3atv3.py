'''
Pedro comprou um saco de ração com peso em quilos. 
Pedro possui dois gatos para os quais fornece a quantidade 
de ração em gramas. Faça um programa que receba o peso do 
saco de ração e a quantidade de ração fornecida para cada gato. 
Calcule e mostre quanto restará de ração no saco após cinco 
dias.
'''

sr = int(input("Insira a quantidade de quilos que tem no saco de ração: "))
qr = int(input("Insira a quantidade em gramas que cada gato come por refeição: "))
gt1 = int(input("Insira a quantidade de vezes que o gato 1 come por dia: "))
gt2 = int(input("Insira a quantidade de vezes que o gato 2 come por dia: "))

srt = sr * 1000 
ttd = ((gt1 * qr) + (gt2 * qr))
tt = (ttd * 5)
if srt < tt:
    input("Irá faltar ração pros gatinho.")
else:
    s = tt - srt
    input(f"Após 5 dias, sobra {s} gramas de ração.")