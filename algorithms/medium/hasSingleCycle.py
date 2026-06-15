# O(n) time | O(1) space
def hasSingleCycle(array):
    # Write your code here.
    numElementsVisited = 0
    currentIdx = 0
    while numElementsVisited < len(array):
        if numElementsVisited > 0 and currentIdx == 0:
            return False
        numElementsVisited += 1
        currentIdx = getNextIdx(array, currentIdx)
    return currentIdx == 0


def getNextIdx(array, currentIdx):
    jump = array[currentIdx]
    nextIdx = (currentIdx + jump) % len(array)
    return nextIdx if nextIdx >= 0 else nextIdx + len(array)
