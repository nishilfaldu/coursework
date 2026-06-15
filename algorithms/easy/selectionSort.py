# Best: O(n^2) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def selectionSort(array):
    # Write your code here.
    minValue = float("inf")
    minValueIdx = 0

    for idx in range(len(array)):
        minValue = array[idx]
        minValueIdx = idx
        for idx_ in range(idx + 1, len(array)):
            if array[idx_] < minValue:
                minValue = array[idx_]
                minValueIdx = idx_

        array[idx], array[minValueIdx] = array[minValueIdx], array[idx]

    return array
