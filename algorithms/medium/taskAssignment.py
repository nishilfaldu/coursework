# O(nlogn) time | O(n) space
def taskAssignment(k, tasks):
    # Write your code here.
    pairedTasks = []
    taskDurationsToIndices = getTaskDurationsToIndices(tasks)

    sortedTasks = sorted(tasks)
    for idx in range(k):
        taskDuration1 = sortedTasks[idx]
        taskDuration1Indices = taskDurationsToIndices[taskDuration1]
        task1Index = taskDuration1Indices.pop()

        taskDuration2 = sortedTasks[len(tasks) - idx - 1]
        taskDuration2Indices = taskDurationsToIndices[taskDuration2]
        task2Index = taskDuration2Indices.pop()

        pairedTasks.append([task1Index, task2Index])

    return pairedTasks


def getTaskDurationsToIndices(tasks):
    taskDurationsToIndices = {}

    for idx, taskDuration in enumerate(tasks):
        if taskDuration not in taskDurationsToIndices:
            taskDurationsToIndices[taskDuration] = []

        taskDurationsToIndices[taskDuration].append(idx)

    return taskDurationsToIndices
