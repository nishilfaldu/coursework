# O(nlog(n)) time | O(1) space - where n is the number of students
def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redsAreTaller = True
    bluesAreTaller = True
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] > blueShirtHeights[i]:
            bluesAreTaller = False
        elif redShirtHeights[i] < blueShirtHeights[i]:
            redsAreTaller = False
        else:
            return False
    return redsAreTaller or bluesAreTaller
