# Solution 1: O(n) time | O(h) - where n is the number of nodes and h is the height of binary tree
def nodeDepths(root, depth=0):
    # Write your code here.
    if root is None:
        return 0
    return nodeDepths(root.right, depth + 1) + nodeDepths(root.left, depth + 1) + depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Solution 2: O(n) time | O(h) - where n is the number of nodes and h is the height of binary tree
def nodeDepths(root):
    stack = [{"node": root, "depth": 0}]
    sumOfDepths = 0
    while len(stack) > 0:
        nodeInfo = stack.pop()
        currentNode, currentNodeDepth = nodeInfo["node"], nodeInfo["depth"]
        if currentNode is None:
            continue

        sumOfDepths += currentNodeDepth
        stack.append({"node": currentNode.left, "depth": currentNodeDepth + 1})
        stack.append({"node": currentNode.right, "depth": currentNodeDepth + 1})

    return sumOfDepths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
