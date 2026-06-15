# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(max(n, m)) time | O(max(n, m)) space
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    carry = 0
    nodeOne, nodeTwo = linkedListOne, linkedListTwo
    newLinkedList = LinkedList(0)
    currentNewLinkedListNode = newLinkedList
    while nodeOne is not None or nodeTwo is not None or carry != 0:
        nodeOneValue = nodeOne.value if nodeOne is not None else 0
        nodeTwoValue = nodeTwo.value if nodeTwo is not None else 0

        sum = nodeOneValue + nodeTwoValue + carry
        carry = sum // 10
        newNode = LinkedList(sum % 10)

        currentNewLinkedListNode.next = newNode
        currentNewLinkedListNode = currentNewLinkedListNode.next

        nodeOne = nodeOne.next if nodeOne is not None else None
        nodeTwo = nodeTwo.next if nodeTwo is not None else None

    return newLinkedList.next
