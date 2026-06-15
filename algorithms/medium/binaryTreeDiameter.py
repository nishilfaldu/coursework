# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binaryTreeDiameter(tree):
    # Write your code here.
    return getTreeInfo(tree).diameter


def getTreeInfo(tree):
    if tree is None:
        return TreeInfo(0, 0)

    leftTreeInfo = getTreeInfo(tree.left)
    rightTreeInfo = getTreeInfo(tree.right)

    longestPathThroughRoot = leftTreeInfo.height + rightTreeInfo.height
    currentDiameter = max(
        leftTreeInfo.diameter, rightTreeInfo.diameter, longestPathThroughRoot
    )
    currentHeight = max(leftTreeInfo.height, rightTreeInfo.height) + 1

    return TreeInfo(currentDiameter, currentHeight)
