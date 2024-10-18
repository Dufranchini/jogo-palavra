"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input('digite um numero inteiro aqui: ')
try: 
    numero_int = int(numero)
except ValueError:
    print('numero invalido')
if numero_int % 2 == 0:
    print(f"{numero_int} é um número par.")
else:
    print(f"{numero_int} é um número ímpar.")

# poderia ter adicionado o .isdigit para verificar se o numero digitado foi somente numero inteiro