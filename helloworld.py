import sys
import numpy as np

print("Numpy version: ", np.__version__)

value = sys.argv[1]
outputLocation = sys.argv[2]
print("Calculating 2 * ",value)
result = 2 * value

print("Writing to file ",outputLocation)
file = open(outputLocation,'w') 
file.write(result)
file.close()

print("Terminated successfully")
