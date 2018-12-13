#!/usr/bin/env python3

#ipchk=input('apply an ip address: ') #this line will now prompt for the ip 

#if ipchk: # if any data is provided, this will test true 
#print('looks like the ip address was set: ' + ipchk) #must indent under IF
#else: #if data NOT provided or wrong
#	print('you did not provide input.') #indented under else
#script above showing how to take input and check it , You’ll also notice that any value causes our script to test true, not just IP addresses.


ipchk = input('Apply an IP address: ') # declaring variable for ipchk 

if ipchk == '192.168.70.0': #if the variable is equal 'then' on next line
    print('looks like ip addy of the gateway was set to: ' + ipchk + ' this is not recommended.') #indented
elif ipchk: #if ANY data is provided, this will test true
    print('looks like the ip address was set to: ' + ipchk) #indented
else: #if data NOT provided
    print('you did not provide input') #indented


