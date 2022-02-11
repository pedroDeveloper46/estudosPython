from audioop import mul
import re


n1 = int(input('Digite um número '))
n2 = int(input('Digite um número '))

soma = n1 + n2
subt  = n1 - n2
mult = n1 * n2
div = n2 / n1
pot = n1 ** n2
divInteira = n1 // n2
resto = n1 % n2

ordemPrec = 2 ** (2 * (n1 + n2))

print('A soma entre {} e {} é {}'.format(n1,n2,soma))
print('A subtração entre {} e {} é {}'.format(n1,n2,subt))
print('A multiplicação entre {} e {} é {}'.format(n1,n2,mult))
print('A divisão entre {} e {} é {}'.format(n1,n2,div))
print('{} elevado a {} é {}'.format(n1,n2,pot))
print('A divisãp entre {} e {} é {}'.format(n1,n2,divInteira))
print('o resto da divisão entre {} e {} é {}'.format(n1,n2,resto))
print('Calculo envolvendo ordem de precedência entre {} e {} é {}'.format(n1,n2,ordemPrec))