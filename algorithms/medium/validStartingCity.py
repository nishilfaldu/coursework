# O(n) time | O(1) space
def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    numberOfCities = len(distances)
    milesRemaining = 0

    indexOfValidStartingCity = 0
    milesRemainingAtValidStartingCity = 0

    for idx in range(1, numberOfCities):
        previousCityDistance = distances[idx - 1]
        fuelFromPreviousCity = fuel[idx - 1]
        milesRemaining += fuelFromPreviousCity * mpg - previousCityDistance

        if milesRemaining < milesRemainingAtValidStartingCity:
            milesRemainingAtValidStartingCity = milesRemaining
            indexOfValidStartingCity = idx

    return indexOfValidStartingCity
