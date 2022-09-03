# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros
print("{:=^40}".format("Lojas PabUu's"))
compra = float(input("Qual o valor da compra? "))

print(
    '''Formas de pagamento:
    Á vista vista no dinheiro [1]
    Á vista cartão [2]
    No cartão 2x [3]
    3x ou mais no Cartão [4]
    ''' 
)

pagamento = int(input("Qual a forma de pagamento? "))

if pagamento == 1:
    total = compra - (compra * 10 / 100) 
    print("Á vista no dinheiro você recebe 10% de desconto!")
    print("O valor fica {:.2f}R$".format(total))
elif pagamento == 2:
    total = compra - (compra * 5 / 100)
    print("Á vista no dinheiro você recebe 5% de desconto!")
    print("O valor fica {:.2f}R$".format(total))
elif pagamento == 3:
    print("Em 2x no cartão fica duas parcelas de {}R$".format(compra / 2))
elif pagamento == 4:
    juros = (compra * 20 / 100) 
    total = compra + juros
    totalpa = int(input("Qual total de parcelas? ")) #t Totalpa == Total de parcelas
    parcelas = total / totalpa 
    print("Sua compra será parcelada em {}x de {:.2f}R$, com juros de {:.2f}R$".format(totalpa, parcelas, juros))
elif pagamento > 4:
    print("erro 404")



