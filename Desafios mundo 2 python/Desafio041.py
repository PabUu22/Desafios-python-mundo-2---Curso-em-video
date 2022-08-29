# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
from datetime import date

anoAtual = date.today().year
anoNascimento = int(input("Digite seu ano de nascimento: "))
idade = anoAtual - anoNascimento

print("O atleta tem {} anos".format(idade))

if idade <= 9:
    print("Nivel do atleta é: MIRIN")
elif idade <= 14:
    print("Nivel do atleta é: INFANTIL")
elif idade <= 19:
    print("Nivel do atleta é: JUNIOR")
elif idade <= 25:
    print("Nivel do atleta é: SÊNIOR")
elif idade > 25:
    print("Nivel do atleta é: MASTER")
    
