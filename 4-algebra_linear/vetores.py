from typing import List

"""
Para se trabalhar com vetores é muito melhor utilizar a lib NumPy,
Onde se encontra uma classe array de alto desempenho com diversas operaćões aritméticas
"""
Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    "Soma os elementos correspondentes"
    assert len(v) == len(w), "Vetores tem o mesmo tamanho"
    return [v_i + w_i for v_i, w_i in zip(v, w)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def subtract(v: Vector, w: Vector) -> Vector:
    "Soma os elementos correspondentes"
    assert len(v) == len(w), "Vetores tem o mesmo tamanho"
    return [v_i - w_i for v_i, w_i in zip(v, w)]


assert subtract([1, 2, 3], [4, 5, 6]) == [-3, -3, -3]


def vector_sum(vectors: List[Vector]) -> Vector:
    "Soma todos os elementos correspondentes"
    # Verifique se os valores não estão vazios
    assert vectors, "no vectors provided"

    # Verifique se os vetores são do mesmo tamanho
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    # O elemento de número i do resultado é a soma de todos vector[i]
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, v: Vector) -> Vector:
    "Multiplica cada elemento por c"
    return [c * v_i for v_i in v]


assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computa a média dos elementos"""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    """Computa v_1 * w_1 + ... + v_n * w_n"""
    assert len(v) == len(w), "vectors must be same length"

    return sum(v_i * w_i for v_i, w_i in zip(v, w))


assert dot([1, 2, 3], [4, 5, 6]) == 32  # 1*4 + 2*5 + 3*6


def sum_of_squares(v: Vector) -> float:
    """Retorna v_1 * v_1 + ... + v_n * v_n"""
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14  # 1*1 + 2*2 + 3*3

import math


def magnitude(v: Vector) -> float:
    """Retorna a magnitude (ou comprimento) de v"""
    return math.sqrt(sum_of_squares(v))  # math.sqrt é a funćão de raiz quadrada


assert magnitude([3, 4]) == 5


def squared_distance(v: Vector, w: Vector) -> float:
    """Computa (v_1 - w_1)**2 + ... + (v_n - w_n)**2"""
    return sum_of_squares(subtract(v, w))


def distance1(v: Vector, w: Vector) -> float:
    """Computa a distância entre v e w"""
    return math.sqrt(squared_distance(v, w))


def distance2(v: Vector, w: Vector) -> float:
    """Computa a distância entre v e w"""
    return magnitude(subtract(v, w))
