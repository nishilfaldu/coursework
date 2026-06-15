# O(n) time | O(1) space - n is the length of string and the constant space
# is because our hash table cannot have more than 26 characters
def firstNonRepeatingCharacter(string):
    # Write your code here.
    charDict = {}
    for char in string:
        if char not in charDict:
            charDict[char] = 0
        charDict[char] += 1

    for idx, char in enumerate(string):
        if charDict[char] == 1:
            return idx

    return -1
