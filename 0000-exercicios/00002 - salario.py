'''
2 - Salário
Nível: 1
Faça um Programa que leia quanto você ganha por hora e o número de horas
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato:
Entrada
O arquivo de entrada contém 2 valores de ponto flutuante.
Saída
Exiba os seguintes dados arrendondados para baixo exatamente como na tabela
abaixo:
Exemplos de entradas
120
123
Exemplos de saídas
Salario bruto: 14760
INSS: 1180
SINDICATO: 738
Salario liquido: 11217
'''

def salario():
    salario_hora = float(input('Digite o valor da sua hora de trabalho: '))
    horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas: '))
    salario_bruto = salario_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - ir - inss - sindicato
    print(f'Salario bruto: R${salario_bruto}')
    print(f'IR: R${ir}')
    print(f'INSS: R${inss}')
    print(f'Sindicato: R${sindicato}')
    print(f'Salario liquido: R${salario_liquido}')

salario()