# O(n) time | O(1) space
def sortedSquaredArray(array):
    # Write your code here.
    result = [0 for _ in range(len(array))]
    leftPtr = 0
    rightPtr = len(array) - 1
    resultPtr = len(array) - 1
    while leftPtr <= rightPtr:
        if abs(array[leftPtr]) >= abs(array[rightPtr]):
            result[resultPtr] = abs(array[leftPtr]) ** 2
            leftPtr += 1
        else:
            result[resultPtr] = abs(array[rightPtr]) ** 2
            rightPtr -= 1
        resultPtr -= 1

    return result
