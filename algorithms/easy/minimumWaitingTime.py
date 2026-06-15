# O(nlogn) time | O(1) space - where n is the number of queries
def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    totalWaitingTime = 0
    for idx, waitTime in enumerate(queries):
        totalWaitingTime += waitTime * ((len(queries)) - idx - 1)

    return totalWaitingTime
