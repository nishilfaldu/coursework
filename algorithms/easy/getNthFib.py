# O(n) time | O(1) space
def getNthFib(n):
    # Write your code here.
    first = 0
    second = 1
    if n == 1:
        return first
    if n == 2:
        return second

    for i in range(n - 2):
        third = first + second
        first = second
        second = third

    return third
