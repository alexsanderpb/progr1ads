valor_litro = float(input("Informe o valor do litro: "))
valor_reais = float(input("Quanto quer abastecer? "))
litros = valor_reais / valor_litro
print("Com R$ %.2f o veiculo vai receber %.2f litros." % (valor_reais, litros))
