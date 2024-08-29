# salario revendedor de carros

salario = float(input('Digite seu salário: R$ '))
carros = int(input('Digite quantos carros você vendeu: '))
valor = float(input('Digite o valor total de suas vendas: '))
valorc = float(input('Digite o valor recebido por carro: '))

comissaoc = carros * valorc
comissaov = valor * 0.05

salariofinal = salario + carros + comissaoc + comissaov

print(f'O Salário final é: R${salariofinal:.2f}')