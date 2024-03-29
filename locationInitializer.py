# This file will contain all of the initialization information for each of the location nodes of the simulator
from locationNode import *
import random

locationNames = ('a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                 'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                 'h0', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',
                 'i0', 'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8',
                 'j0', 'j1', 'j2', 'j3', 'j4', 'j5', 'j6', 'j7', 'j8',
                 'k0', 'k1', 'k2', 'k3', 'k4', 'k5', 'k6', 'k7', 'k8',
                 'l0', 'l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8')

# initialize A nodes
a0 = locationNode('a0', 35)
a1 = locationNode('a1', 25)
a2 = locationNode('a2', 25)
a3 = locationNode('a3', 35)
a4 = locationNode('a4', 35)
a5 = locationNode('a5', 15)
a6 = locationNode('a6', 15)
a7 = locationNode('a7', 45)
a8 = locationNode('a8', 45)

# initialize B nodes
b0 = locationNode('b0', 15)
b1 = locationNode('b1', 25)
b2 = locationNode('b2', 25)
b3 = locationNode('b3', 35)
b4 = locationNode('b4', 55)
b5 = locationNode('b5', 55)
b6 = locationNode('b6', 35)
b7 = locationNode('b7', 35)
b8 = locationNode('b8', 35)

# initialize C nodes
c0 = locationNode('c0', 35)
c1 = locationNode('c1', 25)
c2 = locationNode('c2', 25)
c3 = locationNode('c3', 35)
c4 = locationNode('c4', 35)
c5 = locationNode('c5', 55)
c6 = locationNode('c6', 65)
c7 = locationNode('c7', 25)
c8 = locationNode('c8', 40)

# initialize D nodes
d0 = locationNode('d0', 25)
d1 = locationNode('d1', 25)
d2 = locationNode('d2', 15)
d3 = locationNode('d3', 30)
d4 = locationNode('d4', 50)
d5 = locationNode('d5', 40)
d6 = locationNode('d6', 30)
d7 = locationNode('d7', 35)
d8 = locationNode('d8', 35)

# initialize E nodes
e0 = locationNode('e0', 35)
e1 = locationNode('e1', 25)
e2 = locationNode('e2', 5)
e3 = locationNode('e3', 35)
e4 = locationNode('e4', 35)
e5 = locationNode('e5', 35)
e6 = locationNode('e6', 25)
e7 = locationNode('e7', 65)
e8 = locationNode('e8', 45)

# initialize F nodes
f0 = locationNode('f0', 15)
f1 = locationNode('f1', 25)
f2 = locationNode('f2', 25)
f3 = locationNode('f3', 35)
f4 = locationNode('f4', 55)
f5 = locationNode('f5', 55)
f6 = locationNode('f6', 35)
f7 = locationNode('f7', 35)
f8 = locationNode('f8', 35)

# initialize G nodes
g0 = locationNode('g0', 35)
g1 = locationNode('g1', 25)
g2 = locationNode('g2', 25)
g3 = locationNode('g3', 35)
g4 = locationNode('g4', 35)
g5 = locationNode('g5', 55)
g6 = locationNode('g6', 65)
g7 = locationNode('g7', 25)
g8 = locationNode('g8', 40)

# initialize H nodes
h0 = locationNode('h0', 25)
h1 = locationNode('h1', 25)
h2 = locationNode('h2', 15)
h3 = locationNode('h3', 30)
h4 = locationNode('h4', 50)
h5 = locationNode('h5', 40)
h6 = locationNode('h6', 30)
h7 = locationNode('h7', 35)
h8 = locationNode('h8', 35)

# initialize I nodes
i0 = locationNode('i0', 45)
i1 = locationNode('i1', 35)
i2 = locationNode('i2', 15)
i3 = locationNode('i3', 35)
i4 = locationNode('i4', 65)
i5 = locationNode('i5', 65)
i6 = locationNode('i6', 5)
i7 = locationNode('i7', 65)
i8 = locationNode('i8', 25)

# initialize J nodes
j0 = locationNode('j0', 15)
j1 = locationNode('j1', 45)
j2 = locationNode('j2', 25)
j3 = locationNode('j3', 35)
j4 = locationNode('j4', 55)
j5 = locationNode('j5', 55)
j6 = locationNode('j6', 35)
j7 = locationNode('j7', 35)
j8 = locationNode('j8', 35)

# initialize K nodes
k0 = locationNode('k0', 35)
k1 = locationNode('k1', 25)
k2 = locationNode('k2', 25)
k3 = locationNode('k3', 35)
k4 = locationNode('k4', 35)
k5 = locationNode('k5', 55)
k6 = locationNode('k6', 65)
k7 = locationNode('k7', 25)
k8 = locationNode('k8', 40)

# initialize L nodes
l0 = locationNode('l0', 25)
l1 = locationNode('l1', 25)
l2 = locationNode('l2', 15)
l3 = locationNode('l3', 30)
l4 = locationNode('l4', 50)
l5 = locationNode('l5', 40)
l6 = locationNode('l6', 30)
l7 = locationNode('l7', 35)
l8 = locationNode('l8', 35)

city_map = (a0, a1, a2, a3, a4, a5, a6, a7, a8,
            b0, b1, b2, b3, b4, b5, b6, b7, b8,
            c0, c1, c2, c3, c4, c5, c6, c7, c8,
            d0, d1, d2, d3, d4, d5, d6, d7, d8,
            e0, e1, e2, e3, e4, e5, e6, e7, e8,
            f0, f1, f2, f3, f4, f5, f6, f7, f8,
            g0, g1, g2, g3, g4, g5, g6, g7, g8,
            h0, h1, h2, h3, h4, h5, h6, h7, h8,
            i0, i1, i2, i3, i4, i5, i6, i7, i8,
            j0, j1, j2, j3, j4, j5, j6, j7, j8,
            k0, k1, k2, k3, k4, k5, k6, k7, k8,
            l0, l1, l2, l3, l4, l5, l6, l7, l8)

# Set the neighbors for the A nodes
a0.setNeighbor(b0, 0.5)
a0.setNeighbor(a1, 0.7)

a1.setNeighbor(a0, 0.7)
a1.setNeighbor(b1, 0.9)
a1.setNeighbor(a2, 0.3)

a2.setNeighbor(a1, 0.3)
a2.setNeighbor(b2, 0.4)
a2.setNeighbor(a3, 0.2)

a3.setNeighbor(a2, 0.2)
a3.setNeighbor(a4, 0.5)
a3.setNeighbor(b3, 0.7)

a4.setNeighbor(a3, 0.5)
a4.setNeighbor(b4, 0.5)
a4.setNeighbor(a5, 0.5)

a5.setNeighbor(a4, 0.5)
a5.setNeighbor(b5, 0.15)
a5.setNeighbor(a6, 0.8)

a6.setNeighbor(a5, 0.8)
a6.setNeighbor(b6, 0.6)
a6.setNeighbor(a7, 0.6)

a7.setNeighbor(a6, 0.6)
a7.setNeighbor(b7, 0.9)
a7.setNeighbor(a8, 0.11)

a8.setNeighbor(a7, 0.11)
a8.setNeighbor(b8, 0.1)

# Set the neighbors for the B nodes
b0.setNeighbor(a0, 0.5)
b0.setNeighbor(c0, 0.15)
b0.setNeighbor(b1, 0.1)

b1.setNeighbor(b0, 0.1)
b1.setNeighbor(a1, 0.9)
b1.setNeighbor(b2, 0.4)
b1.setNeighbor(c1, 0.9)

b2.setNeighbor(b1, 0.4)
b2.setNeighbor(a2, 0.4)
b2.setNeighbor(c2, 0.4)
b2.setNeighbor(b3, 0.8)

b3.setNeighbor(b2, 0.8)
b3.setNeighbor(a3, 0.7)
b3.setNeighbor(b4, 0.3)
b3.setNeighbor(c3, 0.7)

b4.setNeighbor(b3, 0.3)
b4.setNeighbor(a4, 0.5)
b4.setNeighbor(b5, 0.2)
b4.setNeighbor(c4, 0.3)

b5.setNeighbor(b4, 0.2)
b5.setNeighbor(a5, 0.15)
b5.setNeighbor(b6, 0.8)
b5.setNeighbor(c5, 0.3)

b6.setNeighbor(b5, 0.8)
b6.setNeighbor(a6, 0.6)
b6.setNeighbor(c6, 0.6)
b6.setNeighbor(b7, 0.6)

b7.setNeighbor(b6, 0.6)
b7.setNeighbor(a7, 0.9)
b7.setNeighbor(c7, 0.12)
b7.setNeighbor(b8, 0.1)

b8.setNeighbor(a8, 0.1)
b8.setNeighbor(b7, 0.1)
b8.setNeighbor(c8, 0.11)

# Set the neighbors for the C nodes
c0.setNeighbor(b0, 0.15)
c0.setNeighbor(d0, 0.4)
c0.setNeighbor(c1, 0.5)

c1.setNeighbor(c0, 0.5)
c1.setNeighbor(b1, 0.9)
c1.setNeighbor(c2, 0.3)
c1.setNeighbor(d1, 0.13)

c2.setNeighbor(c1, 0.3)
c2.setNeighbor(b2, 0.4)
c2.setNeighbor(d2, 0.8)
c2.setNeighbor(c3, 0.9)

c3.setNeighbor(c2, 0.9)
c3.setNeighbor(b3, 0.7)
c3.setNeighbor(d3, 0.8)
c3.setNeighbor(c4, 0.2)

c4.setNeighbor(c3, 0.2)
c4.setNeighbor(b4, 0.3)
c4.setNeighbor(c5, 0.5)
c4.setNeighbor(d4, 0.5)

c5.setNeighbor(c4, 0.5)
c5.setNeighbor(b5, 0.3)
c5.setNeighbor(d5, 0.5)
c5.setNeighbor(c6, 0.11)

c6.setNeighbor(c5, 0.11)
c6.setNeighbor(b6, 0.6)
c6.setNeighbor(d6, 0.2)
c6.setNeighbor(c7, 0.9)

c7.setNeighbor(c6, 0.9)
c7.setNeighbor(b7, 0.12)
c7.setNeighbor(d7, 0.7)
c7.setNeighbor(c8, 0.4)

c8.setNeighbor(c7, 0.4)
c8.setNeighbor(b8, 0.11)
c8.setNeighbor(d8, 0.9)

# Set the neighbors for the D nodes
d0.setNeighbor(c0, 0.4)
d0.setNeighbor(e0, 0.4)
d0.setNeighbor(d1, 0.7)

d1.setNeighbor(d1, 0.7)
d1.setNeighbor(c1, 0.13)
d1.setNeighbor(e1, 0.3)
d1.setNeighbor(d2, 0.2)

d2.setNeighbor(d1, 0.2)
d2.setNeighbor(c2, 0.8)
d2.setNeighbor(e2, 0.4)
d2.setNeighbor(d3, 0.7)

d3.setNeighbor(d2, 0.7)
d3.setNeighbor(c3, 0.8)
d3.setNeighbor(e3, 0.1)
d3.setNeighbor(d4, 0.1)

d4.setNeighbor(d3, 0.1)
d4.setNeighbor(c4, 0.5)
d4.setNeighbor(e4, 0.4)
d4.setNeighbor(d5, 0.8)

d5.setNeighbor(d4, 0.8)
d5.setNeighbor(c5, 0.5)
d5.setNeighbor(e5, 0.8)
d5.setNeighbor(d6, 0.4)

d6.setNeighbor(d5, 0.4)
d6.setNeighbor(e6, 0.11)
d6.setNeighbor(c6, 0.2)
d6.setNeighbor(d7, 0.3)

d7.setNeighbor(d6, 0.3)
d7.setNeighbor(c7, 0.7)
d7.setNeighbor(e7, 0.14)
d7.setNeighbor(d8, 0.1)

d8.setNeighbor(d7, 0.1)
d8.setNeighbor(c8, 0.9)
d8.setNeighbor(e8, 0.11)

# Set the neighbors for the E nodes
e0.setNeighbor(d0, 0.4)
e0.setNeighbor(f0, 0.6)
e0.setNeighbor(e1, 0.7)

e1.setNeighbor(e0, 0.7)
e1.setNeighbor(d1, 0.3)
e1.setNeighbor(f1, 0.1)
e1.setNeighbor(e2, 0.1)

e2.setNeighbor(e1, 0.1)
e2.setNeighbor(d2, 0.4)
e2.setNeighbor(f2, 0.1)
e2.setNeighbor(e3, 0.3)

e3.setNeighbor(e2, 0.3)
e3.setNeighbor(d3, 0.1)
e3.setNeighbor(f3, 0.8)
e3.setNeighbor(e4, 0.2)

e4.setNeighbor(e3, 0.2)
e4.setNeighbor(d4, 0.4)
e4.setNeighbor(e5, 0.8)
e4.setNeighbor(f4, 0.7)

e5.setNeighbor(e4, 0.8)
e5.setNeighbor(d5, 0.8)
e5.setNeighbor(f5, 0.1)
e5.setNeighbor(e6, 0.4)

e6.setNeighbor(e5, 0.4)
e6.setNeighbor(d6, 0.11)
e6.setNeighbor(f6, 0.1)
e6.setNeighbor(e7, 0.8)

e7.setNeighbor(e6, 0.8)
e7.setNeighbor(d7, 0.14)
e7.setNeighbor(f7, 0.2)
e7.setNeighbor(e8, 0.4)

e8.setNeighbor(e7, 0.4)
e8.setNeighbor(d8, 0.11)
e8.setNeighbor(f8, 0.1)

# Set the neighbors for the F nodes
f0.setNeighbor(e0, 0.6)
f0.setNeighbor(g0, 0.2)
f0.setNeighbor(f1, 0.2)

f1.setNeighbor(g0, 0.2)
f1.setNeighbor(e1, 0.1)
f1.setNeighbor(g1, 0.6)
f1.setNeighbor(f2, 0.6)

f2.setNeighbor(f1, 0.6)
f2.setNeighbor(e2, 0.1)
f2.setNeighbor(f3, 0.6)
f2.setNeighbor(g2, 0.7)

f3.setNeighbor(f2, 0.6)
f3.setNeighbor(e3, 0.8)
f3.setNeighbor(g3, 0.7)
f3.setNeighbor(f4, 0.2)

f4.setNeighbor(f3, 0.2)
f4.setNeighbor(g4, 0.1)
f4.setNeighbor(e4, 0.7)
f4.setNeighbor(f5, 0.3)

f5.setNeighbor(f4, 0.3)
f5.setNeighbor(e5, 0.1)
f5.setNeighbor(g5, 0.3)
f5.setNeighbor(f6, 0.12)

f6.setNeighbor(f5, 0.12)
f6.setNeighbor(g6, 0.1)
f6.setNeighbor(e6, 0.8)
f6.setNeighbor(f7, 0.2)

f7.setNeighbor(f6, 0.2)
f7.setNeighbor(e7, 0.2)
f7.setNeighbor(g7, 0.9)
f7.setNeighbor(f8, 0.8)

f8.setNeighbor(f7, 0.8)
f8.setNeighbor(e8, 0.1)
f8.setNeighbor(g8, 0.2)

# Set the neighbors for the G nodes
g0.setNeighbor(f0, 0.2)
g0.setNeighbor(h0, 0.7)
g0.setNeighbor(g1, 0.9)

g1.setNeighbor(g0, 0.9)
g1.setNeighbor(f1, 0.6)
g1.setNeighbor(h1, 0.2)
g1.setNeighbor(g2, 0.1)

g2.setNeighbor(g1, 0.1)
g2.setNeighbor(f2, 0.7)
g2.setNeighbor(h2, 0.8)
g2.setNeighbor(g3, 0.12)

g3.setNeighbor(g2, 0.12)
g3.setNeighbor(f3, 0.4)
g3.setNeighbor(h3, 0.2)
g3.setNeighbor(g4, 0.15)

g4.setNeighbor(g3, 0.15)
g4.setNeighbor(f4, 0.1)
g4.setNeighbor(g5, 0.4)
g4.setNeighbor(h4, 0.5)

g5.setNeighbor(g5, 0.4)
g5.setNeighbor(f5, 0.3)
g5.setNeighbor(h5, 0.12)
g5.setNeighbor(g6, 0.15)

g6.setNeighbor(g5, 0.15)
g6.setNeighbor(f6, 0.1)
g6.setNeighbor(h6, 0.2)
g6.setNeighbor(g7, 0.14)

g7.setNeighbor(g6, 0.14)
g7.setNeighbor(f7, 0.9)
g7.setNeighbor(h7, 0.1)
g7.setNeighbor(g8, 0.4)

g8.setNeighbor(g7, 0.4)
g8.setNeighbor(f8, 0.2)
g8.setNeighbor(h8, 0.7)

# Set the neighbors for the H nodes
h0.setNeighbor(g0, 0.7)
h0.setNeighbor(i0, 0.2)
h0.setNeighbor(h1, 0.5)

h1.setNeighbor(h0, 0.5)
h1.setNeighbor(i1, 0.1)
h1.setNeighbor(g1, 0.2)
h1.setNeighbor(h2, 0.5)

h2.setNeighbor(h1, 0.5)
h2.setNeighbor(i2, 0.9)
h2.setNeighbor(g2, 0.8)
h2.setNeighbor(h3, 0.4)

h3.setNeighbor(h2, 0.4)
h3.setNeighbor(g3, 0.2)
h3.setNeighbor(i3, 0.1)
h3.setNeighbor(h4, 0.8)

h4.setNeighbor(h3, 0.8)
h4.setNeighbor(i4, 0.9)
h4.setNeighbor(g4, 0.5)
h4.setNeighbor(h5, 0.12)

h5.setNeighbor(h4, 0.12)
h5.setNeighbor(g5, 0.12)
h5.setNeighbor(i5, 0.2)
h5.setNeighbor(h6, 0.7)

h6.setNeighbor(h5, 0.7)
h6.setNeighbor(g6, 0.2)
h6.setNeighbor(i6, 0.1)
h6.setNeighbor(h7, 0.4)

h7.setNeighbor(h6, 0.4)
h7.setNeighbor(g7, 0.1)
h7.setNeighbor(i7, 0.7)
h7.setNeighbor(h8, 0.9)

h8.setNeighbor(h7, 0.9)
h8.setNeighbor(g8, 0.7)
h8.setNeighbor(i8, 0.1)

# Set the neighbors for the I nodes
i0.setNeighbor(h0, 0.2)
i0.setNeighbor(j0, 0.7)
i0.setNeighbor(i1, 0.9)

i1.setNeighbor(i0, 0.9)
i1.setNeighbor(h1, 0.1)
i1.setNeighbor(j1, 0.1)
i1.setNeighbor(i2, 0.2)

i2.setNeighbor(i1, 0.2)
i2.setNeighbor(h2, 0.9)
i2.setNeighbor(j2, 0.9)
i2.setNeighbor(i3, 0.7)

i3.setNeighbor(i2, 0.7)
i3.setNeighbor(h3, 0.1)
i3.setNeighbor(j3, 0.8)
i3.setNeighbor(i4, 0.4)

i4.setNeighbor(i3, 0.4)
i4.setNeighbor(j4, 0.1)
i4.setNeighbor(h4, 0.9)
i4.setNeighbor(i5, 0.6)

i5.setNeighbor(i4, 0.6)
i5.setNeighbor(h5, 0.2)
i5.setNeighbor(j5, 0.13)
i5.setNeighbor(i6, 0.4)

i6.setNeighbor(i5, 0.4)
i6.setNeighbor(h6, 0.1)
i6.setNeighbor(j6, 0.3)
i6.setNeighbor(i7, 0.7)

i7.setNeighbor(i6, 0.7)
i7.setNeighbor(h7, 0.7)
i7.setNeighbor(j7, 0.5)
i7.setNeighbor(i8, 0.4)

i8.setNeighbor(i7, 0.4)
i8.setNeighbor(h8, 0.1)
i8.setNeighbor(j8, 0.9)

# Set the neighbors for the J nodes
j0.setNeighbor(i0, 0.7)
j0.setNeighbor(k0, 0.8)
j0.setNeighbor(j1, 0.7)

j1.setNeighbor(j0, 0.7)
j1.setNeighbor(i1, 0.1)
j1.setNeighbor(k1, 0.14)
j1.setNeighbor(j2, 0.4)

j2.setNeighbor(j1, 0.4)
j2.setNeighbor(i2, 0.9)
j2.setNeighbor(k2, 0.11)
j2.setNeighbor(j3, 0.2)

j3.setNeighbor(j2, 0.2)
j3.setNeighbor(i3, 0.8)
j3.setNeighbor(k3, 0.4)
j3.setNeighbor(j4, 0.3)

j4.setNeighbor(j3, 0.3)
j4.setNeighbor(i4, 0.1)
j4.setNeighbor(k4, 0.9)
j4.setNeighbor(j5, 0.7)

j5.setNeighbor(j4, 0.7)
j5.setNeighbor(i5, 0.13)
j5.setNeighbor(k5, 0.8)
j5.setNeighbor(j6, 0.4)

j6.setNeighbor(j5, 0.5)
j6.setNeighbor(i6, 0.3)
j6.setNeighbor(k6, 0.18)
j6.setNeighbor(j7, 0.5)

j7.setNeighbor(j6, 0.5)
j7.setNeighbor(i7, 0.5)
j7.setNeighbor(k7, 0.7)
j7.setNeighbor(j8, 0.5)

j8.setNeighbor(j7, 0.5)
j8.setNeighbor(i8, 0.9)
j8.setNeighbor(k8, 0.8)

# Set the neighbors for the K nodes
k0.setNeighbor(j0, 0.8)
k0.setNeighbor(l0, 0.7)
k0.setNeighbor(k1, 0.7)

k1.setNeighbor(k0, 0.4)
k1.setNeighbor(j1, 0.14)
k1.setNeighbor(l1, 0.8)
k1.setNeighbor(k2, 0.5)

k2.setNeighbor(k1, 0.5)
k2.setNeighbor(j2, 0.11)
k2.setNeighbor(l2, 0.9)
k2.setNeighbor(k3, 0.1)

k3.setNeighbor(k2, 0.1)
k3.setNeighbor(j3, 0.4)
k3.setNeighbor(l3, 0.8)
k3.setNeighbor(k4, 0.11)

k4.setNeighbor(k3, 0.11)
k4.setNeighbor(j4, 0.9)
k4.setNeighbor(l4, 0.9)
k4.setNeighbor(k5, 0.7)

k5.setNeighbor(k4, 0.7)
k5.setNeighbor(j5, 0.8)
k5.setNeighbor(l5, 0.11)
k5.setNeighbor(k6, 0.16)

k6.setNeighbor(k5, 0.16)
k6.setNeighbor(j6, 0.18)
k6.setNeighbor(l6, 0.8)
k6.setNeighbor(k7, 0.6)

k7.setNeighbor(k6, 0.6)
k7.setNeighbor(j7, 0.7)
k7.setNeighbor(l7, 0.9)
k7.setNeighbor(k8, 0.4)

k8.setNeighbor(k7, 0.4)
k8.setNeighbor(j8, 0.8)
k8.setNeighbor(l8, 0.7)

# Set the neighbors for the L nodes
l0.setNeighbor(k0, 0.7)
l0.setNeighbor(l1, 0.9)

l1.setNeighbor(l0, 0.9)
l1.setNeighbor(k1, 0.8)
l1.setNeighbor(l2, 0.6)

l2.setNeighbor(l1, 0.6)
l2.setNeighbor(k2, 0.9)
l2.setNeighbor(l3, 0.7)

l3.setNeighbor(l2, 0.7)
l3.setNeighbor(k3, 0.8)
l3.setNeighbor(l4, 0.4)

l4.setNeighbor(l3, 0.4)
l4.setNeighbor(k4, 0.9)
l4.setNeighbor(l5, 0.3)

l5.setNeighbor(l4, 0.3)
l5.setNeighbor(k5, 0.11)
l5.setNeighbor(l6, 0.5)

l6.setNeighbor(l5, 0.5)
l6.setNeighbor(k6, 0.8)
l6.setNeighbor(l7, 0.5)

l7.setNeighbor(l6, 0.5)
l7.setNeighbor(k7, 0.9)
l7.setNeighbor(l8, 0.14)

l8.setNeighbor(l7, 0.14)
l8.setNeighbor(k8, 0.7)

# randomly assign traffic and weather variables to each node between 0-5
for x in city_map:
    t = random.randint(0, 5)
    w = random.randint(0, 5)
    x.setTraffic(t)
    x.setWeather(w)

# call function to predict all of the travel times
for x in city_map:
    x.predictTravelTime()