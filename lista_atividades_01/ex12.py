# idade em dias

d = int(input('Digite o dia que você nasceu: '))
m = int(input('Digite o mês que você nasceu: '))
a = int(input('Digite o ano que você nasceu: '))

ano = a * 365
mes = m * 30
dias = d+mes+ano

print(f'Sua idade expressa em dias é: {dias}')
