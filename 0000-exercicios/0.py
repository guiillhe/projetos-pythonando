# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
itens = []
# TODO: Crie um loop para solicita os itens ao usuário:
while True:
    item = input()
    if item.upper() == "PARAR":
        break
    else:
    	itens.append(item)
  
# TODO: Solicite o item e armazena na variável "item":

# TODO: Adicione o item à lista "itens":


# Exibe a lista de itens
print("Lista de Equipamentos:")  
for item in itens:
    # Loop que percorre cada item na lista "itens"
    print(f"- {item}")