import sys

value = sys.argv[1]
print("Calculating 2 * ",value)
result = 2 * value

file = open('result.txt','w') 
file.write(result)
file.close()
