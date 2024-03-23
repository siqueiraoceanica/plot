# Captura as linhas de entrada
print("Cole os dados, uma linha por vez. Pressione Enter após cada linha. Pressione Enter duas vezes para finalizar.")

dados = []
while True:
    try:
        entrada = input()
        if entrada == '':
            break
        dados.append(float(entrada))
    except ValueError:
        print("Por favor, insira apenas números válidos.")

# Imprime o vetor resultante
print("Vetor resultante:", dados)