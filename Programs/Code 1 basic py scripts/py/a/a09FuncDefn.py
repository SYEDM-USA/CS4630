def total(x, y):
  return [x[i]+y[i] for i in range(len(x)) ]
 
def stuff(n):
  if n < 0:
    print ("n is -ve")

def total(x, y):
  return [x[i]+y[i] for i in range(len(x)) ]

#use these functions ...
stuff(-5)

v1 = [2,4,6]
v2 = [4,3,12, -9]
print (total (v1, v2))

v3 = [(x + y) for x, y in zip(v1,v2)]
print (v3)
del v2[1:3]
v3 = [(x + y) for x, y in zip(v1,v2)]
print (v3)
