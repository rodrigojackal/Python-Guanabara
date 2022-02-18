#
nome = input('Qual é seu nome? ')
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} e a \n divisão é {:3f}'.format(s, m, d), end=' a ')
print('Divisão inteira {} e Potência {}.'.format(di, e))

# Para quebrar a linha é \n
# Para naõ quebrar a linha end=''