# O(n * m) time | O(n * m) space - where n is the number of words
# and m is length of the longest word
def semordnilap(words):
    # Write your code here.
    wordSet = set(words)
    result = []
    for word in words:
        reversedWord = word[::-1]
        if reversedWord in wordSet and reversedWord != word:
            result.append([word, reversedWord])
            wordSet.remove(reversedWord)
            wordSet.remove(word)
    return result
