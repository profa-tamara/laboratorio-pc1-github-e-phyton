# Escreva as suas respostas neste arquivo.

# Questão 5
# Sua resposta a partir desta linha
G = 3;
T = 3;
soma = (G + T);
print (soma);


# Questão 6
# Sua resposta a partir desta linha
preço = float(input('Qual o preço do livro? R$'))
novo = preço - (preço * 30 / 100)
print ('O preço do livro que custava R${} com desconto é: R${}'. format(preço, novo))

# Questão 7
# Sua resposta a partir desta linha
f = float(input('Informe a temperatura em °f:'))
c = ((f - 32  ) * 5) / 9
print ("A temperatura de {} °F corresponde a {} °C".format (f , c))


# Questão 8
# Sua resposta a partir desta linha
if '99' == 99:
    comparacao1 = print('99 é igual a 99?', True)
else:
    comparacao1 = print('99 é igual a 99?', False)

if 25 > 39:
    comparacao2 = print('25 é maior do que 39?', True)
else:
    comparacao2 = print ('25 é maior do que 39?', False)
    
if 0.9 <= 0.8:
    comparacao3 = print ('0,9 é menor ou igual a 0,8?', True)
else:
    comparacao3 = print ('0,9 é menor ou igual a 0,8?', False)
    
if 71 >= 60:
    comparacao4 = print ('71 é maior ou igual a 60?', True)
else:
    comparacao4 = print ('71 é maior ou igual a 60?', False)
