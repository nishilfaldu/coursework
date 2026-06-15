# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def symmetricalTree(tree):
    # Write your code here.
    return helperSymmetricalTreeFunction(tree.left, tree.right)


def helperSymmetricalTreeFunction(left, right):
    if left is not None and right is not None and left.value == right.value:
        return helperSymmetricalTreeFunction(
            left.left, right.right
        ) and helperSymmetricalTreeFunction(left.right, right.left)

    return left == right


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(h) space
def symmetricalTree(tree):
    # Write your code here.
    leftStack = [tree.left]
    rightStack = [tree.right]

    while len(leftStack) > 0 or len(rightStack) > 0:
        left = leftStack.pop()
        right = rightStack.pop()

        if left is None and right is None:
            continue

        if left is None or right is None or left.value != right.value:
            return False

        leftStack.append(left.left)
        leftStack.append(left.right)
        rightStack.append(right.right)
        rightStack.append(right.left)

    return True
