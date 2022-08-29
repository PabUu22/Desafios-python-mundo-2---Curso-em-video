# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('Digite 1 para \033[1;36mmasculino\033[m', 'e digite 2 para \033[1;34mFeminino\033[m')

gen = int(input('Qual o seu género: '))

if gen == 1:
    Ano = int(input('Digite ano de nascimento: '))

    idade = (2022 - Ano )

    if idade == 18:
        print('Você tem {} anos de idade'.format(idade))
        print('Você deve se alistar \033[1;31;47mimediatamente !!!\33[m')
    elif idade > 18:
        saldo = (idade - 18)
        alistamento = (2022 - saldo)
        print('Você tem {} anos de idade'.format(idade))
        print('E deveria se alistar há {} anos'.format(saldo))
        print('Ou você se alistou em {}'.format(alistamento))
    elif idade < 18:
        saldo = (18 - idade)
        alistamento = (2022 + saldo)
        print('Você tem {} anos de idade'.format(idade))
        print('falta ainda {} anos para seu alistamento'.format(saldo))
        print('Você deve se alistar no ano de {}'.format(alistamento))
else:
    print('Mulheres não são obrigadas a se alistarem')





