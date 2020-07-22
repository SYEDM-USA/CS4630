x, y = 1, 2
print(x,y)
print(format(x,"3d"), format(x,"1.1f"))  #^^1^1.0
print(repr(x).rjust(5), y)

#1st field x in 2 decimal, next in 4 decimal
print('{0:2} {1:4d}'.format(x, x*x))

formattedX = format(x,"4.5f")
print(x, formattedX, format(x,"4.5f"))

print ("hello".zfill(8)) #hello 8 col left 0 filled
print ("hello".zfill(8).rjust(15)) # + in 15 col rt just

print('{0} and {1}'.format('hello', 'world'))
