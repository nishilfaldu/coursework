# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    # Write your code here.
    closestValueSoFar = tree.value
    currentNode = tree
    minDiffSoFar = float("inf")

    while currentNode is not None:
        if abs(currentNode.value - target) < minDiffSoFar:
            minDiffSoFar = abs(currentNode.value - target)
            closestValueSoFar = currentNode.value

        if currentNode.value == target:
            return currentNode.value
        elif currentNode.value > target:
            currentNode = currentNode.left
        elif currentNode.value < target:
            currentNode = currentNode.right

    return closestValueSoFar


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
