import numpy as np


def gaussian_elimination(matrix):
    n = len(matrix)
    for i in range(n):
        # Pivotu bul ve satırları değiştir
        pivot_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[pivot_row][i]):
                pivot_row = j
        matrix[i], matrix[pivot_row] = matrix[pivot_row], matrix[i]

        # i. sütunda altındaki elemanları sıfırla
        for j in range(i + 1, n):
            f = matrix[j][i] / matrix[i][i]
            for k in range(i, n + 1):
                matrix[j][k] -= f * matrix[i][k]

    # Geriye doğru substitüsyon
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i][n] / matrix[i][i]
        for j in range(i - 1, -1, -1):
            matrix[j][n] -= matrix[j][i] * x[i]

    return x


# 4x4 matris örneği
matrix4x4 = [
    [2, 1, -1, 8],
    [-3, -1, 2, -11],
    [-2, 1, 2, -3],
    [1, 2, 3, 12]
]

# 10x10 matris örneği
matrix10x10 = [
    [2, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [-1, 2, -1, 0, 0, 0, 0, 0, 0, 0, -1],
    [0, -1, 2, -1, 0, 0, 0, 0, 0, 0, -1],
    [0, 0, -1, 2, -1, 0, 0, 0, 0, 0, -1],
    [0, 0, 0, -1, 2, -1, 0, 0, 0, 0, -1],
    [0, 0, 0, 0, -1, 2, -1, 0, 0, 0, -1],
    [0, 0, 0, 0, 0, -1, 2, -1, 0, 0, -1],
    [0, 0, 0, 0, 0, 0, -1, 2, -1, 0, -1],
    [0, 0, 0, 0, 0, 0, 0, -1, 2, -1, -1],
    [0, 0, 0, 0, 0, 0, 0, 0, -1, 2, -1]
]

# Doğru matrislerle çözüm yapalım
print("4x4 matris çözümü:", gaussian_elimination(matrix4x4))
print("10x10 matris çözümü:", gaussian_elimination(matrix10x10))
