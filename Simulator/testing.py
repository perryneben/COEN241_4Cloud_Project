import sys
from locationNode import *
from locationInitializer import *
from helperFunctions import *


start_point = input('Please enter the start point: ')
end_point = input('Please enter the end point: ')

# Check the start and end points to see if they are valid
if start_point not in locationNames or end_point not in locationNames:
    print('Point: \'' + start_point + '\' is not valid')
    print('Valid points are: ')
    for i in range(len(locationNames)):
        print(locationNames[i])
    sys.exit()


# Let user know the entered start and end points
print('Your start point is: ' + start_point)
print('Your end point is: ' + end_point)

# get the corresponding nodes by name
startNode = findNodeByName(start_point)
endNode = findNodeByName(end_point)


# try dijkstra
useDijkstraDistance()
startNode.previousNode = startNode
startNode.totalDistance = 0
dijkstra_distance(startNode)


# try and get the shortest path
print('Route: ', route(endNode))
print('Total distance: ', endNode.totalDistance)




# reset the nodes
resetNodes()
useDijkstraTime()
startNode.previousNode = startNode
startNode.totalTime = 0
dijkstra_time(startNode)


# Let user know the entered start and end points
print('Your start point is: ' + start_point)
print('Your end point is: ' + end_point)

# try and get the shortest path
print('Route: ', route(endNode))
print('Total time: ', endNode.totalTime)

















