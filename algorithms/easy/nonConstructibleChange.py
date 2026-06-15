# O(n) time | O(1) space
def nonConstructibleChange(coins):
    # Write your code here.
    changeSoFar = 0
    coins.sort()
    for value in coins:
        if value > changeSoFar + 1:
            return changeSoFar + 1
        else:
            changeSoFar += value

    return changeSoFar + 1
