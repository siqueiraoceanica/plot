import matplotlib.pyplot as plt

title = "Plot"
curvas = 1
par_ordenado = False
texto_x = "Abscissa"
texto_y = "Ordenada"

def plot_data():
    while True:
        # Questão 1
        titulo = input("Digite o título do gráfico (ou deixe em branco para manter o anterior ou o padrão): ")
        if not titulo:
            titulo = title
        else:
            title = titulo

        # Questão 2
        num_curvas = int(input("Digite o número de curvas no mesmo plot: "))
        if not num_curvas:
            num_curvas = curvas
        else:
            curvas = num_curvas

        # Questão 3
        tipo_dados = int(input("Os dados são de valores únicos (1) ou pares ordenados (2)? "))
        if not tipo_dados:
            tipo_dados = 2 if par_ordenado else 1
        else:
            par_ordenado = False if tipo_dados == 1 else True

         # Questão 4
        abscissa_texto = input("Digite o texto do eixo da abscissa: ")
        if not abscissa_texto:
            abscissa_texto = texto_x
        else:
            texto_x = abscissa_texto

        # Questão 5
        abscissa_texto = input("Digite o texto do eixo da abscissa: ")
        if not abscissa_texto:
            abscissa_texto = texto_x
        else:
            texto_x = abscissa_texto

         

        for _ in range(num_curvas):
            
            if tipo_dados == '1':
                abscissa = [i+1 for i in range(len(ordenada))]
                abscissa_texto = input("Digite o texto do eixo da abscissa: ")
                ordenada_texto = input("Digite o texto do eixo da ordenada: ")
                ordenada = [float(val) for val in input("Digite os dados da ordenada (separados por espaços): ").split()]
            elif tipo_dados == '2':
                abscissa_texto = input("Digite o texto do eixo da abscissa: ")
                ordenada_texto = input("Digite o texto do eixo da ordenada: ")
                abscissa = [float(val) for val in input("Digite os dados da abscissa (separados por espaços): ").split()]
                ordenada = [float(val) for val in input("Digite os dados da ordenada (separados por espaços): ").split()]
            
            # Plotar curva
            plt.plot(abscissa, ordenada, label=f'Curva {_+1}')

        # Configurar gráfico
        plt.title(titulo)
        plt.xlabel(abscissa_texto)
        plt.ylabel(ordenada_texto)
        plt.legend()
        plt.grid(True)

        # Exibir gráfico
        plt.show()

        # Perguntar se deseja fazer outro plot
        continuar = input("Deseja fazer outro plot? (s/n): ")
        if continuar.lower() != 's':
            break

plot_data()
