# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n + m) time | O(1) space - where n is the length of the
# first Linked List, and m is the length of the second Linked List
def mergingLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    currentNodeOne = linkedListOne
    currentNodeTwo = linkedListTwo

    while currentNodeOne is not currentNodeTwo:
        if not currentNodeOne:
            currentNodeOne = linkedListTwo
        else:
            currentNodeOne = currentNodeOne.next

        if not currentNodeTwo:
            currentNodeTwo = linkedListOne
        else:
            currentNodeTwo = currentNodeTwo.next

    return currentNodeOne
