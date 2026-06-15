# O(n^2) time | O(n) space
def longestPalindromicSubstring(string):
    # Write your code here.
    currentMaxLengthOfPalindrome = [0, 1]
    for idx in range(1, len(string)):
        oddString = checkIfPalindrome(idx - 1, idx + 1, string)
        evenString = checkIfPalindrome(idx - 1, idx, string)
        maxFromOddAndEvenString = max(oddString, evenString, key=lambda x: x[1] - x[0])
        currentMaxLengthOfPalindrome = max(
            currentMaxLengthOfPalindrome,
            maxFromOddAndEvenString,
            key=lambda x: x[1] - x[0],
        )

    return string[currentMaxLengthOfPalindrome[0] : currentMaxLengthOfPalindrome[1]]


def checkIfPalindrome(leftIdx, rightIdx, string):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1

    return [leftIdx + 1, rightIdx]
