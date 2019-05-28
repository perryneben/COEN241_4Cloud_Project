import sys
from locationNode import *
from locationInitializer import *
from helperFunctions import *

# Get the start and end points
start_point = input('Please enter the start point: ')
end_point = input('Please enter the end point: ')

# Check the start and end points to see if they are valid
if start_point not in locationNames:
    print('Start point: \'' + start_point + '\' is not valid')
    sys.exit()
if end_point not in locationNames:
    print('End point: \'' + end_point + '\' is not valid')
    sys.exit()

# Let user know the entered start and end points
print('Your start point is: ' + start_point)
print('Your end point is: ' + end_point)





