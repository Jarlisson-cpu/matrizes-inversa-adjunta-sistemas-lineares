def print_matriz(m):
    # Exibe a matriz formatada com duas casas decimais
    for linha in m:
        print("[" + " ".join(f"{x:7.2f}" for x in linha) + "]")
    print()


def get_submatriz(m, linha_fora, col_fora):
    # Retorna o menor complementar removendo linha e coluna especificadas
    return [[m[i][j] for j in range(len(m)) if j != col_fora]
            for i in range(len(m)) if i != linha_fora]


def det(m):
    # Calcula o determinante por recursão e expansão de Laplace
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    return sum(((-1) ** j) * m[0][j] * det(get_submatriz(m, 0, j)) for j in range(n))


def matriz_cofatores(m):
    # Cria a matriz de cofatores usando determinantes dos menores
    return [[((-1) ** (i + j)) * det(get_submatriz(m, i, j))
             for j in range(len(m))]
            for i in range(len(m))]


def transpose(m):
    # Transpõe a matriz (linhas viram colunas)
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]


def matriz_adjacente(m):
    # Retorna a matriz adjunta (transposta da matriz de cofatores)
    return transpose(matriz_cofatores(m))


def inversa(m):
    # Calcula a inversa usando adjunta e determinante
    d = det(m)
    if d == 0:
        raise ValueError("Matriz singular sem inversa.")
    return [[v / d for v in linha] for linha in matriz_adjacente(m)]


if __name__ == "__main__":
    matriz = [[4, 7, 2], [3, 6, 1], [2, 5, 3]]
    print("Matriz original:")
    print_matriz(matriz)
    try:
        print("Matriz inversa pelo método da adjunta:")
        print_matriz(inversa(matriz))
    except ValueError as e:
        print(e)
