# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time | O(1) space - where d is the depth (or height) of the ancestral tree
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # Write your code here.
    depthOne = getDescendantDepth(topAncestor, descendantOne)
    depthTwo = getDescendantDepth(topAncestor, descendantTwo)
    if depthOne > depthTwo:
        return backTrackAncestralTree(descendantOne, descendantTwo, depthOne - depthTwo)
    else:
        return backTrackAncestralTree(descendantTwo, descendantOne, depthTwo - depthOne)


def getDescendantDepth(topAncestor, descendant):
    depth = 0
    while descendant != topAncestor:
        depth += 1
        descendant = descendant.ancestor

    return depth


def backTrackAncestralTree(lowerDescendant, higherDescendant, diff):
    while diff > 0:
        lowerDescendant = lowerDescendant.ancestor
        diff -= 1
    while lowerDescendant != higherDescendant:
        lowerDescendant = lowerDescendant.ancestor
        higherDescendant = higherDescendant.ancestor
    return lowerDescendant
