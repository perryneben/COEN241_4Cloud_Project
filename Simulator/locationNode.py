# Node class for the map

class locationNode:
    name = ''
    
    # for use with Dijkstra Algorithm
    previousNode = None
    totalDistance = float('Inf')
    totalTime = float('Inf')
    visited = False
    
    # initializer
    def __init__(self, name, speedLimit):
        self.name = name
        self.speedLimit = speedLimit
        
        
        self.neighbors = [] # list of neighbor nodes
        self.distances = [] # list of distances to neighbors
        self.times = [] # list of times to reach desired neighbors
        
        self.previousNode = None
        self.totalDistance = float('Inf')
        self.totalTime = float('Inf')
        self.visited = False
    
    def setNeighbor(self, neighbor, dist):
        self.neighbors.append(neighbor)
        self.distances.append(dist)
        
        if neighbor:
            self.times.append(self.calcTravelTime(dist, self.speedLimit))
        else:
            self.times.append('Inf')
    
    # overloaded operator for use with priority queue
    def __lt__(self, other):
        return self.totalDistance < other.totalDistance
    
    # this function sets the speed limit at the node
    def setSpeedLimit(self, speedLimit):
        self.speedLimit = speedLimit
    
    # this function sets the weather conditions at the node
    def setWeather(self, weather):
        self.weather = weather
    
    # this function sets the traffic conditions at the node
    def setTraffic(self, traffic):
        self.traffic = traffic
    
    # this function sets the time of day it is at the node
    def setTimeOfDay(self, timeOfDay):
        self.timeOfDay = timeOfDay
    
    # this function sets the day of the week it is
    def setDayOfWeek(self, dayOfWeek):
        self.dayOfWeek = dayOfWeek
    
    # this function sets if it is a holiday
    def setHoliday(self, holiday):
        self.holiday = holiday
    
    # this function sets if a node has been closed
    def setNodeClosure(self, closure):
        self.closure = closure
    
    # this function gets the name of the node
    def getName(self):
        return self.name
    
    # this function will calculate the time it takes to get from one node to another
    def calcTravelTime(self, distance, speed):
        # time = distance/speed
        # time is set in minutes
        # speed is mph
        # distance is miles
        time = float(distance) / float(speed)
        return round(float(time * 60), 2)
    
    # this function gets the northern neighbor
    def getNorthNeighbor(self):
        return self.neighbors[0]
    
    def getNorthDistance(self):
        return self.distances[0]
    
    def getNorthTime(self):
        return self.times[0]
    
    # this function gets the southern neighbor
    def getSouthNeighbor(self):
        return self.neighbors[1]
    
    def getSouthDistance(self):
        return self.distances[1]
    
    def getSouthTime(self):
        return self.times[1]
    
    # this function gets the eastern neighbor
    def getEastNeighbor(self):
        return self.neighbors[2]
    
    def getEastDistance(self):
        return self.distances[2]
    
    def getEastTime(self):
        return self.times[2]
    
    # this function gets the western neighbor
    def getWestNeighbor(self):
        return self.neighbors[3]
    
    def getWestDistance(self):
        return self.distances[3]
    
    def getWestTime(self):
        return self.times[3]
    
    # this function will get the speed limit at the node
    def getSpeedLimit(self):
        return self.speedLimit
    
    # this function gets the weather at the node
    def getWeather(self):
        return self.weather
    
    # this function gets the traffic at the node
    def getTraffic(self):
        return self.traffic
    

    
    
    
    
