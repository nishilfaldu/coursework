# O(wh) time | O(wh) space
def removeIslands(matrix):
    # Write your code here.
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            isRowBorder = row == 0 or row == len(matrix) - 1
            isColBorder = col == 0 or col == len(matrix[row]) - 1
            isBorder = isRowBorder or isColBorder

            if not isBorder:
                continue
            if matrix[row][col] != 1:
                continue

            changeOnesConnectedToBorderToTwos(matrix, row, col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            number = matrix[row][col]
            if number == 2:
                matrix[row][col] = 1
            if number == 1:
                matrix[row][col] = 0

    return matrix


def changeOnesConnectedToBorderToTwos(matrix, startRow, startCol):
    stack = [[startRow, startCol]]

    while len(stack):
        currentNode = stack.pop()
        currentRow, currentCol = currentNode

        matrix[currentRow][currentCol] = 2

        neighbors = getNeighbors(matrix, currentRow, currentCol)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def getNeighbors(matrix, row, col):
    neighbors = []

    if row - 1 >= 0:  # UP
        neighbors.append([row - 1, col])
    if row + 1 < len(matrix):  # DOWN
        neighbors.append([row + 1, col])
    if col - 1 >= 0:  # LEFT
        neighbors.append([row, col - 1])
    if col + 1 < len(matrix[row]):  # RIGHT
        neighbors.append([row, col + 1])
    return neighbors
