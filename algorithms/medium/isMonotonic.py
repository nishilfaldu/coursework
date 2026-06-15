# O(n) time | O(1) space
def isMonotonic(array):
    # Write your code here.
    isNonDecreasing = True
    isNonIncreasing = True
    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            isNonDecreasing = False
        elif array[i] > array[i - 1]:
            isNonIncreasing = False

    return isNonDecreasing or isNonIncreasing
