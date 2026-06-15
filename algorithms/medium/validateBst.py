# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(d) space
def validateBst(tree):
    # Write your code here.
    return helperBst(tree, float("-inf"), float("inf"))


def helperBst(node, minValue, maxValue):
    if node is None:
        return True
    if node.value < minValue or node.value >= maxValue:
        return False
    isLeftValidBst = helperBst(node.left, minValue, node.value)
    isRightValidBst = helperBst(node.right, node.value, maxValue)

    return isLeftValidBst and isRightValidBst
