#  Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
from time import sleep

num = int(input('Digite um valor inteiro: '))

print('''Escolha uma das opções de conversão:
[1] Converter para binario
[2] Converter para octal
[3] Converter para hexadecimal''')

opção = int(input('Escolha uma das opções: '))

print('Convertendo...')
sleep(2)

if opção == 0 or opção > 3:
    print('Opção invalida,por favor digite um numero de 1 até 3!')
elif opção == 1:
    print('O número {}, convertido para binario fica {}'.format(num, bin(num) [2:] ))
elif opção == 2:
    print('O número {}, convertido para octal fica {}'.format(num, oct(num) [2:] ))
elif opção == 3:
    print('O número {}, convertido para hexadecimal fica {}'.format(num, hex(num) [2:] ))
print('Obrigado, gostou da conversão?')