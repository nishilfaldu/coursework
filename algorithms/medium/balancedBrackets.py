# O(n) time | O(n) space
def balancedBrackets(string):
    stack = []
    openingBrackets = "[{("
    closingBrackets = "]})"
    brackets = {"]": "[", ")": "(", "}": "{"}
    for char in string:
        if char in openingBrackets:
            stack.append(char)
        elif char in closingBrackets:
            if len(stack) == 0:
                return False
            if stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
