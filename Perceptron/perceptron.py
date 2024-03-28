from sklearn.linear_model import Perceptron

# Definindo as entradas

entradas = [[0,0],[0,1],[1,0],[1,1]]

# Definindo as saídas

saidas = [0,0,0,1]

perceptron = Perceptron()

perceptron.fit(entradas,saidas)

pergunta1 = int(input('Digite o primeiro número: '))

pergunta2 = int(input('Digite o segundo número: '))

saida_perceptron = perceptron.predict([[pergunta1,pergunta2]])

if pergunta1 == 1:
    print('A saída é 1, ou seja, o operador é AND')
else:
    print('A saída é 0, ou seja, o outro operador')