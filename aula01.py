# faz a importação da biblioteca matplotlib e adiciona um alias (apelido)
#usar linha de comando: python3 -m pip install matplotlib
import matplotlib.pyplot as plt

def ExibirGrafico():
  #definição dos grupos e valores 
  grupos= ['A', 'B', 'C']
  valores = [23, 38, 12]

  # configura um grafico de barras, onde recebe os grupos, valores
  # E opcionalmente as cores 
  plt.bar(grupos, valores, color=['red', 'blue', 'grey'])

  # define o titulo gráfico
  plt.title('gráfico de barras simples')

  # define o titulo do eixo x
  plt.xlabel('grupos')


