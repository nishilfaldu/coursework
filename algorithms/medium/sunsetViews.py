# O(n) time | O(n) space
def sunsetViews(buildings, direction):
    # Write your code here.
    result = []

    startIdx = 0 if direction == "WEST" else len(buildings) - 1
    step = 1 if direction == "WEST" else -1

    runningMaxHeight = 0
    idx = startIdx
    while idx >= 0 and idx < len(buildings):
        if buildings[idx] > runningMaxHeight:
            result.append(idx)

        runningMaxHeight = max(runningMaxHeight, buildings[idx])

        idx += step

    if direction == "EAST":
        result = result[::-1]

    return result
