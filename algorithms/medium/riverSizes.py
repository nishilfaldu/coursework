# O(wh) time | O(wh) space
def riverSizes(matrix):
    # Write your code here.
    riverSizes = []
    visited = [[False for col in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(i, j, visited, riverSizes, matrix)
    return riverSizes


def traverseNode(i, j, visited, riverSizes, matrix):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i, j = currentNode
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        univisitedNeighbors = getUnvisitedNeighbors(i, j, visited, matrix)
        for neighbor in univisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currentRiverSize > 0:
        riverSizes.append(currentRiverSize)


def getUnvisitedNeighbors(i, j, visited, matrix):
    unvisitedNeighbors = []
    if i > 0 and not visited[i - 1][j]:
        unvisitedNeighbors.append([i - 1, j])
    if j > 0 and not visited[i][j - 1]:
        unvisitedNeighbors.append([i, j - 1])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisitedNeighbors.append([i + 1, j])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisitedNeighbors.append([i, j + 1])

    return unvisitedNeighbors
