import random 

import time

print("\n")

print("\n")

def getRandomDate(startDate, endDate ): #

    print("Printing random date between", startDate, " and ", endDate)

    print("\n")

    randomGenerator = random.random()

    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))

    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)

    randomDate = time.strftime(dateFormat, time.localtime(randomTime))

    return randomDate

print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))

print("\n")

print("\n")