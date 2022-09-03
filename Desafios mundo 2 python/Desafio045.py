#Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep

itens =  ["pedra", "Papel", "Tesoura"]

print(""" 
    Suas opções:
    Pedra [0]
    Papel [1]
    Tesoura [2]
""")

jogador = int(input("Qual sua jogada? "))
computador = random.randint(0, 2)

sleep(1)
print("Jo")
sleep(1)
print("Ken")
sleep(1)
print("Pô")
sleep(1)

print("~^" * 14)
print("Você escolheu {}".format(itens[jogador]))
print("O computador escolheu {}".format(itens[computador]))
print("~^" * 14)


if computador == 0:
    if jogador == 0:
        print("Empate")
    elif jogador == 1:
        print("Jogador vence")
    elif jogador == 2:
        print("Computador vence")

if computador == 1:
    if jogador == 0:
        print("Computador vence")
    elif jogador == 1:
        print("Empate")
    elif jogador == 2:
        print("Jogador vence")

if computador == 2:
    if jogador == 0:
        print("Jogador vence")
    elif jogador == 1:
        print("Computador vence")
    elif jogador == 2:
        print("Empate")