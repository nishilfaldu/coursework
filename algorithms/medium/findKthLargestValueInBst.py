# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) time | O(n) space
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    sortedValues = []
    inOrderTraversal(sortedValues, tree)
    return sortedValues[len(sortedValues) - k]


def inOrderTraversal(sortedValues, node):
    if node is None:
        return

    inOrderTraversal(sortedValues, node.left)
    sortedValues.append(node.value)
    inOrderTraversal(sortedValues, node.right)


# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, numberOfNodesVisited, latestVisitedNodeValue):
        self.numberOfNodesVisited = numberOfNodesVisited
        self.latestVisitedNodeValue = latestVisitedNodeValue


# O(h + k) time | O(h) space
def findKthLargestValueInBst(tree, k):
    # Write your code here.
    treeInfo = TreeInfo(0, -1)
    reverseInOrderTraverse(tree, k, treeInfo)
    return treeInfo.latestVisitedNodeValue


def reverseInOrderTraverse(node, k, treeInfo):
    if node is None or treeInfo.numberOfNodesVisited >= k:
        return

    reverseInOrderTraverse(node.right, k, treeInfo)
    if treeInfo.numberOfNodesVisited < k:
        treeInfo.numberOfNodesVisited += 1
        treeInfo.latestVisitedNodeValue = node.value
        reverseInOrderTraverse(node.left, k, treeInfo)
