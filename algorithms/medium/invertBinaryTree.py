# O(n) time | O(d) space
def invertBinaryTree(tree):
    # Write your code here.
    if tree is None:
        return
    swapNodes(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)


def swapNodes(node):
    node.left, node.right = node.right, node.left


# O(n) time | O(n) space
def invertBinaryTree(tree):
    queue = [tree]
    while len(queue) > 0:
        currentNode = queue.pop(0)
        if currentNode is None:
            continue
        currentNode.left, currentNode.right = currentNode.right, currentNode.left
        queue.append(currentNode.left)
        queue.append(currentNode.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
