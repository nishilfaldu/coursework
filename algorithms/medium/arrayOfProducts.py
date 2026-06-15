# O(n) time | O(n) space
def arrayOfProducts(array):
    # Write your code here.
    result = [1 for _ in range(len(array))]
    leftProductSum = [1 for _ in range(len(array))]
    rightProductSum = [1 for _ in range(len(array))]

    leftRunningProduct = 1
    for i in range(len(array)):
        leftProductSum[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        rightProductSum[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        result[i] = leftProductSum[i] * rightProductSum[i]

    return result
