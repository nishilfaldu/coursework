# O(nlog(n)) time | O(n) space
# Comparing the interval to the left
def mergeOverlappingIntervals(intervals):
    # Write your code here.
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)
    
    for nextInterval in sortedIntervals:
        currentIntervalLeft, currentIntervalRight = currentInterval
        nextIntervalLeft, nextIntervalRight = nextInterval

        if currentIntervalRight >= nextIntervalLeft:
            currentInterval[1] = max(currentIntervalRight, nextIntervalRight)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)
        
    return mergedIntervals
