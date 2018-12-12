#!/usr/bin/env python3
my_list = [ "192.168.1.1", 5060, "up"]
#previous line creates a list called "my_list" with parameters inside the brackets []
print("the first item in the list (IP):"+my_list[0])

#lists always start with [0]for first item not "1", create the list by assigning a value and the list items

#Strings are surrounded with quotes. We may not combine unlike data types within Python.below is the solution. We can force an integer value to be a string with the str() function.

print("the second item in the list (port): "+ str(my_list[1]) )
print("the last item in the list (state): "+my_list[2])

#the "+str(my_list[1])) turned 5060 interger to a list header as opposed to an integer

new_list = [5060, "80", 55, "10.0.0.1", "10.0.2.30", "ssh"]
print("When i ssh into IP address: " + new_list[3],'or ' + new_list[4] + "i am unable to ping ports:"+ str(new_list[0]) + (new_list[1]),'or'',' + str(new_list[2]))


