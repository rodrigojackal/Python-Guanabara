# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$ 60 por dia e R$ 0,15 por KM rodado

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
ac = int(input('Informe a diária do veículo: R$ '))
kmr = float(input('Informe quanto custa o KM rodado: R$ '))
pago = (ac * dias) + (kmr * km)

print('O total a pagar é de R$ {:.2f}.'.format(pago))
