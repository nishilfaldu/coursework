# O(n) time | O(n) space - where n is the number of nodes in a binary tree
# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    result = []
    runningSum = 0
    return helperBranchSums(root, result, runningSum)


def helperBranchSums(node, result, runningSum):
    if node is None:
        return

    runningSum += node.value
    if node.left is None and node.right is None:
        result.append(runningSum)
        # return - doesn't matter if it's there or not!

    helperBranchSums(node.left, result, runningSum)
    helperBranchSums(node.right, result, runningSum)

    return result
