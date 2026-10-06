import random
import time

def getrandomtime (startdate , enddate):
    randomgenerator = random.random()
    dateformat = '%m/%d/%Y'

    starttime = time.mktime (time.strptime(startdate , dateformat ))
    enddatetime = time.mktime (time.strptime(enddate , dateformat ))
    RandomTime = starttime + randomgenerator * (enddatetime - starttime)
    RandomDate = time.strftime(dateformat , time.localtime(RandomTime))
    return RandomDate
print (getrandomtime("1/2/2020" , "2/4/2025"))
