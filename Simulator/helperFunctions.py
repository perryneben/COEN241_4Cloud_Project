from heapq import heappush, heappop # used for priority queue
pq = []

from locationInitializer import *
from locationNode import *

# this function finds the desired node based on its name
def findNodeByName(name):
    for i in range(len(city_map)):
        if name == city_map[i].name:
            return city_map[i]


# this function reset all of the variables used in the graph
def resetNodes():
    for x in graph:
        x.visited = False
        x.totalDistance = float('Inf')
        x.totalTime = float('Inf')

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
    if not ne.visited:
        dijkstra_distance(ne)

# determine the shortest path to all of the nodes recursively based on time
def dijkstra_time(node):
    # visit all of the node's neighbors and update if needed
    for i in range(len(node.neighbors)):
        n = node.neighbor[i]
        t = node.times[i]
        if n.totalTime > (t + node.totalTime):
            n.previousNode = node
            n.totalTime = t + node.totalTime
            heappush(pq, (n.totalTime, n))
    node.visited = True
    
    (t, ne) = heappop(pq)
    if not ne.visited:
        dijkstra_time(ne)


# get the shortest route to the given node
def route(endNode):
    node = endNode
    labels = [endNode.name]
    # distances = []
    while node.name != node.previousNode.name:
        # distances.append(node.totalDistance - node.prevNode.totalDistance)
        node = node.previousNode
        labels.append(node.name)
    labels.reverse()
    return labels

















