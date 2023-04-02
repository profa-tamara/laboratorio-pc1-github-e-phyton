# Escreva as suas respostas neste arquivo.

# Questão 5
# Sua resposta a partir desta linha
num1=2
num2=4
print(num1+num2)

# Questão 6
# Sua resposta a partir desta linha
livro=30
desconto=0.3
print("O preço do livro com desconto de 30% é de: R$ "+livro*desconto)

# Questão 7
# Sua resposta a partir desta linha
def menu_inicial():
    print('Conversão de Temperaturas')

def fahr_cel():
    F = float(input('Informe temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

# Questão 8
# Sua resposta a partir desta linha
a=99
b=25
c=39
d=0.9
e=0.8
f=71
g=60
h=a=a  #compara se 99=99
i=b>c  #compara se 25>39
j=d<=e #compara se 0.9<=0.8
k=f>=g #compara se 71>=60

print("Resultado de h: ", h)
print("Resultado de i: ", i)
print("Resultado de j: ", j)
print("Resultado de k: ", k)