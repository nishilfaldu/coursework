# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    # Write your code here.
    nums = {}
    for num in array:
        numToFind = targetSum - num
        if numToFind in nums:
            return [numToFind, num]
        else:
            nums[num] = True
    return []
