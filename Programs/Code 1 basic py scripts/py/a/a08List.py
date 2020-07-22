#List is an iteratable object
list1 = ['spam', 'eggs', 100, 1234, 2*2]
for element in list1:
  print (element)

list1.pop(0) #1st element out
list1.append(1) # add to end
print (list1)

list1.pop() #LIFO
list2 = ['garbage', 'trash']

#Add each element of list2 to list 1?
#use a loop or use extend
list1.extend(list2) 

print (list1)
print (list1.count('eggs'))
