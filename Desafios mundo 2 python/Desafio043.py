# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2) 

print("Seu imc é {:.2f}".format(imc))

if imc < 18.5:
    print("Você está abaixo do peso")
elif imc > 18.5 and imc < 25:
    print("Você está no peso ideal")
elif imc > 25 and imc < 30:
    print("Você está sobrepeso")
elif imc > 30 and imc < 40:
    print("Você está com obsidade")
elif imc > 40:
    print("Você está com obsidade morbida")
