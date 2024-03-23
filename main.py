import matplotlib.pyplot as plt

title = "Plot"
curvas = 1
par_ordenado = False
texto_x = "Abscissa"
texto_y = "Ordenada"
separador = "t"

def plot_data():
    global title, curvas, par_ordenado, texto_x, texto_y, separador


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

        if par_ordenado:
            # Questão 4
            separador_dados = input("Qual é o separador de dados do par ordenado? ")
            if not separador_dados:
                separador_dados = separador
            else:
                separador = separador_dados

         # Questão 5
        abscissa_texto = input("Digite o texto do eixo da abscissa: ")
        if not abscissa_texto:
            abscissa_texto = texto_x
        else:
            texto_x = abscissa_texto

        # Questão 6
        ordenada_texto = input("Digite o texto do eixo da ordenada: ")
        if not ordenada_texto:
            ordenada_texto = texto_y
        else:
            texto_y = ordenada_texto

         

        for _ in range(num_curvas):

            abscissa = []
            ordenada = []
            
            print(f"Curva {_+1}/{num_curvas}")

            # Questão 7
            label = input("Digite a legenda da curva: ")

            # Questão 8
            
            if tipo_dados == 1:
                print("Cole os dados da ordenada: ")
                while True:
                    entrada = input()
                    if entrada == '':
                        break
                    ordenada.append(float(entrada))
                
                # Plotar curva
                plt.plot(range(1, len(ordenada) + 1), ordenada, label=label)

                
            else:
                print(f"Cole os dados da abscissa e ordenada separados por \"{separador}\": ")
                while True:
                    entrada = input()
                    if entrada == '':
                        break
                    partes = entrada.split(separador)
                    if len(partes) != 2:
                        print(f"Por favor, insira os dados separados corretamente por \"{separador}\".")
                        continue
                    abscissa.append(float(partes[0]))
                    ordenada.append(float(partes[1]))

                # Questão 9
                
                try:
                    deslocamento = float(input("Digite o deslocamento da abscissa (se necessário): "))
                    if deslocamento:
                        # Subtrai o valor de cada elemento na lista original
                        for i in range(len(abscissa)):
                            abscissa[i] += deslocamento
                except:
                    pass
                

                # Plotar curva
                plt.plot(abscissa, ordenada, label=label)
            



                

     #   plt.rcParams.update({
   #'figure.figsize': (10, 8),    # Tamanho da figura
   # 'font.size': 14,              # Tamanho da fonte geral
   # 'axes.titlesize': 40,         # Tamanho do título
   # 'axes.labelsize': 16,         # Tamanho dos nomes dos eixos
   # 'xtick.labelsize': 14,        # Tamanho dos rótulos do eixo x
   # 'ytick.labelsize': 14,        # Tamanho dos rótulos do eixo y
   #     })

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
