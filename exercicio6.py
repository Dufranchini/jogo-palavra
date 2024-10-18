"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horas = int(input('digite as horas: '))

if horas <= 11:
    print('Bom Dia')
elif horas <= 17:
    print('boa tarde')
elif horas <= 23:
    print('Boa Noite')
else:
    print('HORA INVALIDA')
