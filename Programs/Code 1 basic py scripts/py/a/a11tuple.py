#tuples: comma separated, not mutable
q = ['a', 123]
r = 123, 543, 'abc'
s = r, (1,2)
t = "lone",
u = ()

#any seq can be unpcked -> dist across elements
r1,r2,r3 = r
q1,q2 = q
print (r,s,t,u)
print (r1,r2,q2)
