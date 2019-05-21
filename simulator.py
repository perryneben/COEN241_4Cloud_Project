import queue
from locationNode import *
from locationInitializor import *
from helperFunctions import *

# just testing the functions and linking of the python files

print(a1.getDistance('b1'))
print(b1.getDistance('c1'))
print(c1.getDistance('c2'))
print(d1.getDistance('c1'))
z = a2.getTime('a1')

print('It will take ' + str(z) + ' minutes to get from a2 to a1')


start_city = input('Please enter the starting point: ')
print('The starting city input is: ' + start_city)

q = buildNodeQueue()

while True:
    if q.empty():
        break
    x = q.get()
    print('The node name is: ' + x.getNodeName())

print('exited while loop')