# O(n) time | O(1) space
def oneEdit(stringOne, stringTwo):
    # Write your code here.
    lengthOne, lengthTwo = len(stringOne), len(stringTwo)
    if abs(lengthOne - lengthTwo) > 1:
        return False

    madeEdit = False
    indexOne = 0
    indexTwo = 0

    while indexOne < lengthOne and indexTwo < lengthTwo:
        if stringOne[indexOne] != stringTwo[indexTwo]:
            if madeEdit:
                return False
            madeEdit = True

            if lengthOne > lengthTwo:
                indexOne += 1
            elif lengthTwo > lengthOne:
                indexTwo += 1
            else:
                indexOne += 1
                indexTwo += 1
        else:
            indexOne += 1
            indexTwo += 1

    return True
