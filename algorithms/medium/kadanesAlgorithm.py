# O(n) time | O(1) space
def kadanesAlgorithm(array):
    # Write your code here.
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for idx in range(1, len(array)):
        maxEndingHere = max(maxEndingHere + array[idx], array[idx])
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar
