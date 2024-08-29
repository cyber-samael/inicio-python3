# contador de energia

print('Seja bem vindo a calculadora de energia para Real')

kwh = float(input('Digite o valor de energia gasto em khw: '))
k = (kwh*0.20)

print(f'O valor total de sua conta de energia é de: R${k:.2f}')