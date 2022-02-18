# Aula 09 - Manipulando de cadeias de texto (Strings)
"""
Técnica de Fatiamento

Frase = Curso em Video Python

Frase [9]: letra específica
Frase [9:13]: Vai pegar do 9 ao 12 (menos um no final)
Frase [9:21:2]: Pula de 2 em 2
Frase [:5]: Irá começar no primeiro caracter e terminar no 4 (excluindo o número 5)
Frase [15:]: Indiquei o ínicio até o final
Frase [9::3]: Começa no 9 e vai até o final, porém pulando de 3 em 3

# Análise

len(frase): Irá ler o tamanho da frase e mostrará a quantidade de caracter.
frase.count('o'): Conta quantos caracteres escolhidos tem na frase.
frase.count('o',0,13): Fazendo uma contagem do 0 ao 12 e informará quantos caracteres tem neste conjunto.
frase.find('deo'): Neste ponto irá mostrar qual a posição esta a frase.
frase.find('Android'): Sinal que ele irá retornar menos -1, dizendo que o string não existe.
'Curso'infrase: Mostra se existe ou não a string na variavel.

# Transformação

frase.replace('Python','Android'): Irá substituir a frase encontrada com a frase escolhida.
frase.upper(): Irá converter tudo para maiúscula.
frase.lower(): Irá converter tudo para minúscula.
frase.capitalize(): Converte apenas a primeira letra altera para maíscula e o resto ficaria em minúscula.
frase.title(): Converte a primeira letra da frase para maiúscula.
frase.strip(): Remove espaços inúteis da string.
frase.rstrip(): Remove espaços inúteis da string a direita.
frase.lstrip(): Remove espaços inúteis da string a esquerda.

# Divisão

frase.split(procurar as funções): A frase será dividida com base nos espaços da string em lista.

# Junção

'-'.join(frase): Irá juntar as frase que foram feito de lista acima para transformar em string única
com - ao invés do espaço.

# Dica

Para escrever um texto grande sem precisar colocar vários prints, coloque tudo dentro de um comentário.

Para forçar a atualização da frase será preciso:

frase = 'Curso em Vídeo Python'
frase = frase.replace('Python','Android')
print(frase)

print("""
Github: http://github.com/rodrigojackal
Twitter: @RodrigoJackal
Skype: rodrigo.jackal
Linkedin: https://www.linkedin.com/in/rodrigo-ferreira-santos-andrade/
""")

"""

# Desafios

"""
Desafio 022 - Analisador de Texto: Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome.

Desafio 023 - Separando digitos de um número: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados.

Ex: Digite um número: 1834
Unidade: 4
Dezena: 3
Centena: 8
Milhar: 1

Desafio 024 - Verificando as primeiras letras de um texto: Crie um programa que leia o nome de uma cidade e diga
se ela começa ou não com o nome "SANTO"

Desafio 025 - Procurando uma string dentro de outra: Crie um programa que leia o nome de uma pessoa e diga
se ela tem "SILVA" no nome.

Desafio 026 - Primeira e última ocorrência de uma string: Faça um programa que leia uma frase pelo teclado
e mostre:

Quantas vezes aparece a letra "A".
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.

Desafio 027 - Primeiro e último nome de uma pessoa: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza
Primeiro: Ana
Último: Souza
"""


