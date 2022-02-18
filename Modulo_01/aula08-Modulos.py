# Aula 08 - Utilizando Módulos / bibliotecas

'''
bebidas: cerveja, vinho, energético
comida: hamburgue, cachorro quente, pizza
doce: pudim, sorvete, bolo

import > bebida: Neste caso serão importadas todos os recursos deste módulo
from > doce > import > pudim: Neste caso será importada apenas um item

biblioteca math: Se trata de uma biblioteca com recursos de matemática

Para calcular a média de um aluno, podemos utilizar assim:
ceil: Arredonda para cima
floor: Arredonda para baixo
trunc: Irá truncar da virgula para frente.
pow: Calcula a potência
sqrt: Raiz quadrada
factorial: Calcula o fatorial
'''
# Utilizando a biblioteca inteira
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
print('A raiz de {} arredondada para cima é igual a {}.'.format(num, math.ceil(raiz)))
print('A raiz de {} arredondada para baixo é igual a {}.'.format(num, math.floor(raiz)))

# utilizando apenas 1 item da biblioteca (desta forma não precisar mencionar a função no código)
from math import sqrt, floor, ceil
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}.'.format(num, raiz))
print('A raiz de {} arredondada para cima é igual a {}.'.format(num, ceil(raiz)))
print('A raiz de {} arredondada para baixo é igual a {}.'.format(num, floor(raiz)))

# Desafios

""""
Desafio 016 - Quebrando um número: Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127
O número 6.127 tem a parte inteira 6.

Desafio 017 - Catetos e Hipotenusa: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo
retângulo, calcule e mostre o comprimento da hipotenusa.

Desafio 018 - Seno, Cosseno e Tangente: Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e 
tangente desse ângulo.

Desafio 019 - Sorteando um item na lista: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

Desafio 020 - Sorteando uma ordem na lista: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos
dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

Desafio 021 - Tocando um MP3: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
"""