"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('qual o seu nome: ')

curto = len(nome) <= 4
normal = len(nome) <= 6
grande = len(nome) > 6

if curto:
    print('seu nome e curto')
elif normal:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')