import math

list= [12, 24, 36, 48, 60]
print("List : " + str(list))

mean = sum(list) / len(list)
var = sum((l-mean)**2 for l in list) / len(list)
st_dev = math.sqrt(var)

print("Standard deviation of the given list: " + str(st_dev))