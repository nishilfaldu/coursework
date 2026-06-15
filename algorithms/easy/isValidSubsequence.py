# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
    arrayIdx = 0
    seqIdx = 0
    while arrayIdx < len(array) and seqIdx < len(sequence):
        if array[arrayIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrayIdx += 1
    return seqIdx == len(sequence)
