def transposeMatrix(matrix):
    # Write your code here.
    result = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        result.append(newRow)

    return result


# [
#     [5,6,7],
#     [2,3,4],
#     [7,8,9]
# ]
