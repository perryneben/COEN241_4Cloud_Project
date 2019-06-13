import sys
sys.path.append('..')
from locationNode import *
from locationInitializer import *
from helperFunctions import *

for x in city_map:
    x.setTimeOfDay(1000)
    x.setDayOfWeek(1)


print('predict values for a1:')
a1.predictTravelTime()

print('original travel values')
for i in range(len(a1.neighbors)):
    print(a1.times[i])