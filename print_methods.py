x=1.5
y=2

print ("method 1, x: %8.3f y: %i" % (x,y)) # 8 = number of spaces the entire number takes, 3 = number of decimal places, f = float
print ('method 2, x: ' + str(x) + ' y: ' + str(y))
print ('method 3, x: {} y: {}'.format(x,y))
print ('method 4, ',x,y)

print ("%s is %i years old" % ("John", 23)) # %s = string, %i = integer