# Escreva as suas respostas neste arquivo.

# Questão 5
# Sua resposta a partir desta linha
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
soma = valor1 + valor2
print("A soma entre", valor1, "e", valor2, "é igual a", soma)

# Questão 6
# Sua resposta a partir desta linha
preço = float(input("Digite o preço da mercadoria:"))
desconto = 30
valor_do_desconto = preço * desconto / 100
a_pagar = preço - valor_do_desconto
print("Um desconto de %5.2f %% em uma mercadoria de R$ %7.2f" % (desconto, preço))
print("vale R$ %7.2f." % valor_do_desconto)
print("O preço do livro com desconto é: R$ %7.2f" % a_pagar)

# Questão 7
# Sua resposta a partir desta linha
tempC = float(input('informe a temperatura em °F'))
tempF = ((tempC - 32) / 1.8) 
print('A temperatura de {}°F corresponde a {}°C'.format(tempC,tempF))

# Questão 8
# Sua resposta a partir desta linha
x = float(input("O seginte número é igual a 99?: "))
y = float(input("O seguinte número é maior que 39?: "))
w = float(input("O seguinte número é menor ou igual a 0.8?: "))
z = float(input("O seguinte número é maior ou igual a 60?: "))

igual_a_99 = x == 99
maior_que_39 = y > 39
menor_ou_igual_a_0_8 = w <= 0.8
maior_ou_igual_a_60 = z >= 60

print("Perguntas:")
print("1. O número x é igual a 99?")
print("2. O número y é maior que 39?")
print("3. O número w é menor ou igual a 0.8?")
print("4. O número z é maior ou igual a 60?")

print("Respostas:")
print("1. ", igual_a_99)
print("2. ", maior_que_39)
print("3. ", menor_ou_igual_a_0_8)
print("4. ", maior_ou_igual_a_60)
