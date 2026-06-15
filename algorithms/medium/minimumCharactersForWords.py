# O(n * l) time | O(c) space where n is the number of words,
# l is the length of the longest word, and c is the number of unique
# characters across all words
def minimumCharactersForWords(words):
    # Write your code here.
    resultCharacterFrequencies = {}

    for word in words:
        wordCharacterFrequencies = getCharacterFrequencies(word)
        updateFrequencies(resultCharacterFrequencies, wordCharacterFrequencies)

    return makeArray(resultCharacterFrequencies)


def getCharacterFrequencies(word):
    characterFrequencies = {}

    for character in word:
        if character not in characterFrequencies:
            characterFrequencies[character] = 0
        characterFrequencies[character] += 1

    return characterFrequencies


def updateFrequencies(resultCharacterFrequencies, wordCharacterFrequencies):
    for word in wordCharacterFrequencies:
        if word not in resultCharacterFrequencies:
            resultCharacterFrequencies[word] = wordCharacterFrequencies[word]
        else:
            resultCharacterFrequencies[word] = max(
                resultCharacterFrequencies[word], wordCharacterFrequencies[word]
            )


def makeArray(resultCharacterFrequencies):
    result = []
    for character in resultCharacterFrequencies:
        for _ in range(resultCharacterFrequencies[character]):
            result.append(character)

    return result
