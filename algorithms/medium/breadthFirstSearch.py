# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # O(v + e) time | O(v) space
    def breadthFirstSearch(self, array):
        # Write your code here.
        stack = [self]
        while len(stack) > 0:
            node = stack.pop(0)
            array.append(node.name)
            for child in node.children:
                stack.append(child)

        return array
