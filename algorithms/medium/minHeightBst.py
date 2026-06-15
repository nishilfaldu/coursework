def minHeightBst(array):
    return constructBst(array, 0, len(array) - 1)


# O(n) time | O(n) space
def constructBst(array, startIdx, endIdx):
    if endIdx < startIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    bst = BST(array[midIdx])
    bst.left = constructBst(array, startIdx, midIdx - 1)
    bst.right = constructBst(array, midIdx + 1, endIdx)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
