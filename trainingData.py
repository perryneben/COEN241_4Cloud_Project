#!/bin/python

trainingDataDefinition = [
	{   "name": "lengthFeet",
		"decsription": "A road segment's length in feet.",
		"values": "Any positive integer.",
		"exampleValue": 1000
	},
	{   "name": "speedLimitMph",
		"description": "Speed limit for a road segment.",
		"values": "Any positive integer.",
		"exampleValue": 25
	},
	{   "name":	"numLanes",
		"description": "Number of lanes per direction.",
		"values": "Any positive integer.",
		"exampleValue": 2
	},
	{   "name":	"dividedTraffic",
		"description": "Is the road segment's bidirectional traffic divided?",
		"values": "0 for no division, 1 for divided or one-way.",
		"exampleValue": 0
	},
	{   "name":	"trafficLights",
		"description": "Number of traffic lights on this road segment.",
		"values": "Any positive integer.",
		"exampleValue": 2
	},
	{   "name": "stopSigns",
		"description": "Number of stop signs on this road segment.",
		"values": "Any positive integer.",
		"exampleValue": 0
	},
	{   "name":	"pedestrianCrossings",
		"description": "Number of pedestrian crossings.",
		"values": "Any positive integer.",
		"exampleValue": 1
	},
	{   "name":	"dayOfWeek",
		"description": "Day of the week.",
		"values": "Su=0, M=1, Tu=2, W=3, Th=4, F=5, Sa=6",
		"exampleValue": 5
	},
	{   "name":	"holiday",
		"description": "Is the day a holiday.",
		"values": "Not a holiday=0, Holiday=1",
		"exampleValue": 1
	},
	{   "name":	"timeOfDay",
		"description": "Time of day in minutes after midnight.",
		"values": "0-1439",
		"exampleValue": 540
	},
	{   "name":	"cloudWeather",
		"description": "Type of weather from the cloud service.",
		"values": "Dry/Clear=0, LightRain=1, HeavyRain=2, LightSnow=3, HeavySnow=4, Ice/DenseFog=5",
		"exampleValue": 2
	},
	{   "name":	"cloudTraffic",
		"description": "Type of traffic on the road segment from the cloud service.",
		"values": "None=0, Little=1, Moderate=2, Heavy=3, Gridlock=4",
		"exampleValue": 3
	},
	{   "name":	"cloudEvent",
		"description": "Road blocking event on road from the cloud service.",
		"values": "No Event=0, Road blocking event=1",
		"exampleValue": 0
	},
	{   "name":	"localWeather",
		"description": "Type of weather from the local autonomous vehicle source.",
		"values": "Dry/Clear=0, LightRain=1, HeavyRain=2, LightSnow=3, HeavySnow=4, Ice/DenseFog=5",
		"exampleValue": 2
	},
	{   "name":	"localTraffic",
        "description": "Type of traffic on the road segment from the local autonomous vehicle source.",
		"values": "None=0, Little=1, Moderate=2, Heavy=3, Gridlock=4",
		"exampleValue": 3
	},
	{   "name":	"localEvent",
		"description": "Road blocking event on road from the local autonomous vehicle source.",
		"values": "No Event=0, Road blocking event=1",
		"exampleValue": 0
	},
	{   "name": "travelTimeSeconds",
		"description": "Number of minutes taken to travel the road segment.",
		"values": "Any positive integer.",
		"exampleValue": 15
	}
]

def printDefinition():
    import pprint
    pprint.pprint(trainingDataDefinition, width=120)
    
def getNames():
    names = []
    for variable in trainingDataDefinition:
        names.append(variable['name'])
    return names

def printVars(vars):
    names = getNames()
    for i in range(len(vars)):
        print("%s: %d" % (names[i], vars[i]))