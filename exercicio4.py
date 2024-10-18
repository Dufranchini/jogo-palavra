# nome = input('digite teu nome: ') 
# idade = input('digite tua idade: ')

# if nome and idade:
#     print(f'seu nome e {nome}')
#     print('seu nome invertido e: ',nome[::-1])
#     if ' ' in nome:
#         print('teu nome contem espaco')
#     else:
#         print('seu nome nao possui espaco')
#     print('seu nome possui',(len(nome)), 'letras')
#     print('a primeira letra de seu nome: ', nome[0])
#     print('a ultima letra de seu nome: ', nome[-1])
# else:
#     print('descupe, vc deixou um campo vazio !')

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome NÃO contém espaços')

    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")

