#!/usr/bin/env python3
list1=['cisco_nxos', 'arista_eos','cisco ios']
print(list1[1])
list1.extend(['juniper'])
print(list1)
list1.append(['10.1.0.1','10.2.0.1','10.3.0.1'])
print(list1)
print(list1[4])
# for the command above, it will print the 3 ips instead of 1 object. Why? Because we placed a list INSIDE of a list! The append function adds ‘something’ at the end of a list. Since we specified a list with the square brackets [], we placed a list inside of another list! Cool.

#the command below will go to the intended place, then parse for the value in .. [ ? ]

print(list1[4][0])

