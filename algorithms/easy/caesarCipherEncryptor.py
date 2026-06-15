# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    # Write your code here.
    newKey = key % 26
    result = ""
    for char in string:
        charNum = ord(char)
        newCharNum = charNum + newKey
        if newCharNum <= 122:
            newChar = chr(newCharNum)
        else:
            newChar = chr(96 + (newCharNum % 122))

        result += newChar

    return result
