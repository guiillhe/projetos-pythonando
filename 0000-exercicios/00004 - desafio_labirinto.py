labirinto = [
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
            [0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 1]
        ]
#(coluna, linha)
saida =(0,0)
chegada = (9,9)


def procurar_saida(labirinto, saida, chegada):
    passos = 0
    if saida == chegada:
        return True
    else:
        if labirinto[saida[0]][saida[1]] == 0:
            print('Não é possivel iniciar o labirinto')
        else:
            for i in range(len(labirinto)):
                for j in range(len(labirinto[i])):
                    if labirinto[i][j] == 1:
                        passos += 1
                        if i == chegada[0] and j == chegada[1]:
                            print(f'Passos: {passos}')
                            print('Chegou ao destino')
                        else:
                            print(f'Passo: {passos}')
                            print(f'Posição: {i},{j}')
                            return False
      
            
            

procurar_saida(labirinto, saida, chegada)