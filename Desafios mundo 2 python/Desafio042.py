# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < (b + c) and b < (a + c) and c < (a + b):
    print('os segmentos podem formar um triangulo ', end="" )
    if a == b == c:
        print("Equilátero")
    elif a != b != c != a:
        print("Escaleno")
    else:
        print("Isósceles")
else:
    print('os segmentos não podem formar um triangulo')




