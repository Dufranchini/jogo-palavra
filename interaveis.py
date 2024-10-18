#for letra in texto
texto = 'luiz' #interavel 
interador = iter(texto) #iterator

# while True: <-- extamente que o for faz !!!
#     try:
#         letra = next(interador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto: 
    print(letra)  