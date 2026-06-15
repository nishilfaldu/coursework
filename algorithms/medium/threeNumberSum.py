# O(n^2) time | O(n) space
def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    result = []
    for idx in range(len(array) - 2):
        currentNum = array[idx]
        leftPtr = idx + 1
        rightPtr = len(array) - 1
        while leftPtr < rightPtr:
            currentSum = array[leftPtr] + array[rightPtr] + currentNum
            if currentSum < targetSum:
                leftPtr += 1
            elif currentSum > targetSum:
                rightPtr -= 1
            else:
                result.append([currentNum, array[leftPtr], array[rightPtr]])
                leftPtr += 1
                rightPtr -= 1

    return result
