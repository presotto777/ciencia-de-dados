import matplotlib.pyplot as plt
 
 #importa a biblioteca pandas
import pandas as pd

def exibirgrafico():
    #cria a dataframe
    df = pd.DataFrame({
        "meses":['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'],
        "temperaturas":[29, 31, 30, 28, 27, 25, 21, 24, 27, 28, 29, 33]
    })

    #redimensionando o grafico
    plt.figure(figsize=[10.0, 5.0])

    #criação do grafico
    plt.plot(df['meses'], df ['temperatura'],color="green")

    #definição de titulos
    plt.title("temperatura média ao longo do tempo")
    plt.xlabel("Meses")
    plt.ylabel("Temperatura")

    # Exibindo grafico
    plt.show()
    plt.savefig('chart2.png')

    # exibe no console dados estatisticos
    print(f'Temperaturas: \n{df['Temperaturas'].describe()}')