import sys
from locationNode import *
from locationInitializer import *
from helperFunctions import *


'''
for x in city_map:
    print('Node name is: ', x.getName())
    print('It has the following neighbors, distance, and time')
    for i in range(len(x.neighbors)):
        if x.neighbors[i]:
            print(x.neighbors[i].name, x.distances[i], x.times[i])
        else:
            print('None', x.distances[i], x.times[i])
'''

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

# get the corresponding nodes by name
startNode = findNodeByName(start_point)
endNode = findNodeByName(end_point)

# try dijkstra
startNode.previousNode = startNode
startNode.totalDistance = 0
dijkstra_distance(startNode)


print('Your end point is: ' + end_point)

# try and get the shortest path
print('Route start node: ', startNode.name)
print('Route end node: ', endNode.name)
print('Route: ', route(endNode))
print('Total distance: ', endNode.totalDistance)

'''
for i in range(len(city_map)):
    #print(city_map[i].name, 'total distance: ', city_map[i].totalDistance,
     #       'previousNode: ', city_map[i].previousNode.name)
'''





















