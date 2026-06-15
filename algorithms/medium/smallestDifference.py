# O(nlog(n) + mlog(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    result = []
    arrayOnePtr = 0
    arrayTwoPtr = 0
    minDiffSoFar = float("inf")
    result = [0, 0]
    while arrayOnePtr < len(arrayOne) and arrayTwoPtr < len(arrayTwo):
        firstNum = arrayOne[arrayOnePtr]
        secondNum = arrayTwo[arrayTwoPtr]
        if firstNum < secondNum:
            arrayOnePtr += 1
        elif secondNum < firstNum:
            arrayTwoPtr += 1
        else:
            return [firstNum, secondNum]

        currentDifference = abs(secondNum - firstNum)
        if currentDifference < minDiffSoFar:
            minDiffSoFar = currentDifference
            result = [firstNum, secondNum]

    return result
