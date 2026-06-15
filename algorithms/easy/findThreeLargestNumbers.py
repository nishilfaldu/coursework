# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    # Write your code here.
    result = [float("-inf") for _ in range(3)]
    for num in array:
        if num > result[2]:
            result[0] = result[1]
            result[1] = result[2]
            result[2] = num
        elif num > result[1]:
            result[0] = result[1]
            result[1] = num
        elif num > result[0]:
            result[0] = num

    return result
