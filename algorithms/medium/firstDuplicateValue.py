# O(n) time | O(1) space
def firstDuplicateValue(array):
    # Write your code here.
    for num in array:
        absoluteValue = abs(num)
        if array[absoluteValue - 1] < 0:
            return absoluteValue
        array[absoluteValue - 1] *= -1
    return -1
