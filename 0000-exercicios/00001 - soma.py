valor1 = ''
valor2 = ''

def soma(valor1, valor2):
    print('='*30)
    print('SOMA DE DOIS VALORES')
    valor1 = input("Digite o primeiro valor: ")
    valor2 = input("Digite o segundo valor: ")
    valor1 = valor1.replace(',','.')
    valor2 = valor2.replace(',','.')
    resultado = round(float(valor1) + float(valor2),2)

    
    return f"A soma dos valores é: {resultado}"  

print(soma(valor1=valor1, valor2=valor2))