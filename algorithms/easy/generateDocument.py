# O(n + m) time | O(x) space - where n is the number of characters, m
# is the number characters in document
def generateDocument(characters, document):
    # Write your code here.
    charDict = {}
    for char in characters:
        if char not in charDict:
            charDict[char] = 0

        charDict[char] += 1

    for char in document:
        if char not in charDict or charDict[char] <= 0:
            return False
        else:
            charDict[char] -= 1

    return True
