# Node class for the map
from predictML import *

class locationNode:
    # initializer
    def __init__(self, name, speedLimit):
        self.name = name
        # speed limit is MPH
        self.speedLimit = speedLimit
        self.weather = 0
        self.traffic = 0
        self.timeOfDay = 1000
        self.dayOfWeek = 0
        self.holiday = 0
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
        self.speedLimit = int(speedLimit)
    
    # this function sets the weather conditions at the node
    def setWeather(self, weather):
        self.weather = int(weather)
    
    # this function sets the traffic conditions at the node
    def setTraffic(self, traffic):
        self.traffic = int(traffic)

    # this function sets the time of day it is at the node
    def setTimeOfDay(self, timeOfDay):
        self.timeOfDay = int(timeOfDay)
    
    # this function sets the day of the week it is
    def setDayOfWeek(self, dayOfWeek):
        self.dayOfWeek = int(dayOfWeek)
    
    # this function sets if it is a holiday
    def setHoliday(self, holiday):
        self.holiday = int(holiday)
    
    # this function sets if a node has been closed
    def setNodeClosure(self, closure):
        self.closure = closure
    
    def printNodeAttributes(self):
        print('Name: ', self.name)
        print('(1) Speed Limit: ', self.speedLimit)
        print('(2) Weather: ', self.weather)
        print('(3) Traffic: ', self.traffic)
        print('(4) Time of Day: ', self.timeOfDay)
        print('(5) Day of Week: ', self.dayOfWeek)
        print('(6) Holiday: ', self.holiday)
        print('(7) Closure: ', self.closure)
    
    # this function calls the Machine learning model to get a prediction of the time it
    # will take to traverse the route
    def predictTravelTime(self):
        # iterate through all of the neighbors to this node using the index so we can
        # also access the distance to them simultaneously
        for i in range(len(self.neighbors)):
            # create the array to hold the variables
            pVar = []
            # get the neighbor and distance to them
            n = self.neighbors[i]
            d = self.distances[i]
            # set the values of the array that is passed to the predict function
            lengthFeet = d * 5280 # convert from miles to feet
            speedLimitMph = n.speedLimit
            dayOfWeek = n.dayOfWeek
            holiday = n.holiday
            timeOfDay = n.timeOfDay
            localWeather = n.weather
            localTraffic = n.traffic
            # set default values for 
            numLanes = 1
            dividedTraffic = 1
            trafficLights = 0
            stopSigns = 1
            pedestrianCrossings = 1
            cloudWeather = 1
            cloudTraffic = 1
            cloudEvent = 0
            #####
            travelTimeSeconds = 0

            pVar.append(lengthFeet)
            pVar.append(speedLimitMph)
            pVar.append(numLanes)
            pVar.append(dividedTraffic)
            pVar.append(trafficLights)
            pVar.append(stopSigns)
            pVar.append(pedestrianCrossings)
            pVar.append(dayOfWeek)
            pVar.append(holiday)
            pVar.append(timeOfDay)
            pVar.append(cloudWeather)
            pVar.append(cloudTraffic)
            pVar.append(cloudEvent)
            pVar.append(localWeather)
            pVar.append(localTraffic)
            pVar.append(travelTimeSeconds)
            
            # predicted time is in seconds so convert it to minutes
            predictedTime = predict(pVar) / 60
            
            roundedPrediction = round(predictedTime[0], 2)
            self.times.append(abs(roundedPrediction))


