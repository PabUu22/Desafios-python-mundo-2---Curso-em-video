# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:

from time import sleep

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = ((nota1 + nota2) / 2 )

print("Analisando suas notas...")
sleep(2)

if media < 5.0:
    print("Aluno(a) reprovado(a)")
    print("Sua média foi de {}".format(media))
elif media < 5 or media < 7:
    print("Aluno de recuperação, sua média foi de {}".format(media))
elif media == 7:
    print("Aluno(a) aprovado(a)") 
    print("Sua média foi de {}".format(media))
    print("Aluno(a) passou, porém bem arrastado, portanto melhore suas notas")
elif media <= 9:
    print("Aluno(a) aprovado(a)")
    print("Sua média foi de {}".format(media))
    print("Sua media foi boa")
elif media <= 10:
    print("Aluno(a) aprovado(a)")
    print("Suas notas foram perfeitas, tendo uma média de {}".format(media))
    print("Continue assim !!!")