from heapq import heappush, heappop # for priority queue
pq = []

class node:
    label = ''
    # adjacency list of the node 
    neighbors = [] # list of nodes
    distances = [] # distances to neighbors
    # for Dijkstra
    prevNode = None
    totalDistance = float('Inf')
    visited = False
    # constructor
    def __init__(self, label):
        self.label = label
        self.neighbors = []
        self.distances = []
        self.prevNode = None
        self.totalDistance = float('Inf')
        self.visited = False

    def __lt__(self, other):
        return self.totalDistance < other.totalDistance

# find the shortest paths to all nodes recursively
def dijkstra(node):
    # visit all neighbors and update them if necessary
    for i in range(len(node.neighbors)):
        n = node.neighbors[i]
        d = node.distances[i]
        if n.totalDistance > d + node.totalDistance:
            n.prevNode = node
            n.totalDistance = d + node.totalDistance
            heappush(pq, (n.totalDistance, n))
    node.visited = True
    
    
    (d, ne) = heappop(pq)
    if not ne.visited:
        dijkstra(ne)

# get the shortest path to the given node
def route(endNode):
    node = endNode
    labels = [endNode.label]
    # distances = []
    while node.label != node.prevNode.label:
        # distances.append(node.totalDistance - node.prevNode.totalDistance)
        node = node.prevNode
        labels.append(node.label)
    labels.reverse()
    return labels
    # distances.reverse()
    # return (labels, distances)
        
# create a graph
a = node('a')
b = node('b')
c = node('c')
d = node('d')
e = node('e')
f = node('f')
graph = (a, b, c, d, e, f)


a.neighbors.append(b)
a.distances.append(1)
a.neighbors.append(d)
a.distances.append(1)

b.neighbors.append(a)
b.distances.append(1)
b.neighbors.append(c)
b.distances.append(3)
b.neighbors.append(d)
b.distances.append(2)

c.neighbors.append(b)
c.distances.append(3)
c.neighbors.append(e)
c.distances.append(1)
c.neighbors.append(f)
c.distances.append(1)

d.neighbors.append(a)
d.distances.append(1)
d.neighbors.append(b)
d.distances.append(2)
d.neighbors.append(e)
d.distances.append(1)

e.neighbors.append(c)
e.distances.append(1)
e.neighbors.append(d)
e.distances.append(1)
e.neighbors.append(f)
e.distances.append(3)



f.neighbors.append(c)
f.distances.append(1)
f.neighbors.append(e)
f.distances.append(3)

# print the graph
#print('The graph:')
#print()
#for n in graph:
#    print('Node: ', n.label)
#    print('Neighbors:')
#    for i in range(len(n.neighbors)):
#        print(n.neighbors[i].label, n.distances[i])
#    print()

# find the shortest paths to all neighbors starting w/ the given node
startNode = a
print('Route start node:', startNode.label)
startNode.prevNode = startNode
startNode.totalDistance = 0
dijkstra(startNode)


# print the shortest path to the given node
endNode = f
print('Route end node:', endNode.label)
print('Route:', route(endNode))
print('Total distance:', endNode.totalDistance)
