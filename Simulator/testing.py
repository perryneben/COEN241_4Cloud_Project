import sys
from locationNode import *
from locationInitializer import *
from helperFunctions import *

start_point = input('Please enter the start point: ')
end_point = input('Please enter the end point: ')

# check the start and end points entered
if not isNodeOnMap(start_point) or not isNodeOnMap(end_point):
    sys.exit()

# Let user know the entered start and end points
print('Your start point is: ' + start_point)
print('Your end point is: ' + end_point)

# get the corresponding nodes by name
startNode = findNodeByName(start_point)
endNode = findNodeByName(end_point)


#changeNodeParameters()

traveledRoute = []

# add node the the route being traveled
traveledRoute.append((startNode.name, 0))


while startNode != endNode:
    # reset the nodes to enable the user to alter the parameters of the node
    resetNodes()
    useDijkstraTime()
    startNode.previousNode = startNode
    startNode.totalTime = 0
    
    dijkstra_time(startNode)

    currentRoute = route(endNode)

    # try and get the shortest path
    print('\nCurrent Planned Route: ', currentRoute)
    print('Current Planned travel time: ', round(endNode.totalTime, 2))

    if currentRoute:
        # set the next node as the new start to simulate having traveled there
        startNode = findNodeByName(currentRoute[1])
        # add node the the route being traveled
        traveledRoute.append((startNode.name, startNode.totalTime))
        # ask user if they want to change any node parameters
        changeNodeParameters()


finalRoute = []
finalTime = 0
for x in traveledRoute:
    finalRoute.append(x[0])
    finalTime += x[1]

print('Final Route: ', finalRoute)
print('Total time traveled: ', round(finalTime, 2))







