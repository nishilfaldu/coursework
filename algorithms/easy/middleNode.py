# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def middleNode(linkedList):
    # Write your code here.
    length = 1
    currentNode = linkedList
    while currentNode.next is not None:
        length += 1
        currentNode = currentNode.next

    distance = length // 2

    anotherCurrentNode = linkedList
    for _ in range(distance):
        anotherCurrentNode = anotherCurrentNode.next

    return anotherCurrentNode
