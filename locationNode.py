# Node class for the map

class locationNode:
    # initializer / instance attributes
    def __init__(self, name, speedLimit, northNeighbor, distanceNorth, southNeighbor, distanceSouth, eastNeighbor, distanceEast, westNeighbor, distanceWest):
        self.name = name
        self.speedLimit = speedLimit
        
        # set the north node data
        self.northNeighbor = northNeighbor
        self.distanceNorth = distanceNorth
        if 'null' != distanceNorth:
            self.timeNorth = self.calcTravelTime(distanceNorth, speedLimit)
        else:
            self.timeNorth = 0
        
        # set the south node data
        self.southNeighbor = southNeighbor
        self.distanceSouth = distanceSouth
        if 'null' != distanceSouth:
            self.timeSouth = self.calcTravelTime(distanceSouth, speedLimit)
        else:
            self.timeSouth = 0
        
        # set the east node data
        self.eastNeighbor = eastNeighbor
        self.distanceEast = distanceEast
        if 'null' != distanceEast:
            self.timeEast = self.calcTravelTime(distanceEast, speedLimit)
        else:
            self.timeEast = 0
        
        # set the west node data
        self.westNeighbor = westNeighbor
        self.distanceWest = distanceWest
        if 'null' != distanceWest:
            self.timeWest = self.calcTravelTime(distanceWest, speedLimit)
        else:
            self.timeWest = 0
    
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
    
    # this function returns the distance it takes to travel between nodes
    def getDistance(self, neighbor):
        if self.northNeighbor == neighbor:
            return self.distanceNorth
        elif self.southNeighbor == neighbor:
            return self.distanceSouth
        elif self.eastNeighbor == neighbor:
            return self.distanceEast
        elif self.westNeighbor == neighbor:
            return self.distanceWest
        else:
            print("Not a valid neighbor")
    
    # this function returns the time it takes to get between nodes
    def getTime(self, neighbor):
        if self.northNeighbor == neighbor:
            return self.timeNorth
        elif self.southNeighbor == neighbor:
            return self.timeSouth
        elif self.eastNeighbor == neighbor:
            return self.timeEast
        elif self.westNeighbor == neighbor:
            return self.timeWest
        else:
            print("Not a valid neighbor")
    
    # this function will calculate the time it takes to get from one node to another
    def calcTravelTime(self, distance, speed):
        # time = distance/speed
        # time is set in minutes
        # speed is mph
        # distance is miles
        time = int(distance) / int(speed)
        return int(time * 60)
        