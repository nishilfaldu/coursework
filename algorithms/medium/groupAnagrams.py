# O(w * n * log(n)) time | O(wn) space - where w is the number of words
# and n is the length of the longest word
def groupAnagrams(words):
    # Write your code here.
    wordDict = {}
    for word in words:
        sortedWord = "".join(sorted(word))
        if sortedWord not in wordDict:
            wordDict[sortedWord] = []

        wordDict[sortedWord].append(word)

    return list(wordDict.values())
