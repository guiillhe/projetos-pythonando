def sobrevivente():
    pessoas = int(input('Digite a quantidade de pessoas no circulo: '))
    lista = []
    for i in range(1,pessoas+1):
        lista.append(i)        
    while len(lista) > 1:
        try:
            for i in range(1,len(lista)):                
                if len(lista) == i-1:                    
                    break
                else:                                                    
                    lista.pop(i)
                                   
        except IndexError:            
            lista.pop(0)
            print(lista)
            
    print(f'O sobrevivente é: {lista[0]}')

sobrevivente()
        

