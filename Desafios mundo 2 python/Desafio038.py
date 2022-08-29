# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

num1 = int(input('Digite um primeiro número inteiro: '))
num2 = int(input('Digite um segundo número inteiro: '))

if num1 > num2:
    print('Número {} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('Número {} é maior que {}'.format(num2, num1))
else:
    print('os dois numeros são iguais')