def calc():    
    primeiro_numero = input('Digite um número: ')
    segundo_numero = input('Digite um segundo número: ')
    operador = input('Escolha um operador (+, -, *, /): ')

    numeros_validos = None
    try:
        numero1 = float(primeiro_numero)
        numero2 = float(segundo_numero)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('um ou ambos numeros sao invalidos')

    if operador == '+':
        soma = numero1 + numero2
        print(f'A soma de {numero1} + {numero2} = {soma}')
    elif operador == '-':
        subtracao = numero1 - numero2
        print(f'{numero1} - {numero2} = {subtracao}')
    elif operador == '*':
        multiplicacao = numero1 * numero2
        print(f'{numero1} x {numero2} = {multiplicacao}')
    elif operador == '/':
        divisao = numero1 / numero2
        print(f'{numero1} / {numero2} = {divisao}')
    else:
        print('O operador dado não é compatível ou não existe!')

while True:
    sair = input('Gostaria de iniciar a calculadora? [s]sim ou [n]não: ').lower()
    if sair == 'n':
        break
    elif sair == 's':
        calc()
    else:
        print('Opção inválida. Por favor, digite "s" para sair ou "n" para continuar.')
