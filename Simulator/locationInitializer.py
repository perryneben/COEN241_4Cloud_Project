# This file will contain all of the initialization information for each of the location nodes of the simulator
from locationNode import *

locationNames = ('a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4',
             'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4')

a1 = locationNode('a1', 35)
a2 = locationNode('a2', 25)
a3 = locationNode('a3', 15)
a4 = locationNode('a4', 45)

b1 = locationNode('b1', 15)
b2 = locationNode('b2', 35)
b3 = locationNode('b3', 25)
b4 = locationNode('b4', 25)

c1 = locationNode('c1', 25)
c2 = locationNode('c2', 55)
c3 = locationNode('c3', 35)
c4 = locationNode('c4', 45)

d1 = locationNode('d1', 10)
d2 = locationNode('d2', 25)
d3 = locationNode('d3', 15)
d4 = locationNode('d4', 45)

city_map = (a1, a2, a3, a4, b1, b2, b3, b4,
            c1, c2, c3, c4, d1, d2, d3, d4)

# Set the neighbors for the A nodes
a1.setNeighbor(a2, 1)
a1.setNeighbor(b1, 7)

a2.setNeighbor(a1, 1)
a2.setNeighbor(a3, 3)
a2.setNeighbor(b2, 6)

a3.setNeighbor(a2, 3)
a3.setNeighbor(a4, 12)
a3.setNeighbor(b3, 8)

a4.setNeighbor(a3, 12)
a4.setNeighbor(b4, 15)

# Set the neighbors for the B nodes
b1.setNeighbor(b2, 12)
b1.setNeighbor(c1, 6)
b1.setNeighbor(a1, 7)

b2.setNeighbor(b1, 12)
b2.setNeighbor(b3, 14)
b2.setNeighbor(c2, 31)
b2.setNeighbor(a2, 6)

b3.setNeighbor(b2, 14)
b3.setNeighbor(b4, 7)
b3.setNeighbor(c3, 23)
b3.setNeighbor(a3, 8)

b4.setNeighbor(b3, 7)
b4.setNeighbor(c4, 17)
b4.setNeighbor(a4, 15)

# Set the neighbors for the C nodes
c1.setNeighbor(c2, 22)
c1.setNeighbor(d1, 9)
c1.setNeighbor(b1, 6)

c2.setNeighbor(c1, 22)
c2.setNeighbor(c3, 32)
c2.setNeighbor(d2, 9)
c2.setNeighbor(b2, 31)

c3.setNeighbor(c2, 32)
c3.setNeighbor(c4, 45)
c3.setNeighbor(d3, 9)
c3.setNeighbor(b3, 23)

c4.setNeighbor(c3, 19)
c4.setNeighbor(d4, 9)
c4.setNeighbor(b4, 17)

# Set the neighbors for the D nodes
d1.setNeighbor(d2, 9)
d1.setNeighbor(c1, 9)

d2.setNeighbor(d1, 15)
d2.setNeighbor(d3, 5)
d2.setNeighbor(c2, 9)

d3.setNeighbor(d2, 9)
d3.setNeighbor(d4, 11)
d3.setNeighbor(c3, 9)

d4.setNeighbor(d3, 8)
d4.setNeighbor(c4, 9)