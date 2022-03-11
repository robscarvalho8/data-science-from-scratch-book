"""
Usaremos letras maiúsculas para representar matrizes
"""

from typing import List, Tuple, Callable

Vector = List[float]
Matrix = List[List[float]]

# A tem 2 linhas e 3 colunas
A = [
    [1, 2, 3],
    [4, 5, 6],
]

# B tem 3 linhas e 2 colunas
B = [
    [1, 2],
    [2, 3],
    [4, 5],
]


def shape(A: Matrix) -> Tuple[int, int]:
    """Retorna (número de linhas de A, números de colunas de A)"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0  # núemro de elementos na primeira linha
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 Linha, 3 Colunas (Matriz 2x3)


def get_row(A: Matrix, i: int) -> Vector:
    """Retorna a linha i de A (como um Vector)"""
    return A[i]  # A[i] já está na linha i


def get_column(A: Matrix, j: int) -> Vector:
    """Retorna a coluna j de A (como um Vector)"""
    return [A_i[j] for A_i in A]  # elemento j da linha A_i  for (para cada linha A_i)


def make_matrix(
    num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]
) -> Matrix:
    """
    Retorna uma matriz num_rows x num_cols
    cuja entrada (i, j) é entry_fn(i, j)
    """
    return [[entry_fn(i, j) for j in range(num_cols)] for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """Retorna a matriz de identidada nxn"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1],
]
