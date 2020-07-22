from a09FuncDefn import *
stuff(-5)   # use func from file a09...

v1 = [2,4,6]
v2 = [4,3,12, -9]
print (total (v1, v2)) # use func from file a09...

v3 = [(x + y) for x, y in zip(v1,v2)]
print (v3)
del v2[1:3]
v3 = [(x + y) for x, y in zip(v1,v2)]
print (v3)
