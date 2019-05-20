# This file will contain all of the initialization information for each of the location nodes of the simulator

from locationNode import *

# name, speedLimit, northNeighbor, distanceNorth, southNeighbor, distanceSouth, eastNeighbor, distanceEast, westNeighbor, distanceWest
a1 = locationNode('a1', 35, 'null', 'null', 'a2', 1, 'b1', 7, 'null', 'null')
a2 = locationNode('a2', 25, 'a1', 1, 'a3', 3, 'b2', 6, 'null', 'null')
a3 = locationNode('a3', 15, 'a2', 3, 'a4', 12, 'b3', 8, 'null', 'null')
a4 = locationNode('a4', 45, 'a3', 12, 'null', 'null', 'b4', 15, 'null', 'null')