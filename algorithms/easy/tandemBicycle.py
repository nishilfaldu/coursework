# O(nlog(n)) time | O(1) space - where n is the number of tandem bicycles
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    redShirtSpeeds.sort()
    if fastest:
        blueShirtSpeeds = sorted(blueShirtSpeeds, reverse=True)
    else:
        blueShirtSpeeds.sort()

    print(redShirtSpeeds, blueShirtSpeeds)

    totalSpeed = 0
    for i in range(len(redShirtSpeeds)):
        totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[i])

    return totalSpeed
