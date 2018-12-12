#!/usr/bin/env python3
proto= ['ssh','http', 'https']
protoa= ['ssh','http','https']
print(proto)
print(proto[1])
#list.extend or append examples which either add individual object to existing list or adds the list as an embedded list into the existing list
# proto.extend('dns') #this COMMAND added term 'dns', to the end of our list


# demonstrate the difference between append() and extend(). The former appends an object to the end of the list (e.g., another list), while the later appends each element of the iterable object (e.g., another list) to the end of the list. To do this, we’ll need a second list

proto.append('dns')  #this line will add 'dns' to the end of our list 
protoa.append('dns') #this line will add 'dns' to the end of our list
print(proto)

proto2= [22,80,443,53] #made a list of common ports for example below
proto.extend(proto2) #pass proto2 as an argument to the extend method -- then print result
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method then print result
print(protoa)
