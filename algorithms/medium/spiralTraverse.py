# O(n) time | O(n) space - where n is the total number of elements in the array
def spiralTraverse(array):
    # Write your code here.
    startRow = 0
    startCol = 0
    endRow = len(array) - 1
    endCol = len(array[0]) - 1
    res = []
    while startRow <= endRow and startCol <= endCol:
        for i in range(startCol, endCol + 1):
            res.append(array[startRow][i])
        for i in range(startRow + 1, endRow + 1):
            res.append(array[i][endCol])
        for i in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            res.append(array[endRow][i])
        for i in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            res.append(array[i][startRow])
        startRow += 1
        endRow -= 1
        startCol += 1
        endCol -= 1
    return res
