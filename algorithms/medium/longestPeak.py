# O(n) time | O(1) space
def longestPeak(array):
    # Write your code here.
    longestPeakLength = 0
    idx = 1
    while idx < len(array) - 1:
        isPeak = False
        if array[idx] > array[idx - 1] and array[idx] > array[idx + 1]:
            isPeak = True

        if not isPeak:
            idx += 1
            continue

        leftPtr = idx - 2
        while leftPtr >= 0 and array[leftPtr] < array[leftPtr + 1]:
            leftPtr -= 1
        rightPtr = idx + 2
        while rightPtr < len(array) and array[rightPtr] < array[rightPtr - 1]:
            rightPtr += 1

        currentLength = rightPtr - leftPtr - 1
        longestPeakLength = max(longestPeakLength, currentLength)
        idx = rightPtr

    return longestPeakLength
