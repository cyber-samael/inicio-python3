# calcular IMC

print('Olá, seja bem vindo à calculadora de IMC!')

peso = float(input('Adicione o seu peso: '))
altura = float(input('Adicione sua altura: '))
imc = (peso/altura)*altura

print(f'O valor do seu IMC é : {imc}')
