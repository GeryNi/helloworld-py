import sys

value = sys.argv[1]
outputLocation = sys.argv[2]
print("Calculating 2 * ",value)
result = 2 * value

file = open(outputLocation,'w') 
file.write(result)
file.close()
