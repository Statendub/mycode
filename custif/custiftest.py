#!/usr/bin/env python3

message = 'The postage amount needed is '
print('How much does your letter weigh?')

weight = float(input())
if weight <=0:
	message = message + 'nothing'
elif (weight >0) and (weight <= 1):
	message = message + '.55'
elif weight > 1:
	message = message + str((1.15)*float(weight))
elif weight > 5:
	message = message + str((.90)*(weight))
elif weight == 0:
	message = message + '0'
print(message)
	
