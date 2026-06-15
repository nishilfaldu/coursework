# O(nlogn) time | O(n) space
def sweetAndSavory(dishes, target):
    # Write your code here.
    savoryDishes = sorted([dish for dish in dishes if dish > 0])
    sweetDishes = sorted([dish for dish in dishes if dish < 0], key=abs)

    bestPair = [0, 0]
    bestDifference = float("inf")
    sweetIndex, savoryIndex = 0, 0

    while sweetIndex < len(sweetDishes) and savoryIndex < len(savoryDishes):
        currentSum = sweetDishes[sweetIndex] + savoryDishes[savoryIndex]

        if currentSum <= target:
            currentDifference = target - currentSum
            if currentDifference < bestDifference:
                bestPair = [sweetDishes[sweetIndex], savoryDishes[savoryIndex]]
                bestDifference = currentDifference
            savoryIndex += 1
        else:
            sweetIndex += 1

    return bestPair
