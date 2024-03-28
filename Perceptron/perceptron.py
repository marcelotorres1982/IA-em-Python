# Importando Perceptron da lib scikit-learn

from sklearn.linear_model import Perceptron

# Definindo as entradas e saídas

entradas = [[0,0],[0,1],[1,0],[1,1]]
saidas = [0,0,0,1]

# Criando o Perceptron
perceptron = Perceptron()

# Treinando o Perceptron
perceptron.fit(entradas,saidas)

# Interagindo com o usuário
pergunta1 = int(input('Digite o primeiro número: '))
pergunta2 = int(input('Digite o segundo número: '))

# Informando a saída
saida_perceptron = perceptron.predict([[pergunta1,pergunta2]])

# Verificando a saída
if saida_perceptron == 1:
    print('A saída é 1, ou seja, o operador é AND')
else:
    print('A saída é 0, ou seja, o outro operador')
