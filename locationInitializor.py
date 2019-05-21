# This file will contain all of the initialization information for each of the location nodes of the simulator

from locationNode import *

# name, speedLimit, northNeighbor, distanceNorth, southNeighbor, distanceSouth, eastNeighbor, distanceEast, westNeighbor, distanceWest
a1 = locationNode('a1', 35, 'null', 'null', 'a2', 1, 'b1', 7, 'null', 'null')
a2 = locationNode('a2', 25, 'a1', 1, 'a3', 3, 'b2', 6, 'null', 'null')
a3 = locationNode('a3', 15, 'a2', 3, 'a4', 12, 'b3', 8, 'null', 'null')
a4 = locationNode('a4', 45, 'a3', 12, 'null', 'null', 'b4', 15, 'null', 'null')

# create the intermediate nodes
b1 = locationNode('b1', 15, 'null', 'null', 'b2', 12, 'c1', 6, 'a1', 7)
b2 = locationNode('b2', 35, 'b1', 12, 'b3', 14, 'c2', 31, 'a2', 6)
b3 = locationNode('b3', 25, 'b2', 14, 'b4', 7, 'c3', 23, 'a3', 8)
b4 = locationNode('b4', 25, 'b3', 7, 'null', 'null', 'c4', 17, 'a4', 15)

c1 = locationNode('c1', 25, 'null', 'null', 'c2', 22, 'd1', 9, 'b1', 6)
c2 = locationNode('c2', 25, 'c1', 22, 'c3', 32, 'd2', 9, 'b2', 31)
c3 = locationNode('c3', 35, 'c2', 32, 'c4', 45, 'd3', 9, 'b3', 23)
c4 = locationNode('c4', 45, 'c3', 19, 'null', 'null', 'd4', 9, 'b4', 17)


# create the end four nodes
d1 = locationNode('d1', 35, 'null', 'null', 'd2', 9, 'null', 'null', 'c1', 9)
d2 = locationNode('d2', 25, 'd1', 15, 'd3', 5, 'null', 'null', 'c2', 9)
d3 = locationNode('d3', 15, 'd2', 9, 'd4', 11, 'null', 'null', 'c3', 9)
d4 = locationNode('d4', 45, 'd3', 8, 'null', 'null', 'null', 'null', 'c4', 9)
