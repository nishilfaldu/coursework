# O(n^2) time | O(d) space - where n is the number of nodes in a tree
# and d is the depth of the tree
def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    return areSameBsts(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))


def areSameBsts(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo

    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False

    leftRootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, minVal)
    leftRootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxTwo, minVal)
    rightRootIdxOne = getIdxOfFirstBiggerOrEqual(arrayOne, rootIdxOne, maxVal)
    rightRootIdxTwo = getIdxOfFirstBiggerOrEqual(arrayTwo, rootIdxTwo, maxVal)

    currentVal = arrayOne[rootIdxOne]
    leftAreSame = areSameBsts(
        arrayOne, arrayTwo, leftRootIdxOne, leftRootIdxTwo, minVal, currentVal
    )
    rightAreSame = areSameBsts(
        arrayOne, arrayTwo, rightRootIdxOne, rightRootIdxTwo, currentVal, maxVal
    )
    return leftAreSame and rightAreSame


def getIdxOfFirstSmaller(array, startIdx, minVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] < array[startIdx] and array[i] >= minVal:
            return i
    return -1


def getIdxOfFirstBiggerOrEqual(array, startIdx, maxVal):
    for i in range(startIdx + 1, len(array)):
        if array[i] >= array[startIdx] and array[i] < maxVal:
            return i
    return -1
