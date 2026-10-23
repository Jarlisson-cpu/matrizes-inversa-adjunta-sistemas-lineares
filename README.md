# 🧮 Matrizes: Determinante, Adjunta, Inversa e Sistemas Lineares

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)

Implementação **do zero, em Python puro** (sem NumPy), de operações clássicas de **Álgebra Linear**.

## 📄 Arquivos

### `matriz.py`
- **Determinante** por recursão e **expansão de Laplace**
- **Matriz de cofatores**
- **Transposta**
- **Matriz adjunta** (transposta da matriz de cofatores)
- **Inversa** pelo método da adjunta: `A⁻¹ = adj(A) / det(A)` (com erro para matriz singular)

### `lineares.py`
- Resolução de sistemas lineares por **Gauss-Jordan** com pivoteamento
- Classifica o sistema em **solução única**, **infinitas soluções** ou **sem solução**
- Leitura interativa dos coeficientes pelo terminal

## 🚀 Como executar

```bash
python matriz.py      # mostra a inversa de uma matriz 3x3 de exemplo
python lineares.py    # pede as equações no terminal
```

Exemplo de entrada para `lineares.py`:

```
Quantidade de equações/variáveis: 2
Linha 1: 2 1
Linha 2: 1 3
Termos independentes: 5 10
```

## 🧠 Conceitos praticados

Recursão · list comprehensions · álgebra linear · precisão numérica com tolerância (`1e-12`)

---

👤 Feito por **[Jarlisson Brito](https://github.com/Jarlisson-cpu)** · [LinkedIn](https://www.linkedin.com/in/jarlisson-brito-602909368/)
