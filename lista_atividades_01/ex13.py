# impostos carros

custof = float(input('Digite o valor de fábrica do veiculo: R$ '))
pd = 0.28
pi = 0.45

custod = custof * pd
custoi = custof * pi

custofi = custof + custod + custoi

print(f'O custo final do comprador é: R$ {custofi:.2f}')
