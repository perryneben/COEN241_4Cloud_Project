from heapq import heappush, heappop # used for priority queue
pq = []

from locationInitializer import *
from locationNode import *

# this function checks if a node is in the map
def isNodeOnMap(name):
    # Check the start and end points to see if they are valid
    if name not in locationNames:
        print('Point: \'' + name + '\' is not valid')
        print('Valid points are: ')
        for i in range(len(locationNames)):
            print(locationNames[i], ' ', end = '')
        print()
        return False
    
    return True

# this function finds the desired node based on its name
def findNodeByName(name):
    for i in range(len(city_map)):
        if name == city_map[i].name:
            return city_map[i]

# this function reset all of the variables used in the graph
def resetNodes():
    pq = []
    for x in city_map:
        x.previousNode = None
        x.totalDistance = float('Inf')
        x.totalTime = float('Inf')
        x.visited = False

# this function selects distance for use with dijkstra
def useDijkstraDistance():
    for x in city_map:
        x.usingDistance = True
        x.usingTime = False

# this function selects time for use with dijkstra
def useDijkstraTime():
    for x in city_map:
        x.usingTime = True
        x.usingDistance = False

# determine the shortest path to all of the nodes recursively based on distance
def dijkstra_distance(node):
    # visit all of the node's neighbors and update them if needed
    for i in range(len(node.neighbors)):
        n = node.neighbors[i]
        d = node.distances[i]
        if n.totalDistance > (d + node.totalDistance):
            n.previousNode = node
            n.totalDistance = d + node.totalDistance
            heappush(pq, (n.totalDistance, n))
                
    node.visited = True
    
    (d, ne) = heappop(pq)
    while pq:
        dijkstra_distance(ne)

# determine the shortest path to all of the nodes recursively based on time
def dijkstra_time(node):
    # visit all of the node's neighbors and update them if needed
    for i in range(len(node.neighbors)):
        n = node.neighbors[i]
        t = node.times[i]
        if n.totalTime > (t + node.totalTime):
            n.previousNode = node
            n.totalTime = t + node.totalTime
            heappush(pq, (n.totalTime, n))
                
    node.visited = True
    (t, ne) = heappop(pq)
    while pq:
        dijkstra_time(ne)

# get the shortest route to the given node
def route(endNode):
    node = endNode
    labels = [endNode.name]
    while node.name != node.previousNode.name:
        node = node.previousNode
        labels.append(node.name)
    labels.reverse()
    return labels

# this function allows a user to change a node parameters
def changeNodeParameters():
    answer = input('Would you like to change any conditions for the points in the city?[Y/N]: ')
    if 'N' == answer or 'n' == answer:
        return
    
    print('Nodes in the city: ')
    for x in city_map:
        print(x.name, ' ', end = '')
    print()
    
    continueNodeChanges = True
    while continueNodeChanges:
        # have the user select a valid node to change its parameters
        validNodeSelection = False
        while not validNodeSelection:
            nodeChangeName = input('Please select a node that you would like to adjust: ')
            # check if the node selection is valid
            if isNodeOnMap(nodeChangeName):
                validNodeSelection = True
        
        # get the node itself
        nodeChange = findNodeByName(nodeChangeName)
        nodeChange.printNodeAttributes()
        
        # get the number selection from the user
        validNumberSelection = False
        while not validNumberSelection:
            numberChange = input('Please input the desired number of the attribute you wish to change: [q to quit] ')
            # speed limit
            if numberChange == '1':
                newSpeedLimit = input('Please enter the new speed limit: ')
                nodeChange.speedLimit = int(newSpeedLimit)
                
                # recalculate travel times for all nodes
                recalculateTravelTimes()
                
                validNumberSelection = True
            # weather
            elif numberChange == '2':
                newWeather = input('Please enter the new weather conditions: ')
                
                validNumberSelection = True
            # traffic
            elif numberChange == '3':
                newTraffic = input('Please enter the new traffic conditions: ')
                
                validNumberSelection = True
            # time of day
            elif numberChange == '4':
                newTimeOfDay = input('Please enter the new time of day: ')
                
                validNumberSelection = True
            # day of week
            elif numberChange == '5':
                newDayOfWeek = input('Please enter the new day of the week: ')
                
                validNumberSelection = True
            # holiday
            elif numberChange == '6':
                newHoliday = input('Please enter if it is a holiday: ')
                
                validNumberSelection = True
            # closure
            elif numberChange == '7':
                newClosure = input('Please enter the new closure status of the node: ')
                
                validNumberSelection = True
            # check if the user wants to quit
            elif numberChange == 'q':
                return
            # otherwise user input an invalid number
            else:
                print('Invalid selection.  Please try again')
        
        changeAnother = input('Would you like to change another node?[Y/N]: ')
        if changeAnother == 'N' or changeAnother == 'n':
            continueNodeChanges = False

# this function calculates the travel time between all of the nodes
def recalculateTravelTimes():
    # iterate through all of the nodes in the city map
    for x in city_map:
        # clear all of the times stored for travel from this node
        # to its neighbors
        x.times = []
        # iterate through all of the node's neighbors
        for y in x.distances:
            x.times.append(x.calcTravelTime(y))


