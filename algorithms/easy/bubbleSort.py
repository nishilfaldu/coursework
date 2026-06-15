# Best: O(n) time | O(1) space
# Average: O(n^2) time | O(1) space
# Worst: O(n^2) time | O(1) space
def bubbleSort(array):
    # Write your code here.
    isSorted = False
    while not isSorted:
        isSorted = True
        for idx in range(1, len(array)):
            if array[idx] < array[idx - 1]:
                array[idx], array[idx - 1] = array[idx - 1], array[idx]
                isSorted = False
    return array
