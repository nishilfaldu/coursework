# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def splitBinaryTree(tree):
    # Write your code here.
    desiredSubtreeSum = getTreeSum(tree) / 2
    canBeSplit = trySubtrees(tree, desiredSubtreeSum)[0]
    return desiredSubtreeSum if canBeSplit else 0


def trySubtrees(tree, desiredSubtreeSum):
    if tree is None:
        return (False, 0)

    leftSubTreeCanBeSplit, leftSubtreeSum = trySubtrees(tree.left, desiredSubtreeSum)
    rightSubTreeCanBeSplit, rightSubtreeSum = trySubtrees(tree.right, desiredSubtreeSum)

    currentTreeSum = tree.value + leftSubtreeSum + rightSubtreeSum
    canBeSplit = (
        leftSubTreeCanBeSplit
        or rightSubTreeCanBeSplit
        or currentTreeSum == desiredSubtreeSum
    )

    return (canBeSplit, currentTreeSum)


def getTreeSum(tree):
    if tree is None:
        return 0
    return tree.value + getTreeSum(tree.left) + getTreeSum(tree.right)
