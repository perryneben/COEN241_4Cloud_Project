# Node class for the map
import datetime
class locationNode:
    # initializer
    def __init__(self, name, speedLimit):
        self.name = name
        # speed limit is MPH
        self.speedLimit = speedLimit
        self.weather = ''
        self.traffic = ''
        self.timeOfDay = datetime.datetime.now()
        self.dayOfWeek = str(datetime.datetime.today().weekday())
        self.holiday = False
        self.closure = False
        self.usingTime = False
        self.usingDistance = False
        
        # this is just a list of the neighbor nodes
        self.neighbors = []
        # list of distance in feet to each neighbor
        self.distances = []
        # list of travel time in minutes to each neighbor
        self.times = []
        
        self.previousNode = None
        self.totalDistance = float('Inf')
        self.totalTime = float('Inf')
        self.distanceTime = float('Inf')
        self.visited = False
    
    def setNeighbor(self, neighbor, dist):
        self.neighbors.append(neighbor)
        self.distances.append(dist)
        self.times.append(self.calcTravelTime(dist))

    # overloaded operator for use with priority queue
    def __lt__(self, other):
        # check what is being used for comparison
        if self.usingTime:
            return self.totalTime < other.totalTime
        # default assumption is distance
        return self.totalDistance < other.totalDistance
    
    # this function sets the speed limit at the node
    def setSpeedLimit(self, speedLimit):
        # set the speed limit
        self.speedLimit = speedLimit
    
    # this function sets the weather conditions at the node
    def setWeather(self, weather):
        self.weather = weather
        if weather == '1':
            for x in self.times:
                x += 1
        elif weather == '2':
            for x in self.times:
                x += 2
        elif weather == '3':
            for x in self.times:
                x += 3
        elif weather == '4':
            for x in self.times:
                x += 4
        elif weather == '5':
            for x in self.times:
                x += 5
    
    # this function sets the traffic conditions at the node
    def setTraffic(self, traffic):
        self.traffic = traffic
        if traffic == '1':
            for x in self.times:
                x += 2
        elif traffic == '2':
            for x in self.times:
                x += 4
        elif traffic == '3':
            for x in self.times:
                x += 6
        elif traffic == '4':
            for x in self.times:
                x += 8
        elif traffic == '5':
            for x in self.times:
                x += 10

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
    
    # this function will calculate the time it takes to get from one node to another
    def calcTravelTime(self, distance):
        # time = distance/speed
        # time is set in minutes
        # speed is mph
        # distance is miles
        time = float(distance) / float(self.speedLimit)
        return round(float(time * 60), 2)
    
    def printNodeAttributes(self):
        print('Name: ', self.name)
        print('(1) Speed Limit: ', self.speedLimit)
        print('(2) Weather: ', self.weather)
        print('(3) Traffic: ', self.weather)
        print('(4) Time of Day: ', self.timeOfDay)
        print('(5) Day of Week: ', self.dayOfWeek)
        print('(6) Holiday: ', self.holiday)
        print('(7) Closure: ', self.closure)
    
    
    
    
    
