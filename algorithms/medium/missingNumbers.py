# O(n) time | O(n) space
def missingNumbers(nums):
    # Write your code here.
    includedNums = set(nums)
    result = []
    for num in range(1, len(nums) + 3):
        if num not in includedNums:
            result.append(num)
    return result


# O(n) time | O(1) space
def missingNumbers(nums):
    # Write your code here.
    total = sum(range(1, len(nums) + 3))
    for num in nums:
        total -= num

    averageOfMissingValues = total // 2
    foundFirstHalf = 0
    foundSecondHalf = 0
    for num in nums:
        if num <= averageOfMissingValues:
            foundFirstHalf += num
        else:
            foundSecondHalf += num

    expectedFirstHalf = sum(range(1, averageOfMissingValues + 1))
    expectedSecondHalf = sum(range(averageOfMissingValues + 1, len(nums) + 3))

    return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]
