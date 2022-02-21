# Aula 10 – Condições (Parte 1)

"""
Nessa aula, vamos aprender como utilizar estruturas condicionais simples e compostas nos seus programas em Python.

se carro.esquerda() = if carro.esquerda():
    bloco_V_            bloco True
senão               = else:
    bloco_F_            bloco False
"""

# Exemplo - Condição simples
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome))

# Exemplo - Condição composta
tempo = int((input('Quantos anos tem seu carro? ')))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
    print('--fim--')

# Exemplo - Condição Simplificada (porém complexa)
tempo = int((input('Quantos anos tem seu carro? ')))
print('Carro novo' if tempo < 3 else 'Carro velho')
print('--fim--')

# Exemplo - Composto:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
    
# Exemplo - Simplificado:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('PARABÉNS' if m >= 6 else 'ESTUDE MAIS!')

# Desafios

"""
Desafio 028 - Jogo da Adivinhação v.1.0: Escrevam um programa que faça o computador "pensar" em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

Desafio 029 - Radar eletrônico: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem deizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada KM acima do limite.

Desafio 030 - Par ou Ímpar?: Crie um programa que leia o número inteiro e mostre na tela se ele é PAR ou IMPAR.

Desafio 031 - Custo da Viagem: Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o 
preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200KM e R$ 0,45 para viagens mais longas.

Desafio 032 - Ano Bissexto: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

Desafio 033 - Maior e menor valores: Faça um programa que leia três número e mostre qual é o maior e qual é o menor.

Desafio 034 - Aumentos múltiplos: Escreva um program que pergunte o salário de um funcionário e calcule
o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.

Desafio 035 - Analisando Triângulo v1.0: Desenvolva um programa que leia o comprimento de três retas e diga
ao usuário se elas podem ou não formar um triângulo.
"""


