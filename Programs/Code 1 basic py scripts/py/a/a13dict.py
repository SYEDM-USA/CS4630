#dictionaires ... key (imutable), value
dict1 = {(123, 'abc') : 7042, 'lennox': [2, 4, 3]}
dict1['dawn'] = 'school' # add 
print (dict1.keys())
print (dict1.items())

print ('123' in dict1) # check for key '123'
#many methods pp, clear, get, ...
dict1.pop('lennox')     # remove
print (dict1.items())



