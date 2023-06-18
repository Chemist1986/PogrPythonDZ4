def transpose_matrix(matrix):
    # Получаем количество строк и столбцов исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Создаем новую матрицу с количеством строк равным количеству столбцов исходной матрицы,
    # и количеством столбцов равным количеству строк исходной матрицы
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    # Заполняем новую матрицу значениями, транспонируя исходную матрицу
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

matrix = [[1, 2, 3],
          [4, 5, 6]]

transposed_matrix = transpose_matrix(matrix)

print(transposed_matrix)