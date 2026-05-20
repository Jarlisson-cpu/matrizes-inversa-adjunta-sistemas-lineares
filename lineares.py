def print_matriz(m):
    for r in m:
        print("[" + " ".join(f"{v:8.3f}" for v in r) + "]")
    print()


def gauss_jordan(aug):
    n, m = len(aug), len(aug[0]) - 1
    row = 0
    for col in range(m):
        p = next((i for i in range(row, n) if abs(aug[i][col]) > 1e-12), None)
        if p is None:
            continue
        aug[row], aug[p] = aug[p], aug[row]
        aug[row] = [v / aug[row][col] for v in aug[row]]
        for i in range(n):
            if i != row:
                f = aug[i][col]
                aug[i] = [aug[i][j] - f * aug[row][j] for j in range(m + 1)]
        row += 1
        if row == n:
            break
    if any(all(abs(aug[i][j]) < 1e-12 for j in range(m)) and abs(aug[i][m]) > 1e-12 for i in range(n)):
        return aug, "none"
    return aug, "infinite" if row < m else "unique"


def resolver_sistema(a, b):
    if len(a) != len(b):
        raise ValueError("Número de equações e termos diferentes.")
    aug = [row + [b[i]] for i, row in enumerate(a)]
    red, status = gauss_jordan(aug)
    if status != "unique":
        return None, status
    sol = [0.0] * len(a[0])
    for row in red:
        p = next((j for j, v in enumerate(row[:-1]) if abs(v) > 1e-12), None)
        if p is not None:
            sol[p] = row[-1]
    return sol, status


def ler_matriz_entrada():
    n = int(input("Quantidade de equações/variáveis: ").strip())
    a = [list(map(float, input(f"Linha {i + 1}: ").split())) for i in range(n)]
    if any(len(row) != n for row in a):
        raise ValueError("Cada linha deve ter n coeficientes.")
    b = list(map(float, input("Termos independentes: ").split()))
    if len(b) != n:
        raise ValueError("Quantidade de termos independentes incorreta.")
    return a, b


def main():
    try:
        a, b = ler_matriz_entrada()
    except Exception as e:
        print("Erro:", e)
        return
    print("\nMatriz aumentada inicial:")
    print_matriz([row + [b[i]] for i, row in enumerate(a)])
    sol, status = resolver_sistema(a, b)
    if status == "none":
        print("O sistema não tem solução.")
    elif status == "infinite":
        print("O sistema tem infinitas soluções.\nMatriz reduzida:")
        print_matriz(gauss_jordan([row + [b[i]] for i, row in enumerate(a)])[0])
    else:
        print("Solução única encontrada:")
        for i, v in enumerate(sol, 1):
            print(f"x{i} = {v:.6f}")


if __name__ == "__main__":
    main()
