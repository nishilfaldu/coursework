# O(n) time | O(n) space
def zeroSumSubarray(nums):
    # Write your code here.
    sumSet = set([0])
    currentSum = 0
    for num in nums:
        currentSum += num
        if currentSum in sumSet:
            return True
        sumSet.add(currentSum)
    return False
