def row_sum(matrix, row):
    return matrix[row][0] + matrix[row][1]+matrix[row][2]

def col_sum(matrix, col):
    return matrix[0][col] + matrix[1][col]+matrix[2][col]

def main():
    matrix = []
    for i in range(3):
        row = list(map(int, input().split()))
        matrix.append(row)
    print("Row sums:")
    for i in range(0,3):
        print(f"Row {i+1}: {row_sum(matrix, i)}")
    print("COlumn sums: ")
    for i in range(0, 3):
        print(f"Column {i+1}: {col_sum(matrix, i)}")


main()




