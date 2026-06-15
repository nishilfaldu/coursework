# O(n) time | O(1) space
def majorityElement(array):
    count = 0
    answer = None
    for value in array:
        # When count hits zero it means we will no longer have a majority element,
        # in the subarray so far, so the number is still a majority element in
        # the rest of subarray
        if count == 0:
            answer = value

        if value == answer:
            count += 1
        else:
            count -= 1

    return answer


[1, 1, 2, 2, 3, 5, 1]
