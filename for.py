for i in range (10):
    if i ==2:
        print('i e 2, pulando')
        continue 
    if i == 8: 
        print('i e 8, else n executara')
        break 
    for j in range(1,3):
        print(i,j)
    else:
        print("for competo com sucesso !")