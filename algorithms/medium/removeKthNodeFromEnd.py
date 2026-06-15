# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space
def removeKthNodeFromEnd(head, k):
    # Write your code here.
    first, second = head, head
    for _ in range(k):
        second = second.next

    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while second.next is not None:
        first = first.next
        second = second.next
    first.next = first.next.next
