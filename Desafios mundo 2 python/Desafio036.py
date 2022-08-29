# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

vcasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = float(input('Em quantos anos de financiamento? '))

prestação = vcasa / (anos * 12)

print('Para pagar um casa de R${:.2f} em {} anos'.format(vcasa, anos), end=' ')
print('A prestação será de R${:.2f}'.format(prestação))

print('Analisando sua situação...')
sleep(3)

if prestação <= (salario * 30) / 100:
    print('Impréstimo aprovado')
else:
    print('Impréstimo negado')
