# O(n) time | O(n) space
def runLengthEncoding(string):
    # Write your code here.
    # The input string is guaranteed to be non-empty,
    # so out first run will be of at least length 1
    result = ""
    runningCharCount = 1
    for idx in range(1, len(string)):
        previousChar = string[idx - 1]
        currentChar = string[idx]

        if previousChar == currentChar and runningCharCount != 9:
            runningCharCount += 1
            continue

        result += str(runningCharCount) + previousChar
        runningCharCount = 1

    return result + str(runningCharCount) + string[len(string) - 1]
