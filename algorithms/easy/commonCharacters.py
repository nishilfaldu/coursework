# O(n * m) time | O(c) space - where n is the number of strings,
# m is the length of the longest string, and c is the number of unique
# characters across all strings
def commonCharacters(strings):
    # Write your code here.
    characterCounts = {}
    for string in strings:
        uniqueStringCharacters = set(string)
        for character in uniqueStringCharacters:
            if character not in characterCounts:
                characterCounts[character] = 0
            characterCounts[character] += 1

    result = []
    for character, count in characterCounts.items():
        if count == len(strings):
            result.append(character)

    return result


# O(n * m) time | O(m) space - where n is the number of strings,
# m is the length of the longest string, and m is the length of the
# longest string
def commonCharacters(strings):
    # Write your code here.
    smallestString = getSmallestString(strings)
    potentialCommonCharacters = set(smallestString)

    for string in strings:
        removeNonexistentCharacters(string, potentialCommonCharacters)

    return list(potentialCommonCharacters)


def getSmallestString(strings):
    currentSmallestLen = float("inf")
    currentSmallestString = strings[0]
    for string in strings:
        if currentSmallestLen > len(string):
            currentSmallestLen = len(string)
            currentSmallestString = string
    return currentSmallestString


def removeNonexistentCharacters(string, potentialCommonCharacters):
    uniqueCharacters = set(string)

    for character in list(potentialCommonCharacters):
        if character not in uniqueCharacters:
            potentialCommonCharacters.remove(character)
