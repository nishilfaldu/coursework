# O(n) time | O(1) space
def moveElementToEnd(array, toMove):
    # Write your code here.
    start = 0
    end = len(array) - 1
    while start < end:
        while array[end] == toMove and end > start:
            end -= 1
        if array[start] == toMove:
            array[start], array[end] = array[end], array[start]
        start += 1
    return array
